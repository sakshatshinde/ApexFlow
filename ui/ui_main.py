# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainiRHTAA.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTabWidget, QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1180, 708)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1181, 681))
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setMovable(True)
        self.aiChat = QWidget()
        self.aiChat.setObjectName(u"aiChat")
        self.aiChat.setMinimumSize(QSize(1175, 0))
        self.gridLayoutWidget = QWidget(self.aiChat)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 1161, 631))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(50, 55))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 135))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.pushButton.setPalette(palette)
        font = QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setFlat(True)

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse|Qt.TextInteractionFlag.TextBrowserInteraction|Qt.TextInteractionFlag.TextSelectableByKeyboard|Qt.TextInteractionFlag.TextSelectableByMouse)
        self.textBrowser.setOpenExternalLinks(True)

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 60))
        self.textEdit.setTabChangesFocus(True)

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.aiChat, "")
        self.financials = QWidget()
        self.financials.setObjectName(u"financials")
        sizePolicy.setHeightForWidth(self.financials.sizePolicy().hasHeightForWidth())
        self.financials.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.financials, "")
        self.annualReports = QWidget()
        self.annualReports.setObjectName(u"annualReports")
        sizePolicy.setHeightForWidth(self.annualReports.sizePolicy().hasHeightForWidth())
        self.annualReports.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.annualReports, "")
        self.macro = QWidget()
        self.macro.setObjectName(u"macro")
        sizePolicy.setHeightForWidth(self.macro.sizePolicy().hasHeightForWidth())
        self.macro.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.macro, "")
        self.sectoral = QWidget()
        self.sectoral.setObjectName(u"sectoral")
        sizePolicy.setHeightForWidth(self.sectoral.sizePolicy().hasHeightForWidth())
        self.sectoral.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.sectoral, "")
        self.indices = QWidget()
        self.indices.setObjectName(u"indices")
        sizePolicy.setHeightForWidth(self.indices.sizePolicy().hasHeightForWidth())
        self.indices.setSizePolicy(sizePolicy)
        self.tabWidget.addTab(self.indices, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1180, 33))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ApexFlow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AI assitant will reply soon ... Please note this is not a chat, no history of your messages will be kept in the context.", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your prompt here ...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aiChat), QCoreApplication.translate("MainWindow", u"AI Chat", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.financials), QCoreApplication.translate("MainWindow", u"Financials", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.annualReports), QCoreApplication.translate("MainWindow", u"Annual Reports", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.macro), QCoreApplication.translate("MainWindow", u"Macro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sectoral), QCoreApplication.translate("MainWindow", u"Sectoral", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indices), QCoreApplication.translate("MainWindow", u"Indices", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

