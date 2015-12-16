#!usr/bin/env python

from gi.repository import Gtk

class Handler:
	def onDeleteWindow(self,*args):
		print "quitting"
		Gtk.main_quit()
	
	def buttonClicked(self,*args):
		print "click"
		textbuffer.set_text("clicked button")
		

gladefile = "gui.glade"
builder = Gtk.Builder()
builder.add_from_file(gladefile)
builder.connect_signals(Handler())

window = builder.get_object("MainWindow")
textbuffer = builder.get_object("textbuffer1")
textbuffer.set_text("This is default text")

window.show_all()

Gtk.main()
