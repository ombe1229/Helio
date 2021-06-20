# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(752, 549)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius: 8px;")
        self.drop_shadow_frame.setFrameShape(QFrame.StyledPanel)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: rgb(27, 29, 34);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        font = QFont()
        font.setFamily(u"Noto Sans CJK KR Bold")
        font.setPointSize(15)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(236, 240, 241);")

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_maxmize = QPushButton(self.frame_btns)
        self.btn_maxmize.setObjectName(u"btn_maxmize")
        self.btn_maxmize.setMinimumSize(QSize(16, 16))
        self.btn_maxmize.setMaximumSize(QSize(18, 18))
        self.btn_maxmize.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgba(85 ,255, 127, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_maxmize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(18, 18))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(18, 18))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"  border: none;\n"
"  border-radius: 8px;\n"
"  background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;\n"
"")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_menu = QFrame(self.content_bar)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(60, 0))
        self.frame_menu.setMaximumSize(QSize(60, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgb(27, 29, 34);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_menu)

        self.frame_page_content = QFrame(self.content_bar)
        self.frame_page_content.setObjectName(u"frame_page_content")
        self.frame_page_content.setFrameShape(QFrame.StyledPanel)
        self.frame_page_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_page_content)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_title_2 = QLabel(self.frame_page_content)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setMinimumSize(QSize(360, 50))
        self.label_title_2.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Noto Sans CJK KR Black")
        font1.setPointSize(30)
        self.label_title_2.setFont(font1)
        self.label_title_2.setStyleSheet(u"color: rgb(236, 240, 241);")
        self.label_title_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_title_2)

        self.frame = QFrame(self.frame_page_content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_4.addWidget(self.frame_page_content)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font2 = QFont()
        font2.setFamily(u"Noto Sans CJK KR Medium")
        font2.setPointSize(8)
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(129, 129, 129)")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_3.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 50px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Helio", None))
        self.btn_maxmize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"About Heliotrope", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"From Heliotrope", None))
    # retranslateUi

