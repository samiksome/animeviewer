#!/usr/bin/env python

import xml.etree.ElementTree
import os, urllib, gzip

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

BASE_URL="http://api.anidb.net:9001/"
ARGS="httpapi?request=anime&client=mantisviewer&clientver=1&protover=1"

def get_info(aid):
	# check cache first
	if not os.path.exists("info_cache/"+aid+".xml"):
		urllib.urlretrieve(BASE_URL+ARGS+"&aid="+aid, "info_cache/"+aid+".xml.gz")
		with gzip.open("info_cache/"+aid+".xml.gz") as f:
			content = f.read()
		f = open("info_cache/"+aid+".xml", "w")
		f.write(content)
		f.close()
		os.remove("info_cache/"+aid+".xml.gz")

	with open("info_cache/"+aid+".xml", "r") as f:
		info = f.read()
	return info
