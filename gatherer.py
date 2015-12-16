#!/usr/bin/env python

from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.ElementTree

def search(filename, searchterm):
    DOMtree = xml.etree.ElementTree.parse(filename)
    root = DOMtree.getroot()

    matchlist = []
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

    return matchlist
