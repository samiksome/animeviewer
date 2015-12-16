#!/usr/bin/env python

import xml.dom.minidom
import xml.etree.ElementTree

import time

def search(file,searchterms):
        starttime = time.time()

	DOMTree = xml.dom.minidom.parse(file)
	collection = DOMTree.documentElement
	animes = collection.getElementsByTagName("anime")

	endtime = time.time()
	print 'Time taken for preprocessing:', endtime - starttime

	matchlist=[]
	starttime = time.time()
	for anime in animes:
		titles = anime.getElementsByTagName("title")

		jpname = ""
		enname = ""
		for title in titles:
			if(title.getAttribute("xml:lang")=="x-jat" and title.getAttribute("type")=="main"):
				jpname = title.childNodes[0].data
			elif(title.getAttribute("xml:lang")=="en" and title.getAttribute("type")=="official"):
				enname = title.childNodes[0].data

		words = searchterms.split()
		allwords = True
		for word in words:
			if(not(word.lower() in jpname.lower()) and not(word.lower() in enname.lower())):
				allwords = False
				break
		if(allwords):
			dispname = ""
			if(enname==""):
				dispname = jpname
			elif(jpname==""):
				dispname = enname
			else:
				if(enname==jpname):
					dispname = enname
				else:
					dispname = enname+" | "+jpname
			matchlist.append([anime.getAttribute("aid"),dispname])

        endtime = time.time()
        print 'Time taken for search:', endtime - starttime

        return matchlist

def fast_search(filename, searchterm):
    starttime = time.time()

    DOMtree = xml.etree.ElementTree.parse(filename)
    root = DOMtree.getroot()

    endtime = time.time()
    print 'Time taken for preprocessing:', endtime - starttime

    matchlist = []

    starttime = time.time()

    for anime in root:

        jpname, enname = "", ""
        for title in anime:
            if title.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'x-jat' and title.attrib['type'] == 'main':
                jpname = title.text
            elif title.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == 'en' and title.attrib['type'] == 'official':
                enname = title.text

        words = searchterm.split()
        allwords = True
        for word in words:
	    if not(word.lower() in jpname.lower()) and not(word.lower() in enname.lower()):
		allwords = False
		break

	if allwords:
	    if enname == "":
		dispname = jpname
	    elif jpname == "":
		dispname = enname
	    else:
		if enname == jpname:
		    dispname = enname
		else:
		    dispname = enname + " | " + jpname

	    matchlist.append([anime.attrib['aid'], dispname])

    endtime = time.time()
    print 'Time taken for search:', endtime - starttime

    return matchlist
