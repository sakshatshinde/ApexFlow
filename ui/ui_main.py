# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkMGxDm.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLCDNumber, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1247, 800)
        icon = QIcon()
        icon.addFile(u"apexFlowIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon1 = QIcon()
        icon1.addFile(u"exit_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u"about_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.aiTab = QWidget()
        self.aiTab.setObjectName(u"aiTab")
        self.gridLayout_2 = QGridLayout(self.aiTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser = QTextBrowser(self.aiTab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.textEdit = QTextEdit(self.aiTab)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setTabChangesFocus(True)

        self.verticalLayout_5.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.send_msg_to_ai_btn = QPushButton(self.aiTab)
        self.send_msg_to_ai_btn.setObjectName(u"send_msg_to_ai_btn")

        self.horizontalLayout.addWidget(self.send_msg_to_ai_btn)

        self.clear_prompt_btn = QPushButton(self.aiTab)
        self.clear_prompt_btn.setObjectName(u"clear_prompt_btn")

        self.horizontalLayout.addWidget(self.clear_prompt_btn)

        self.attach_ai_btn = QPushButton(self.aiTab)
        self.attach_ai_btn.setObjectName(u"attach_ai_btn")
        self.attach_ai_btn.setEnabled(False)

        self.horizontalLayout.addWidget(self.attach_ai_btn)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 1, 0, 1, 1)

        self.tabWidget.addTab(self.aiTab, "")
        self.macro = QWidget()
        self.macro.setObjectName(u"macro")
        self.tabWidget.addTab(self.macro, "")
        self.financials = QWidget()
        self.financials.setObjectName(u"financials")
        self.tabWidget.addTab(self.financials, "")
        self.annualReports = QWidget()
        self.annualReports.setObjectName(u"annualReports")
        self.tabWidget.addTab(self.annualReports, "")
        self.sectoral = QWidget()
        self.sectoral.setObjectName(u"sectoral")
        self.tabWidget.addTab(self.sectoral, "")
        self.indices = QWidget()
        self.indices.setObjectName(u"indices")
        self.gridLayout_3 = QGridLayout(self.indices)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.majorIndicesHeader = QLabel(self.indices)
        self.majorIndicesHeader.setObjectName(u"majorIndicesHeader")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setWeight(QFont.DemiBold)
        self.majorIndicesHeader.setFont(font)
        self.majorIndicesHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.majorIndicesHeader)

        self.layout_MSCIWorld = QHBoxLayout()
        self.layout_MSCIWorld.setObjectName(u"layout_MSCIWorld")
        self.MSCIWorld_Label = QLabel(self.indices)
        self.MSCIWorld_Label.setObjectName(u"MSCIWorld_Label")
        self.MSCIWorld_Label.setMinimumSize(QSize(180, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.MSCIWorld_Label.setFont(font1)
        self.MSCIWorld_Label.setFrameShape(QFrame.Shape.Box)
        self.MSCIWorld_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_MSCIWorld.addWidget(self.MSCIWorld_Label)

        self.MSCIWorld_Percentage = QLabel(self.indices)
        self.MSCIWorld_Percentage.setObjectName(u"MSCIWorld_Percentage")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.MSCIWorld_Percentage.setFont(font2)

        self.layout_MSCIWorld.addWidget(self.MSCIWorld_Percentage)

        self.MSCIWorld = QLCDNumber(self.indices)
        self.MSCIWorld.setObjectName(u"MSCIWorld")
        self.MSCIWorld.setDigitCount(8)

        self.layout_MSCIWorld.addWidget(self.MSCIWorld)


        self.verticalLayout.addLayout(self.layout_MSCIWorld)

        self.layout_Nifty50 = QHBoxLayout()
        self.layout_Nifty50.setObjectName(u"layout_Nifty50")
        self.Nifty50_Label = QLabel(self.indices)
        self.Nifty50_Label.setObjectName(u"Nifty50_Label")
        self.Nifty50_Label.setMinimumSize(QSize(180, 0))
        self.Nifty50_Label.setFont(font1)
        self.Nifty50_Label.setFrameShape(QFrame.Shape.Box)
        self.Nifty50_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Nifty50.addWidget(self.Nifty50_Label)

        self.Nifty50_Percentage = QLabel(self.indices)
        self.Nifty50_Percentage.setObjectName(u"Nifty50_Percentage")
        self.Nifty50_Percentage.setFont(font2)

        self.layout_Nifty50.addWidget(self.Nifty50_Percentage)

        self.Nifty50 = QLCDNumber(self.indices)
        self.Nifty50.setObjectName(u"Nifty50")
        self.Nifty50.setDigitCount(8)

        self.layout_Nifty50.addWidget(self.Nifty50)


        self.verticalLayout.addLayout(self.layout_Nifty50)

        self.layout_Nasdaq100 = QHBoxLayout()
        self.layout_Nasdaq100.setObjectName(u"layout_Nasdaq100")
        self.Nasdaq100_Label = QLabel(self.indices)
        self.Nasdaq100_Label.setObjectName(u"Nasdaq100_Label")
        self.Nasdaq100_Label.setMinimumSize(QSize(180, 0))
        self.Nasdaq100_Label.setFont(font1)
        self.Nasdaq100_Label.setFrameShape(QFrame.Shape.Box)
        self.Nasdaq100_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Nasdaq100.addWidget(self.Nasdaq100_Label)

        self.Nasdaq100_Percentage = QLabel(self.indices)
        self.Nasdaq100_Percentage.setObjectName(u"Nasdaq100_Percentage")
        self.Nasdaq100_Percentage.setFont(font2)

        self.layout_Nasdaq100.addWidget(self.Nasdaq100_Percentage)

        self.Nasdaq100 = QLCDNumber(self.indices)
        self.Nasdaq100.setObjectName(u"Nasdaq100")
        self.Nasdaq100.setDigitCount(8)

        self.layout_Nasdaq100.addWidget(self.Nasdaq100)


        self.verticalLayout.addLayout(self.layout_Nasdaq100)

        self.layout_SP500 = QHBoxLayout()
        self.layout_SP500.setObjectName(u"layout_SP500")
        self.SP500_Label = QLabel(self.indices)
        self.SP500_Label.setObjectName(u"SP500_Label")
        self.SP500_Label.setMinimumSize(QSize(180, 0))
        self.SP500_Label.setFont(font1)
        self.SP500_Label.setFrameShape(QFrame.Shape.Box)
        self.SP500_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_SP500.addWidget(self.SP500_Label)

        self.SP500_Percentage = QLabel(self.indices)
        self.SP500_Percentage.setObjectName(u"SP500_Percentage")
        self.SP500_Percentage.setFont(font2)

        self.layout_SP500.addWidget(self.SP500_Percentage)

        self.SP500 = QLCDNumber(self.indices)
        self.SP500.setObjectName(u"SP500")
        self.SP500.setDigitCount(8)

        self.layout_SP500.addWidget(self.SP500)


        self.verticalLayout.addLayout(self.layout_SP500)

        self.layout_Nikkei225 = QHBoxLayout()
        self.layout_Nikkei225.setObjectName(u"layout_Nikkei225")
        self.Nikkei225_Label = QLabel(self.indices)
        self.Nikkei225_Label.setObjectName(u"Nikkei225_Label")
        self.Nikkei225_Label.setMinimumSize(QSize(180, 0))
        self.Nikkei225_Label.setFont(font1)
        self.Nikkei225_Label.setFrameShape(QFrame.Shape.Box)
        self.Nikkei225_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Nikkei225.addWidget(self.Nikkei225_Label)

        self.SP500_Percentage1 = QLabel(self.indices)
        self.SP500_Percentage1.setObjectName(u"SP500_Percentage1")
        self.SP500_Percentage1.setFont(font2)

        self.layout_Nikkei225.addWidget(self.SP500_Percentage1)

        self.Nikkei225 = QLCDNumber(self.indices)
        self.Nikkei225.setObjectName(u"Nikkei225")
        self.Nikkei225.setDigitCount(8)

        self.layout_Nikkei225.addWidget(self.Nikkei225)


        self.verticalLayout.addLayout(self.layout_Nikkei225)

        self.layout_Hangseng = QHBoxLayout()
        self.layout_Hangseng.setObjectName(u"layout_Hangseng")
        self.Hangseng_Label = QLabel(self.indices)
        self.Hangseng_Label.setObjectName(u"Hangseng_Label")
        self.Hangseng_Label.setMinimumSize(QSize(180, 0))
        self.Hangseng_Label.setFont(font1)
        self.Hangseng_Label.setFrameShape(QFrame.Shape.Box)
        self.Hangseng_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Hangseng.addWidget(self.Hangseng_Label)

        self.Hangseng_Percentage = QLabel(self.indices)
        self.Hangseng_Percentage.setObjectName(u"Hangseng_Percentage")
        self.Hangseng_Percentage.setFont(font2)

        self.layout_Hangseng.addWidget(self.Hangseng_Percentage)

        self.Hangseng = QLCDNumber(self.indices)
        self.Hangseng.setObjectName(u"Hangseng")
        self.Hangseng.setDigitCount(8)

        self.layout_Hangseng.addWidget(self.Hangseng)


        self.verticalLayout.addLayout(self.layout_Hangseng)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.commoditiesHeader = QLabel(self.indices)
        self.commoditiesHeader.setObjectName(u"commoditiesHeader")
        self.commoditiesHeader.setFont(font)
        self.commoditiesHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.commoditiesHeader)

        self.layout_Gold = QHBoxLayout()
        self.layout_Gold.setObjectName(u"layout_Gold")
        self.Gold_Label = QLabel(self.indices)
        self.Gold_Label.setObjectName(u"Gold_Label")
        self.Gold_Label.setMinimumSize(QSize(180, 0))
        self.Gold_Label.setFont(font1)
        self.Gold_Label.setFrameShape(QFrame.Shape.Box)
        self.Gold_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Gold.addWidget(self.Gold_Label)

        self.Gold_Percentage = QLabel(self.indices)
        self.Gold_Percentage.setObjectName(u"Gold_Percentage")
        self.Gold_Percentage.setFont(font2)

        self.layout_Gold.addWidget(self.Gold_Percentage)

        self.Gold = QLCDNumber(self.indices)
        self.Gold.setObjectName(u"Gold")
        self.Gold.setDigitCount(8)

        self.layout_Gold.addWidget(self.Gold)


        self.verticalLayout_2.addLayout(self.layout_Gold)

        self.layout_Silver = QHBoxLayout()
        self.layout_Silver.setObjectName(u"layout_Silver")
        self.Silver_Label = QLabel(self.indices)
        self.Silver_Label.setObjectName(u"Silver_Label")
        self.Silver_Label.setMinimumSize(QSize(180, 0))
        self.Silver_Label.setFont(font1)
        self.Silver_Label.setFrameShape(QFrame.Shape.Box)
        self.Silver_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_Silver.addWidget(self.Silver_Label)

        self.Silver_Percentage = QLabel(self.indices)
        self.Silver_Percentage.setObjectName(u"Silver_Percentage")
        self.Silver_Percentage.setFont(font2)

        self.layout_Silver.addWidget(self.Silver_Percentage)

        self.Silver = QLCDNumber(self.indices)
        self.Silver.setObjectName(u"Silver")
        self.Silver.setDigitCount(8)

        self.layout_Silver.addWidget(self.Silver)


        self.verticalLayout_2.addLayout(self.layout_Silver)

        self.layout_BrentCrudeOil = QHBoxLayout()
        self.layout_BrentCrudeOil.setObjectName(u"layout_BrentCrudeOil")
        self.BrentCrudeOil_Label = QLabel(self.indices)
        self.BrentCrudeOil_Label.setObjectName(u"BrentCrudeOil_Label")
        self.BrentCrudeOil_Label.setMinimumSize(QSize(180, 0))
        self.BrentCrudeOil_Label.setFont(font1)
        self.BrentCrudeOil_Label.setFrameShape(QFrame.Shape.Box)
        self.BrentCrudeOil_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_BrentCrudeOil.addWidget(self.BrentCrudeOil_Label)

        self.BrentCrudeOil_Percentage = QLabel(self.indices)
        self.BrentCrudeOil_Percentage.setObjectName(u"BrentCrudeOil_Percentage")
        self.BrentCrudeOil_Percentage.setFont(font2)

        self.layout_BrentCrudeOil.addWidget(self.BrentCrudeOil_Percentage)

        self.BrentCrudeOil = QLCDNumber(self.indices)
        self.BrentCrudeOil.setObjectName(u"BrentCrudeOil")
        self.BrentCrudeOil.setDigitCount(8)

        self.layout_BrentCrudeOil.addWidget(self.BrentCrudeOil)


        self.verticalLayout_2.addLayout(self.layout_BrentCrudeOil)

        self.layout_NaturalGas = QHBoxLayout()
        self.layout_NaturalGas.setObjectName(u"layout_NaturalGas")
        self.NaturalGas_Label = QLabel(self.indices)
        self.NaturalGas_Label.setObjectName(u"NaturalGas_Label")
        self.NaturalGas_Label.setMinimumSize(QSize(180, 0))
        self.NaturalGas_Label.setFont(font1)
        self.NaturalGas_Label.setFrameShape(QFrame.Shape.Box)
        self.NaturalGas_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NaturalGas.addWidget(self.NaturalGas_Label)

        self.NaturalGas_Percentage = QLabel(self.indices)
        self.NaturalGas_Percentage.setObjectName(u"NaturalGas_Percentage")
        self.NaturalGas_Percentage.setFont(font2)

        self.layout_NaturalGas.addWidget(self.NaturalGas_Percentage)

        self.NaturalGas = QLCDNumber(self.indices)
        self.NaturalGas.setObjectName(u"NaturalGas")
        self.NaturalGas.setDigitCount(8)

        self.layout_NaturalGas.addWidget(self.NaturalGas)


        self.verticalLayout_2.addLayout(self.layout_NaturalGas)

        self.layout_USDINR = QHBoxLayout()
        self.layout_USDINR.setObjectName(u"layout_USDINR")
        self.USDINR_Label = QLabel(self.indices)
        self.USDINR_Label.setObjectName(u"USDINR_Label")
        self.USDINR_Label.setMinimumSize(QSize(180, 0))
        self.USDINR_Label.setFont(font1)
        self.USDINR_Label.setFrameShape(QFrame.Shape.Box)
        self.USDINR_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_USDINR.addWidget(self.USDINR_Label)

        self.USDINR_Percentage = QLabel(self.indices)
        self.USDINR_Percentage.setObjectName(u"USDINR_Percentage")
        self.USDINR_Percentage.setFont(font2)

        self.layout_USDINR.addWidget(self.USDINR_Percentage)

        self.USDINR = QLCDNumber(self.indices)
        self.USDINR.setObjectName(u"USDINR")
        self.USDINR.setDigitCount(8)

        self.layout_USDINR.addWidget(self.USDINR)


        self.verticalLayout_2.addLayout(self.layout_USDINR)

        self.layout_USVix = QHBoxLayout()
        self.layout_USVix.setObjectName(u"layout_USVix")
        self.USVix_Label = QLabel(self.indices)
        self.USVix_Label.setObjectName(u"USVix_Label")
        self.USVix_Label.setMinimumSize(QSize(180, 0))
        self.USVix_Label.setFont(font1)
        self.USVix_Label.setFrameShape(QFrame.Shape.Box)
        self.USVix_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_USVix.addWidget(self.USVix_Label)

        self.USVix_Percentage = QLabel(self.indices)
        self.USVix_Percentage.setObjectName(u"USVix_Percentage")
        self.USVix_Percentage.setFont(font2)

        self.layout_USVix.addWidget(self.USVix_Percentage)

        self.USVix = QLCDNumber(self.indices)
        self.USVix.setObjectName(u"USVix")
        self.USVix.setDigitCount(8)

        self.layout_USVix.addWidget(self.USVix)


        self.verticalLayout_2.addLayout(self.layout_USVix)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.indianIndicesHeader = QLabel(self.indices)
        self.indianIndicesHeader.setObjectName(u"indianIndicesHeader")
        self.indianIndicesHeader.setFont(font)
        self.indianIndicesHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.indianIndicesHeader)

        self.layout_IndiaRepoRate = QHBoxLayout()
        self.layout_IndiaRepoRate.setObjectName(u"layout_IndiaRepoRate")
        self.IndiaRepoRate_Label = QLabel(self.indices)
        self.IndiaRepoRate_Label.setObjectName(u"IndiaRepoRate_Label")
        self.IndiaRepoRate_Label.setMinimumSize(QSize(180, 0))
        self.IndiaRepoRate_Label.setFont(font1)
        self.IndiaRepoRate_Label.setFrameShape(QFrame.Shape.Box)
        self.IndiaRepoRate_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_IndiaRepoRate.addWidget(self.IndiaRepoRate_Label)

        self.IndiaRepoRate_Percentage = QLabel(self.indices)
        self.IndiaRepoRate_Percentage.setObjectName(u"IndiaRepoRate_Percentage")
        self.IndiaRepoRate_Percentage.setFont(font2)

        self.layout_IndiaRepoRate.addWidget(self.IndiaRepoRate_Percentage)

        self.IndiaRepoRate = QLCDNumber(self.indices)
        self.IndiaRepoRate.setObjectName(u"IndiaRepoRate")
        self.IndiaRepoRate.setDigitCount(8)

        self.layout_IndiaRepoRate.addWidget(self.IndiaRepoRate)


        self.verticalLayout_3.addLayout(self.layout_IndiaRepoRate)

        self.layout_IndiaVix = QHBoxLayout()
        self.layout_IndiaVix.setObjectName(u"layout_IndiaVix")
        self.IndiaVix_Label = QLabel(self.indices)
        self.IndiaVix_Label.setObjectName(u"IndiaVix_Label")
        self.IndiaVix_Label.setMinimumSize(QSize(180, 0))
        self.IndiaVix_Label.setFont(font1)
        self.IndiaVix_Label.setFrameShape(QFrame.Shape.Box)
        self.IndiaVix_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_IndiaVix.addWidget(self.IndiaVix_Label)

        self.IndiaVix_Percentage = QLabel(self.indices)
        self.IndiaVix_Percentage.setObjectName(u"IndiaVix_Percentage")
        self.IndiaVix_Percentage.setFont(font2)

        self.layout_IndiaVix.addWidget(self.IndiaVix_Percentage)

        self.IndiaVix = QLCDNumber(self.indices)
        self.IndiaVix.setObjectName(u"IndiaVix")
        self.IndiaVix.setDigitCount(8)

        self.layout_IndiaVix.addWidget(self.IndiaVix)


        self.verticalLayout_3.addLayout(self.layout_IndiaVix)

        self.layout_NiftyIT = QHBoxLayout()
        self.layout_NiftyIT.setObjectName(u"layout_NiftyIT")
        self.NiftyIT_Label = QLabel(self.indices)
        self.NiftyIT_Label.setObjectName(u"NiftyIT_Label")
        self.NiftyIT_Label.setMinimumSize(QSize(180, 0))
        self.NiftyIT_Label.setFont(font1)
        self.NiftyIT_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyIT_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyIT.addWidget(self.NiftyIT_Label)

        self.NiftyIT_Percentage = QLabel(self.indices)
        self.NiftyIT_Percentage.setObjectName(u"NiftyIT_Percentage")
        self.NiftyIT_Percentage.setFont(font2)

        self.layout_NiftyIT.addWidget(self.NiftyIT_Percentage)

        self.NiftyIT = QLCDNumber(self.indices)
        self.NiftyIT.setObjectName(u"NiftyIT")
        self.NiftyIT.setDigitCount(8)

        self.layout_NiftyIT.addWidget(self.NiftyIT)


        self.verticalLayout_3.addLayout(self.layout_NiftyIT)

        self.layout_NiftyBank = QHBoxLayout()
        self.layout_NiftyBank.setObjectName(u"layout_NiftyBank")
        self.NiftyBank_Label = QLabel(self.indices)
        self.NiftyBank_Label.setObjectName(u"NiftyBank_Label")
        self.NiftyBank_Label.setMinimumSize(QSize(180, 0))
        self.NiftyBank_Label.setFont(font1)
        self.NiftyBank_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyBank_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyBank.addWidget(self.NiftyBank_Label)

        self.NiftyBank_Percentage = QLabel(self.indices)
        self.NiftyBank_Percentage.setObjectName(u"NiftyBank_Percentage")
        self.NiftyBank_Percentage.setFont(font2)

        self.layout_NiftyBank.addWidget(self.NiftyBank_Percentage)

        self.NiftyBank = QLCDNumber(self.indices)
        self.NiftyBank.setObjectName(u"NiftyBank")
        self.NiftyBank.setDigitCount(8)

        self.layout_NiftyBank.addWidget(self.NiftyBank)


        self.verticalLayout_3.addLayout(self.layout_NiftyBank)

        self.layout_NiftyFMCG = QHBoxLayout()
        self.layout_NiftyFMCG.setObjectName(u"layout_NiftyFMCG")
        self.NiftyFMCG_Label = QLabel(self.indices)
        self.NiftyFMCG_Label.setObjectName(u"NiftyFMCG_Label")
        self.NiftyFMCG_Label.setMinimumSize(QSize(180, 0))
        self.NiftyFMCG_Label.setFont(font1)
        self.NiftyFMCG_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyFMCG_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyFMCG.addWidget(self.NiftyFMCG_Label)

        self.NiftyFMCG_Percentage = QLabel(self.indices)
        self.NiftyFMCG_Percentage.setObjectName(u"NiftyFMCG_Percentage")
        self.NiftyFMCG_Percentage.setFont(font2)

        self.layout_NiftyFMCG.addWidget(self.NiftyFMCG_Percentage)

        self.NiftyFMCG = QLCDNumber(self.indices)
        self.NiftyFMCG.setObjectName(u"NiftyFMCG")
        self.NiftyFMCG.setDigitCount(8)

        self.layout_NiftyFMCG.addWidget(self.NiftyFMCG)


        self.verticalLayout_3.addLayout(self.layout_NiftyFMCG)

        self.layout_NiftyIndiaDefence = QHBoxLayout()
        self.layout_NiftyIndiaDefence.setObjectName(u"layout_NiftyIndiaDefence")
        self.NiftyIndiaDefence_Label = QLabel(self.indices)
        self.NiftyIndiaDefence_Label.setObjectName(u"NiftyIndiaDefence_Label")
        self.NiftyIndiaDefence_Label.setMinimumSize(QSize(180, 0))
        self.NiftyIndiaDefence_Label.setFont(font1)
        self.NiftyIndiaDefence_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyIndiaDefence_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyIndiaDefence.addWidget(self.NiftyIndiaDefence_Label)

        self.NiftyIndiaDefence_Percentage = QLabel(self.indices)
        self.NiftyIndiaDefence_Percentage.setObjectName(u"NiftyIndiaDefence_Percentage")
        self.NiftyIndiaDefence_Percentage.setFont(font2)

        self.layout_NiftyIndiaDefence.addWidget(self.NiftyIndiaDefence_Percentage)

        self.NiftyIndiaDefence = QLCDNumber(self.indices)
        self.NiftyIndiaDefence.setObjectName(u"NiftyIndiaDefence")
        self.NiftyIndiaDefence.setDigitCount(8)

        self.layout_NiftyIndiaDefence.addWidget(self.NiftyIndiaDefence)


        self.verticalLayout_3.addLayout(self.layout_NiftyIndiaDefence)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.moreIndicesHeader = QLabel(self.indices)
        self.moreIndicesHeader.setObjectName(u"moreIndicesHeader")
        self.moreIndicesHeader.setFont(font)
        self.moreIndicesHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.moreIndicesHeader)

        self.layout_NiftyMidcap150 = QHBoxLayout()
        self.layout_NiftyMidcap150.setObjectName(u"layout_NiftyMidcap150")
        self.NiftyMidcap150_Label = QLabel(self.indices)
        self.NiftyMidcap150_Label.setObjectName(u"NiftyMidcap150_Label")
        self.NiftyMidcap150_Label.setMinimumSize(QSize(180, 0))
        self.NiftyMidcap150_Label.setFont(font1)
        self.NiftyMidcap150_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyMidcap150_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyMidcap150.addWidget(self.NiftyMidcap150_Label)

        self.NiftyMidcap150_Percentage = QLabel(self.indices)
        self.NiftyMidcap150_Percentage.setObjectName(u"NiftyMidcap150_Percentage")
        self.NiftyMidcap150_Percentage.setFont(font2)

        self.layout_NiftyMidcap150.addWidget(self.NiftyMidcap150_Percentage)

        self.NiftyMidcap150 = QLCDNumber(self.indices)
        self.NiftyMidcap150.setObjectName(u"NiftyMidcap150")
        self.NiftyMidcap150.setDigitCount(8)

        self.layout_NiftyMidcap150.addWidget(self.NiftyMidcap150)


        self.verticalLayout_4.addLayout(self.layout_NiftyMidcap150)

        self.layout_NiftySmallCap250 = QHBoxLayout()
        self.layout_NiftySmallCap250.setObjectName(u"layout_NiftySmallCap250")
        self.NiftySmallCap250_Label = QLabel(self.indices)
        self.NiftySmallCap250_Label.setObjectName(u"NiftySmallCap250_Label")
        self.NiftySmallCap250_Label.setMinimumSize(QSize(180, 0))
        self.NiftySmallCap250_Label.setFont(font1)
        self.NiftySmallCap250_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftySmallCap250_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftySmallCap250.addWidget(self.NiftySmallCap250_Label)

        self.NiftySmallCap250_Percentage = QLabel(self.indices)
        self.NiftySmallCap250_Percentage.setObjectName(u"NiftySmallCap250_Percentage")
        self.NiftySmallCap250_Percentage.setFont(font2)

        self.layout_NiftySmallCap250.addWidget(self.NiftySmallCap250_Percentage)

        self.NiftySmallCap250 = QLCDNumber(self.indices)
        self.NiftySmallCap250.setObjectName(u"NiftySmallCap250")
        self.NiftySmallCap250.setDigitCount(8)

        self.layout_NiftySmallCap250.addWidget(self.NiftySmallCap250)


        self.verticalLayout_4.addLayout(self.layout_NiftySmallCap250)

        self.layout_NiftyAuto = QHBoxLayout()
        self.layout_NiftyAuto.setObjectName(u"layout_NiftyAuto")
        self.NiftyAuto_Label = QLabel(self.indices)
        self.NiftyAuto_Label.setObjectName(u"NiftyAuto_Label")
        self.NiftyAuto_Label.setMinimumSize(QSize(180, 0))
        self.NiftyAuto_Label.setFont(font1)
        self.NiftyAuto_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyAuto_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyAuto.addWidget(self.NiftyAuto_Label)

        self.NiftyAuto_Percentage = QLabel(self.indices)
        self.NiftyAuto_Percentage.setObjectName(u"NiftyAuto_Percentage")
        self.NiftyAuto_Percentage.setFont(font2)

        self.layout_NiftyAuto.addWidget(self.NiftyAuto_Percentage)

        self.NiftyAuto = QLCDNumber(self.indices)
        self.NiftyAuto.setObjectName(u"NiftyAuto")
        self.NiftyAuto.setDigitCount(8)

        self.layout_NiftyAuto.addWidget(self.NiftyAuto)


        self.verticalLayout_4.addLayout(self.layout_NiftyAuto)

        self.layout_NiftyPharma = QHBoxLayout()
        self.layout_NiftyPharma.setObjectName(u"layout_NiftyPharma")
        self.NiftyPharma_Label = QLabel(self.indices)
        self.NiftyPharma_Label.setObjectName(u"NiftyPharma_Label")
        self.NiftyPharma_Label.setMinimumSize(QSize(180, 0))
        self.NiftyPharma_Label.setFont(font1)
        self.NiftyPharma_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyPharma_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyPharma.addWidget(self.NiftyPharma_Label)

        self.NiftyPharma_Percentage = QLabel(self.indices)
        self.NiftyPharma_Percentage.setObjectName(u"NiftyPharma_Percentage")
        self.NiftyPharma_Percentage.setFont(font2)

        self.layout_NiftyPharma.addWidget(self.NiftyPharma_Percentage)

        self.NiftyPharma = QLCDNumber(self.indices)
        self.NiftyPharma.setObjectName(u"NiftyPharma")
        self.NiftyPharma.setDigitCount(8)

        self.layout_NiftyPharma.addWidget(self.NiftyPharma)


        self.verticalLayout_4.addLayout(self.layout_NiftyPharma)

        self.layout_NIftyOilGas = QHBoxLayout()
        self.layout_NIftyOilGas.setObjectName(u"layout_NIftyOilGas")
        self.NIftyOilGas_Label = QLabel(self.indices)
        self.NIftyOilGas_Label.setObjectName(u"NIftyOilGas_Label")
        self.NIftyOilGas_Label.setMinimumSize(QSize(180, 0))
        self.NIftyOilGas_Label.setFont(font1)
        self.NIftyOilGas_Label.setFrameShape(QFrame.Shape.Box)
        self.NIftyOilGas_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NIftyOilGas.addWidget(self.NIftyOilGas_Label)

        self.NIftyOilGas_Percentage = QLabel(self.indices)
        self.NIftyOilGas_Percentage.setObjectName(u"NIftyOilGas_Percentage")
        self.NIftyOilGas_Percentage.setFont(font2)

        self.layout_NIftyOilGas.addWidget(self.NIftyOilGas_Percentage)

        self.NIftyOilGas = QLCDNumber(self.indices)
        self.NIftyOilGas.setObjectName(u"NIftyOilGas")
        self.NIftyOilGas.setDigitCount(8)

        self.layout_NIftyOilGas.addWidget(self.NIftyOilGas)


        self.verticalLayout_4.addLayout(self.layout_NIftyOilGas)

        self.layout_NiftyEnergy = QHBoxLayout()
        self.layout_NiftyEnergy.setObjectName(u"layout_NiftyEnergy")
        self.NiftyEnergy_Label = QLabel(self.indices)
        self.NiftyEnergy_Label.setObjectName(u"NiftyEnergy_Label")
        self.NiftyEnergy_Label.setMinimumSize(QSize(180, 0))
        self.NiftyEnergy_Label.setFont(font1)
        self.NiftyEnergy_Label.setFrameShape(QFrame.Shape.Box)
        self.NiftyEnergy_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_NiftyEnergy.addWidget(self.NiftyEnergy_Label)

        self.NiftyEnergy_Percentage = QLabel(self.indices)
        self.NiftyEnergy_Percentage.setObjectName(u"NiftyEnergy_Percentage")
        self.NiftyEnergy_Percentage.setFont(font2)

        self.layout_NiftyEnergy.addWidget(self.NiftyEnergy_Percentage)

        self.NiftyEnergy = QLCDNumber(self.indices)
        self.NiftyEnergy.setObjectName(u"NiftyEnergy")
        self.NiftyEnergy.setDigitCount(8)

        self.layout_NiftyEnergy.addWidget(self.NiftyEnergy)


        self.verticalLayout_4.addLayout(self.layout_NiftyEnergy)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 1, 0, 1, 1)

        self.NiftyHeatmapWebView = QWebEngineView(self.indices)
        self.NiftyHeatmapWebView.setObjectName(u"NiftyHeatmapWebView")
        self.NiftyHeatmapWebView.setUrl(QUrl(u"about:blank"))

        self.gridLayout_3.addWidget(self.NiftyHeatmapWebView, 1, 1, 1, 2)

        self.tabWidget.addTab(self.indices, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1247, 29))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ApexFlow - Financial Analytics", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"      /* Base colors and variables */\n"
