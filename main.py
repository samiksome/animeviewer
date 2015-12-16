#!/usr/bin/python

import gatherer

searchterms = raw_input(">")
matchlist = gatherer.fast_search("anime-titles.xml",searchterms)
for i,v in enumerate(matchlist):
	print i, v

