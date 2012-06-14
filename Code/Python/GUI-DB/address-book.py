#!/usr/bin/python
import pygtk
pygtk.require('2.0')

import gtk
import gtk.glade

class AddressBook(object):
    def __init__(self):
        self.address ={'raj':("srgdsf",'324234'),
                  'sam':("fdsg",'f324234'),
                  'ram kumar':("dvsvsrgdsf",'32df4234'),
                  'sumesh':("srgfdsdsf",'3d324234'),
                  'prashanth':("xzccsrgdsf",'32324234')}
        
        glade_file="/home/vimal/Projects/pycode-browser/Code/Python/GUI-DB/address-book.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(glade_file)
        #main window
        self.wmain = self.builder.get_object("AddressBook")

        self.builder.connect_signals(self)
        self.win = self.builder.get_object("AddressBook")
        self.enName=self.builder.get_object("enName")
        self.enEmail=self.builder.get_object("enEmail")
        self.enPhone=self.builder.get_object("enPhone")
        self.bnFind = self.builder.get_object("btnSearch")
        autoname = gtk.EntryCompletion()
        self.enName.set_completion(autoname)
        completion_model_name = self.__create_names_completion_model()
        autoname.set_model(completion_model_name)
        autoname.set_text_column(0)
        autoname.connect("match-selected",self.on_name_selected)
   
    def __create_names_completion_model(self):
        try:
            store = gtk.ListStore(str)
            for key_word in self.address.keys():
                iter = store.append()
                store.set(iter,0,key_word)
            return store
        except:
            store = []
            return store
    
    def on_name_selected(self, completion, model, iter):
        self.bnFind.activate()
        
    def on_btnSearch(self,object):
        name=self.enName.get_text()
        if self.address.has_key(name):
            self.enEmail.set_text(self.address[name][0])
            self.enPhone.set_text(self.address[name][1])
    
        else:
            dialog = gtk.MessageDialog(self.win,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_ERROR, gtk.BUTTONS_OK,
                "Name not found in the database")
            dialog.run()
            dialog.destroy()
    def on_addressbookDistroy(self,object):
        gtk.main_quit()

w=AddressBook()
gtk.main()
