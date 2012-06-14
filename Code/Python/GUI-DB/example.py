#!/usr/bin/python
import pygtk
pygtk.require('2.0')

import gtk
import gtk.glade

class Example(object):
    def __init__(self):     
        glade_file="/home/vimal/Projects/pycode-browser/Code/Python/GUI-DB/example.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        #main window
        self.builder.connect_signals(self)
        self.enName=self.builder.get_object("enName")
        self.wmain = self.builder.get_object("Example")
        self.wmain.show()
    
    def on_btnOK_clicked(self,object):
        name=self.enName.get_text()
        dialog = gtk.MessageDialog(self.wmain,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
               name)
        dialog.run()
        dialog.destroy()

    def on_quit(self,object):
         gtk.main_quit()

w=Example()
gtk.main()
