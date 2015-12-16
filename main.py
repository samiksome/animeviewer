#!/usr/bin/python

import gatherer
import xml.etree.ElementTree

searchterms = raw_input("title>")
matchlist = gatherer.search("anime-titles.xml",searchterms)
for i,v in enumerate(matchlist):
	print i+1, v[1]

chosen_anime = int(raw_input("choose>"))
chosen_anime = chosen_anime-1
info = gatherer.get_info(matchlist[chosen_anime][0])
root = xml.etree.ElementTree.fromstring(info)
imgid = root.find('picture').text
img = gatherer.get_img(imgid)
img.show()
print info