"QMainWindow {\n"
"    background-color: #111827;\n"
"    color: #F9FAFB;\n"
"}\n"
"\n"
"/* Tab styling */\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    background-color: #111827;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #1F2937;\n"
"    color: #F9FAFB;\n"
"    padding: 8px 16px;\n"
"    margin-right: 2px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #374151;\n"
"    border-bottom: 2px solid #10B981;\n"
"}\n"
"\n"
"QTabBar::tab:hover:!selected {\n"
"    background-color: #2D3748;\n"
"}\n"
"\n"
"/* LCD styling */\n"
"QLCDNumber {\n"
"    background-color: #1F2937;\n"
"    color: #10B981;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Label styling */\n"
"QLabel {\n"
"    background-color: transparent;\n"
"    color: #F9FAFB;\n"
"    padding: 6px;\n"
"    font-weight: 400;\n"
"}"
                        "\n"
"\n"
"/* Header labels */\n"
"QLabel[objectName*=\"Header\"] {\n"
"    background-color: #374151;\n"
"    color: white;\n"
"    padding: 8px;\n"
"    border-radius: 4px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Button styling - Fixed contrast issues */\n"
"QPushButton {\n"
"    background-color: #3B82F6;\n"
"    color: #FFFFFF;\n"
"    border-radius: 4px;\n"
"    padding: 10px 14px;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"    letter-spacing: 0.5px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2563EB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1D4ED8;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #374151;\n"
"    color: #9CA3AF;\n"
"}\n"
"\n"
"/* Text components */\n"
"QTextEdit, QTextBrowser {\n"
"    background-color: #1F2937;\n"
"    color: #F9FAFB;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 6px;\n"
"    selection-background-color: #4F46E5;\n"
"}\n"
"\n"
"/* Menu styling */\n"
"QMenuBar"
                        " {\n"
