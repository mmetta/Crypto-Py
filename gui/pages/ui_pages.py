# -*- coding: utf-8 -*-
# ##############################################################################
# Form generated from reading UI file 'pagesKqgMQx.ui'
#
# Created by: Qt User Interface Compiler version 6.4.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
# ##############################################################################

from py_Core import *
from gui.pages.page_01 import Py_Page_1
from gui.pages.page_02 import Py_Page_2
from gui.pages.page_03 import Py_Page_3


class Ui_StackedWidget(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1056, 657)

        self.page_1 = Py_Page_1()
        application_pages.addWidget(self.page_1)

        self.page_2 = Py_Page_2()
        application_pages.addWidget(self.page_2)

        self.page_3 = Py_Page_3()
        application_pages.addWidget(self.page_3)

        QMetaObject.connectSlotsByName(application_pages)
    # setupUi
