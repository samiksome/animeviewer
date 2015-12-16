#!/usr/bin/python

from xml.dom.minidom import parse
import xml.dom.minidom

def search(file,str):
	DOMTree = xml.dom.minidom.parse(file)
	collection = DOMTree.documentElement
	animes = collection.getElementsByTagName("anime")

	for anime in animes:
		titles = anime.getElementsByTagName("title")

		jpname = ""
		enname = ""
		for title in titles:
			if(title.getAttribute("xml:lang")=="x-jat" and title.getAttribute("type")=="main"):
				jpname = title.childNodes[0].data
			elif(title.getAttribute("xml:lang")=="en" and title.getAttribute("type")=="official"):
				enname = title.childNodes[0].data

		words = str.split()
		allwords = True
		for word in words:
			if(not(word.lower() in jpname.lower()) and not(word.lower() in enname.lower())):
				allwords = False
				break
		if(allwords):
			if(enname==""):
				print jpname
			elif(jpname==""):
				print enname
			else:
				if(enname==jpname):
					print enname
				else:
					print enname+" | "+jpname