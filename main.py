#!/usr/bin/python

import gatherer

searchterms = raw_input("search title ")
matchlist = gatherer.search("anime-titles.xml",searchterms)
for i in range(len(matchlist)):
	print str(i+1)+": "+matchlist[i][1]
	
