#!/usr/bin/python

import gatherer

searchterms = raw_input("search title ")
matchlist = gatherer.search("anime-titles.xml",searchterms)
for i in range(len(matchlist)):
	print str(i+1)+": "+matchlist[i][1]
	
chosen_anime = input("choose ")
chosen_anime = chosen_anime-1
info = gatherer.get_info(matchlist[chosen_anime][0])
