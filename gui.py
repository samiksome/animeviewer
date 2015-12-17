#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView

def search_start(searchterms):
    print searchterms.split()
    root.clearSearchInput()

app = QApplication(sys.argv)
view = QDeclarativeView()
url = QUrl('gui.qml')
view.setSource(url)
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

root = view.rootObject()

root.exit_gui.connect(app.quit)
root.search_start.connect(search_start)

view.showFullScreen()
sys.exit(app.exec_())
