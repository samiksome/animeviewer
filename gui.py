#!usr/bin/env python

from gi.repository import Gtk
import gatherer
import xml.etree.ElementTree

class Handler:
	def onDeleteWindow(self,*args):
		print "quitting"
		Gtk.main_quit()

	def closeButtonClicked(self,*args):
		Gtk.main_quit()
	
	def searchButtonClicked(self,*args):
		bounds = searchtextbuffer.get_bounds()
		searchterms = searchtextbuffer.get_text(bounds[0],bounds[1],False)

		matchlist = gatherer.search("anime-titles.xml",searchterms)
		populate_results(matchlist)

		headline.set_text("Search results")
		searchresultscreen.show()
		searchscreen.hide()

	def searchResultActivated(self,*args):
		aid = args[1].get_children()[0].get_children()[1].get_text()
		dispname = args[1].get_children()[0].get_children()[0].get_text()
		populate_info(aid,dispname)

		headline.set_text("Anime information")
		infoscreen.show()
		searchresultscreen.hide()

def populate_results(matchlist):
	for item in matchlist:
		row = Gtk.ListBoxRow()
		hbox = Gtk.Box(Gtk.Orientation.HORIZONTAL,0)
		row.add(hbox)
		label = Gtk.Label(item[1],xalign=0)
		label_aid = Gtk.Label(item[0],xalign=0)
		hbox.pack_start(label,True,True,0)
		hbox.pack_start(label_aid,True,False,0)
		hbox.show()
		label.show()
		row.show()
		searchresultlist.add(row)

def populate_info(aid,dispname):
	info = gatherer.get_info(aid)
	root = xml.etree.ElementTree.fromstring(info)
	imgid = root.find('picture').text
	img = gatherer.get_img(imgid)
	
	animepicture.set_from_file("img_cache/"+imgid)
	animetitle.set_text(dispname)
	animedescription.set_text(root.find('description').text)
	animeinfo.set_text("Type: "+root.find('type').text+"\nOriginal run: "+root.find('startdate').text+" to "+root.find('enddate').text+"\nEpisodes: "+root.find('episodecount').text)

gladefile = "gui.glade"
builder = Gtk.Builder()
builder.add_from_file(gladefile)
builder.connect_signals(Handler())

window = builder.get_object("MainWindow")
headline = builder.get_object("headline")
closebutton = builder.get_object("closebutton")
searchscreen = builder.get_object("searchscreen")
searchresultscreen = builder.get_object("searchresultscreen")
searchresultlist = builder.get_object("searchresultlist")
infoscreen = builder.get_object("infoscreen")

searchtextbuffer = builder.get_object("searchtextbuffer")
animepicture = builder.get_object("animepicture")
animetitle = builder.get_object("animetitle")
animeinfo = builder.get_object("animeinfo")
animedescription = builder.get_object("animedescription")

headline.set_text("Search for anime")
window.fullscreen()
window.show_all()
searchresultscreen.hide()
infoscreen.hide()

Gtk.main()