"    background-color: #1F2937;\n"
"    color: #F9FAFB;\n"
"    border-bottom: 1px solid #374151;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 6px 8px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #374151;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #1F2937;\n"
"    color: #F9FAFB;\n"
"    border: 1px solid #111827;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 16px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #374151;\n"
"}\n"
"\n"
"/* Scrollbar styling */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #1F2937;\n"
"    width: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #4F46E5;\n"
"    min-height: 24px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar:h"
                        "orizontal {\n"
"    border: none;\n"
"    background: #1F2937;\n"
"    height: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #4F46E5;\n"
"    min-width: 24px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"/* Triangle indicators */\n"
"QLabel[class=\"up-triangle\"] {\n"
"    color: #10B981; /* Green color for up movement */\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QLabel[class=\"down-triangle\"] {\n"
"    color: #EF4444; /* Red color for down movement */\n"
"    font-family: Arial;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"            ", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textBrowser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"AI assistant will reply here... Please note this is not a chat, no history of your messages will be kept in the context.", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your prompt here...", None))
        self.send_msg_to_ai_btn.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.clear_prompt_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.attach_ai_btn.setText(QCoreApplication.translate("MainWindow", u"Attach", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aiTab), QCoreApplication.translate("MainWindow", u"Ask AI", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.aiTab), QCoreApplication.translate("MainWindow", u"Here you can send a message to Gemini and ask for it's input", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.macro), QCoreApplication.translate("MainWindow", u"Macro", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.financials), QCoreApplication.translate("MainWindow", u"Financials", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.annualReports), QCoreApplication.translate("MainWindow", u"Annual Reports", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sectoral), QCoreApplication.translate("MainWindow", u"Sectoral", None))
        self.majorIndicesHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: white; padding: 8px; border-radius: 4px;", None))
        self.majorIndicesHeader.setText(QCoreApplication.translate("MainWindow", u"MAJOR INDICES", None))
        self.MSCIWorld_Label.setText(QCoreApplication.translate("MainWindow", u"MSCI World", None))
        self.MSCIWorld_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.Nifty50_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty 50", None))
        self.Nifty50_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.Nasdaq100_Label.setText(QCoreApplication.translate("MainWindow", u"Nasdaq 100", None))
        self.Nasdaq100_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.SP500_Label.setText(QCoreApplication.translate("MainWindow", u"S&P 500", None))
        self.SP500_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.Nikkei225_Label.setText(QCoreApplication.translate("MainWindow", u"Nikkei 225", None))
        self.SP500_Percentage1.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.Hangseng_Label.setText(QCoreApplication.translate("MainWindow", u"Hang Seng", None))
        self.Hangseng_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.commoditiesHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: white; padding: 8px; border-radius: 4px;", None))
        self.commoditiesHeader.setText(QCoreApplication.translate("MainWindow", u"COMMODITIES & FOREX", None))
        self.Gold_Label.setText(QCoreApplication.translate("MainWindow", u"Gold", None))
        self.Gold_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.Silver_Label.setText(QCoreApplication.translate("MainWindow", u"Silver", None))
        self.Silver_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.BrentCrudeOil_Label.setText(QCoreApplication.translate("MainWindow", u"Brent Crude Oil", None))
        self.BrentCrudeOil_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NaturalGas_Label.setText(QCoreApplication.translate("MainWindow", u"Natural Gas", None))
        self.NaturalGas_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.USDINR_Label.setText(QCoreApplication.translate("MainWindow", u"USD INR", None))
        self.USDINR_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.USVix_Label.setText(QCoreApplication.translate("MainWindow", u"US VIX", None))
        self.USVix_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.indianIndicesHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: white; padding: 8px; border-radius: 4px;", None))
        self.indianIndicesHeader.setText(QCoreApplication.translate("MainWindow", u"INDIAN RATES & INDICES", None))
        self.IndiaRepoRate_Label.setText(QCoreApplication.translate("MainWindow", u"India Repo Rate", None))
        self.IndiaRepoRate_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.IndiaVix_Label.setText(QCoreApplication.translate("MainWindow", u"India VIX", None))
        self.IndiaVix_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyIT_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty IT", None))
        self.NiftyIT_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyBank_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Bank", None))
        self.NiftyBank_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyFMCG_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty FMCG", None))
        self.NiftyFMCG_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyIndiaDefence_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty India Defence", None))
        self.NiftyIndiaDefence_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.moreIndicesHeader.setStyleSheet(QCoreApplication.translate("MainWindow", u"color: white; padding: 8px; border-radius: 4px;", None))
        self.moreIndicesHeader.setText(QCoreApplication.translate("MainWindow", u"MORE INDIAN INDICES", None))
        self.NiftyMidcap150_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Midcap 150", None))
        self.NiftyMidcap150_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftySmallCap250_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Smallcap 250", None))
        self.NiftySmallCap250_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyAuto_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Auto", None))
        self.NiftyAuto_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyPharma_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Pharma", None))
        self.NiftyPharma_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NIftyOilGas_Label.setText(QCoreApplication.translate("MainWindow", u"Nifty Oil and Gas", None))
        self.NIftyOilGas_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.NiftyEnergy_Label.setText(QCoreApplication.translate("MainWindow", u"NIFTY ENERGY", None))
        self.NiftyEnergy_Percentage.setText(QCoreApplication.translate("MainWindow", u"+0.00%", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.indices), QCoreApplication.translate("MainWindow", u"Indices", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.indices), QCoreApplication.translate("MainWindow", u"Indices all over the world", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

