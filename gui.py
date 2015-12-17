#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView

app = QApplication(sys.argv)
view = QDeclarativeView()
url = QUrl('gui.qml')
view.setSource(url)
view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
view.show()
sys.exit(app.exec_())
