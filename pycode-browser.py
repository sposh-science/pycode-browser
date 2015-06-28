#!/usr/bin/python
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#(c) SPACE 2007 www.space-kerala.org
#Authors: 
# Vibeesh P <vibeesh@space-kerala.org>, 
# Vimal Joseph <vimal.joseph@zyxware.com> (modified on march 2, 2010 by  to change the script to browse python programmes.)
# march 9, 2010 added save and some interface changes.
# April 3, 2010 replaced the gtktextview with gtksourceview for syntax highlighting and line
# numbering. 
# May 3, 2010 now the modified programmes will execute in /tmp and will be deleted when exiting the application
# May 8, 2010, the vte terminal added
# June 14, 2012 Minor corrections in the class name.
# version 0.93


import os, stat, sys, time
from gi.repository import Vte
import pygtk
pygtk.require('2.0')
from gi.repository import Gtk

from user import home
import shutil
from gi.repository import GtkSource
from gi.repository import GLib

#GLOBALDIR = os.path.join(sys.prefix, 'share', 'pycode')
#GLOBALDIR = ""
#DEFAULTS = {
#	'gladefile': os.path.join(GLOBALDIR, 'glade', 'pycode.glade'),
#	'code_dir': os.path.join(GLOBALDIR, 'Code'),
#}

def abs_path_gui(gladefile):
        name = sys.argv[0]
        dirname = os.path.dirname(name)
        if dirname != '':
            name = os.path.dirname(name) + os.sep + 'gui' + os.sep + gladefile
        else:
            name = 'gui' + os.sep + gladefile
        return name
def abs_path():
        name = sys.argv[0]
        dirname = os.path.dirname(name)
        if dirname != '':
            name = os.path.dirname(name) + os.sep
        else:
            name = '.'
        return name

def get_language_for_mime_type(mime):
    lang_manager = GtkSource.LanguageManager.get_default()
    lang_ids = lang_manager.get_language_ids()
    for i in lang_ids:
        lang = lang_manager.get_language(i)
        for m in lang.get_mime_types():
            if m == mime:
                return lang
    return None

#####  FileBrowser  #########################################################

