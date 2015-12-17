#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView
import xml.etree.ElementTree
import gatherer

def search_start(searchterms):
    matchlist = gatherer.search("anime-titles.xml",searchterms)
    info = gatherer.get_info(matchlist[0][0])
    xmlroot = xml.etree.ElementTree.fromstring(info)
    imgid = xmlroot.find('picture').text
    gatherer.get_img(imgid)
    root.clearSearchInput()
    root.setAnimeInfo(matchlist[0][1],"img_cache/"+imgid)
    root.setInfoAreaVisibility(True)
    
def browse_back():
    print "browse back"
    
def browse_forward():
    print "browse forward"

app = QApplication(sys.argv)
view = QDeclarativeView()
url = QUrl('gui.qml')
view.setSource(url)
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

root = view.rootObject()

root.exit_gui.connect(app.quit)
root.search_start.connect(search_start)
root.browse_back.connect(browse_back)
root.browse_forward.connect(browse_forward)

view.showFullScreen()
sys.exit(app.exec_())