class FileBrowser_pycode( object ):
    """Holds a gtk widget that acts as a file browser.  It must be
    initialized with a root directory.
    """
    def __init__( self, root_dir, filter_out_extensions = [] ):
        self.root_dir  = root_dir
        self.filter_out_ext = filter_out_extensions

        ## The store will contain:
        ## 0. filename (str)
        ## 1. whether it's a directory (bool)
        ## 2. file size (int)
        ## 3. last modified (str)
        column_mapping = [ 0, 2, 3 ]    # From user columns to model columns
        self.file_structure = Gtk.TreeStore(str, bool)
        self.populate_tree(root_dir, self.file_structure.get_iter_first())
        uifile = abs_path_gui("gui.ui")
        wTree = Gtk.Builder()
        wTree.add_from_file(uifile)
        # wTree=Gtk.glade.XML(gladefile)
        ## Create the treeview and link it to the model
        # self.w_treeview = wTree.get_widget("treeview")
        self.w_treeview = wTree.get_object("treeview")
        self.w_treeview.set_model(self.file_structure)

        self.srcView = GtkSource.View()
        self.srcBfr = self.srcView.get_buffer()
        #mgr = gtksourceview.SourceLanguagesManager()
        srcLanguage = get_language_for_mime_type("text/x-python")
        
        #self.helpBfr = Gtk.TextBuffer()
        self.srcScrolledWindow = wTree.get_object("srcScrolledWindow")
        # self.srcView = gtksourceview.View(self.srcBfr)
        self.srcScrolledWindow.add(self.srcView)
        self.srcBfr.set_language(srcLanguage)
        self.srcBfr.set_highlight_syntax(True)
        self.srcView.set_buffer(self.srcBfr)
        self.srcView.set_show_line_numbers(True)
        context = self.srcView.get_pango_context()
        font = context.get_font_description()
        font.set_size(int(font.get_size() * 1.5))
        self.srcView.modify_font(font)
        #self.srcView.set_editable(False)
        self.srcView.show()
        self.terminalScrolledWindow = wTree.get_object("terminalScrolledWindow")
        self.terminal_expander = wTree.get_object("terminalexpander")
        self.terminal = Vte.Terminal()
        self.terminalScrolledWindow.add(self.terminal)
        self.terminal.show()
        #self.helpView = wTree.get_widget("helpView")
        #self.helpView.set_buffer(self.helpBfr)
        self.srcBfr.set_text("#Python Code Browser: Select a python program from the left panel")
        self.btnExecute=wTree.get_object("btnExecute")
        self.btnSaveas=wTree.get_object("btnSaveas")
        self.tbtnExecute=wTree.get_object("tbtnExecute")
        self.tbtnSaveas=wTree.get_object("tbtnSaveas")
        dic={"on_frm_treeview_delete_event": self.quit, 
             "quit_clicked": self.quit,
             "execute_clicked":self.open_file,
             "on_treeview_cursor_changed":self.disp_details,
             "saveas_clicked":self.save_as,
             "about_clicked":self.about}
        wTree.connect_signals(dic)
        ## Create the columns to view the contents
        self.columns = [ Gtk.TreeViewColumn(title) for title in ['Filename'] ]
        self.w_cell = Gtk.CellRendererText()
        self.w_cell.set_property("xalign",0)
        for i,column in enumerate(self.columns):
            self.w_treeview.append_column(column)
            column.set_property("resizable", True)
            column.pack_end(self.w_cell, True)
            column.add_attribute(self.w_cell, 'text', column_mapping[i])

        ## Create a cell-renderer that displays a little directory or
        ## document icon depending on the file type
        self.w_cellpix = Gtk.CellRendererPixbuf()
        self.w_cellpix.set_property("xpad", 8)
        self.w_cellpix.set_property("xalign", 0)
        
        def pix_format_func(treeviewcolumn, cell, model, iter, dummyParam):
          if model.get(iter,1)[0]:
             cell.set_property("stock-id", Gtk.STOCK_DIRECTORY)
          else:
             cell.set_property("stock-id", Gtk.STOCK_ABOUT)
             
        self.columns[0].pack_start(self.w_cellpix, expand=True)
        self.columns[0].set_cell_data_func(self.w_cellpix, pix_format_func)

    def quit(self,*args):
        Gtk.main_quit()
    def execute (self,src):
        cmd = "/usr/bin/python"
        if self.srcBfr.get_modified()==True:
            tname="pycode-0007-0007.py"
            f = open("/tmp/"+tname,"w")
            f.write(self.srcBfr.get_text(self.srcBfr.get_start_iter(), self.srcBfr.get_end_iter(), include_hidden_chars=False))
            f.close()
            #os.system("cp "+src+" /tmp/"+fname)
            argv = [cmd, "/tmp/"+tname]
        else:
            argv = [cmd, src]
        self.terminal.reset(True, True)
        self.terminal.grab_focus()
        self.terminal.spawn_sync (pty_flags=Vte.PtyFlags.DEFAULT,
                                  working_directory='.',
                                  argv=argv,
                                  envv=[],
                                  spawn_flags=GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                                  child_setup=None,
                                  child_setup_data=None,)
        self.terminal_expander.set_expanded(True)
    def open_file(self,obj):
    	model, parent_iter = self.w_treeview.get_selection().get_selected()
        pathname = self.get_pathname_from_iter(parent_iter)
        extn = os.path.splitext(pathname)[1]
        if extn == ".py":
	       	self.execute(pathname)
    def about(self,obj):
        abouttxt="Python Code Browser: Version 0.93\nCode: Vibeesh P., Vimal Joseph\nLicense: GNU GPL V3"
        #self.helpBfr.set_text(abouttxt)
        cmd = "echo"
        argv = [cmd, abouttxt]
        self.terminal.reset(True, True)
        self.terminal.fork_command(command=cmd,argv=argv)
        self.terminal_expander.set_expanded(True)
    def save_as(self,obj):
        dialog = Gtk.FileChooserDialog(title=None,action=Gtk.FILE_CHOOSER_ACTION_SAVE,buttons=(Gtk.STOCK_CANCEL,Gtk.RESPONSE_CANCEL,Gtk.STOCK_SAVE,Gtk.RESPONSE_OK))
        model, parent_iter = self.w_treeview.get_selection().get_selected()
        fpath = self.get_pathname_from_iter(parent_iter)
        path,filename = os.path.split(fpath)
        dialog.set_current_name(filename)
        response = dialog.run()
        if response == Gtk.RESPONSE_OK:
            if self.srcBfr.get_modified()==True:
                f = open(dialog.get_filename(),"w")
                f.write(self.srcBfr.get_text(self.srcBfr.get_start_iter(), self.srcBfr.get_end_iter()))
                f.close()
            else:
                shutil.copy(fpath,dialog.get_filename())
        elif response == Gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        dialog.destroy()



    def disp_details(self,view):
        model, parent_iter = view.get_selection().get_selected()
        path = self.get_pathname_from_iter(parent_iter)
        extn = os.path.splitext(path)[1]
        if extn == ".py":
            self.btnExecute.set_sensitive(True) 
            self.btnSaveas.set_sensitive(True) 
            self.tbtnExecute.set_sensitive(True) 
            self.tbtnSaveas.set_sensitive(True) 
            fname_without_extn  = os.path.splitext(path)[0]
            desc_fname = fname_without_extn + ".py"
            if os.path.isfile(desc_fname) == True:
                fl = open(desc_fname)
                desc = fl.read()
                fl.close()
                hdesc = "Click on Execute to run this program\nSave as to save the program and modify it"
                #add the hdesc to status bar
        else:
            desc="#Python Code Browser: Select a python program from the left panel" 
            hdesc="Select a python program from this directory"
            self.btnExecute.set_sensitive(False) 
            self.btnSaveas.set_sensitive(False) 
            self.tbtnExecute.set_sensitive(False) 
            self.tbtnSaveas.set_sensitive(False)   
    	self.srcBfr.set_text(desc)
        #self.helpBfr.set_text(hdesc)
        self.srcBfr.set_modified(False)
    	
    def get_pathname_from_iter( self, treeiter ):
        """Return a filesystem pathname from a tree in the path.  This
        involves looking up the filenames at each step and joining them.
        """
        m  = self.file_structure
        if treeiter:                    # Not at root
            treepath  = m.get_path(treeiter)
            filenames = [ ]
            while treeiter is not None:
                filenames.append(m.get_value(treeiter, 0))
                treeiter = m.iter_parent(treeiter)
            filenames.reverse()
        else:
            filenames = [ ]
        return os.path.join(*[self.root_dir]+filenames)

    def populate_tree( self, dir, treeparent, visit_subdirectories = True ):
        """Given a location in the tree (given by treeparent), fill out the
        file information.  Repopulation (i.e. calling a second time to
        update the tree) is not very well handled right nself.execute(pathname)ow.
        """
        m = self.file_structure
        files = []
        for f in os.listdir(dir):
		try:
                      if f[0] != '.':
	                if os.path.isdir(os.path.join(dir,f)):
				if len(os.listdir(os.path.join(dir,f))) > 0 and f!="gui":
		                	files.append(f)
				
                      	elif os.path.splitext(f)[1] in self.filter_out_ext:
                      		files.append(f)
	        except OSError,e:
			print e
        files.sort()
        ## Stat each file andself.lbl_desc construct the row
        for f in files:
            row = [ f, False]
            fname = os.path.join(dir, f)
            try:
                filestat = os.stat(fname)
                row[1] = stat.S_ISDIR(filestat.st_mode)
            except OSError:
                pass
            
            m.append(treeparent, row)

        ## Populate subdirectories if required
        if visit_subdirectories and len(files) > 0:
            n = m.iter_n_children(treeparent)
            for i in range(n):
                child_iter = m.iter_nth_child(treeparent,i)
                if m.get_value(child_iter,1): # It's a subdirectory
                    self.populate_tree(os.path.join(dir,files[i]),
                                       child_iter, visit_subdirectories)

    def set_double_click_callback( self, func ):
        """The callback is called with the following arguments:
        - filebrowser object
        - pathname of the file clicked (not necessarily absolute)
        - whether the file is a directory (bool
        """
        def treeview_callback(treeview, path, view_column):
            file_iter = treeview.get_model().get_iter(path)
            isdir = self.file_structure.get_value(file_iter, 1)
            pathname = self.get_pathname_from_iter(file_iter)
            func(self, pathname, isdir)
        
        self.w_treeview.connect("row-activated", treeview_callback)


#####  Standalone Running  ##################################################

if __name__ == "__main__":

    def my_callback(fb,pathname,isdir):
        extn  = os.path.splitext(pathname)[1]
        if extn == ".py":
        	fb.execute(pathname)
  
    fb = FileBrowser_pycode(os.path.join(abs_path(),'Code'),[".py"])
    fb.set_double_click_callback(my_callback)
    Gtk.main()
