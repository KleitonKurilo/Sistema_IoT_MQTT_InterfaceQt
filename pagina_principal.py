# -*- coding: utf-8 -*-
import datetime
import sqlite3
import subprocess


################################################################################
## Form generated from reading UI file 'Designer_24_05_23WtMzUf.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QMetaObject, QRect,
                            QSize, Qt, QTimer, QElapsedTimer,QThread)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QCalendarWidget, QCheckBox, QFrame, QMessageBox,
                               QGroupBox, QLCDNumber, QLabel, QMenuBar, QPushButton, QSpinBox,
                               QStatusBar, QTabWidget, QTimeEdit, QWidget)

from mqtt import MQTTSubscriber



import threading

from relatorio import gerar_relatorio_manual






class Ui_MainWindow(object):


        #Endereço Broker

    broker = "192.168.0.100"

    subscriber_servidor = MQTTSubscriber(broker, "serv")
    tempo_servidor_offiline = 0

        # Linha 1
    subscriber_mesa_1 = MQTTSubscriber(broker, "Mesa1")
    subscriber_est_1_ap = MQTTSubscriber(broker, "EstA1")
    subscriber_est_1_rep = MQTTSubscriber(broker, "EstR1")
    subscriber_pre_1_ap = MQTTSubscriber(broker, "PreA1")
    subscriber_pre_1_rep = MQTTSubscriber(broker, "PreR1")
    subscriber_hy_1_ap = MQTTSubscriber(broker, "HyA1")
    subscriber_hy_1_rep = MQTTSubscriber(broker, "HyP1")
    subscriber_op_L1 = MQTTSubscriber(broker, "op_L1")

    Mesa_de_Montagem_L1 = 0
    Estanquiedade_Aprovadas_L1 = 0
    Estanquiedade_Reprovadas_L1 = 0
    Pressurizacao_Aprovadas_L1 = 0
    Pressurizacao_Reprovadas_L1 = 0
    Hypot_Aprovadas_L1 = 0
    Hypot_Reprovadas_L1 = 0
    sistema_ativado_l1 = False
    sistema_iniciado_linha_1 = False
    contagem_projetada_l1 = 0














        # Linha 2
    subscriber_mesa_2 = MQTTSubscriber(broker, "Mesa2")
    subscriber_est_2_ap = MQTTSubscriber(broker, "EstA2")
    subscriber_est_2_rep = MQTTSubscriber(broker, "EstR2")
    subscriber_pre_2_ap = MQTTSubscriber(broker, "PreA2")
    subscriber_pre_2_rep = MQTTSubscriber(broker, "PreR2")
    subscriber_hy_2_ap = MQTTSubscriber(broker, "HyA2")
    subscriber_hy_2_rep = MQTTSubscriber(broker, "HyP2")
    subscriber_op_L2 = MQTTSubscriber(broker, "op_L2")

    Mesa_de_Montagem_L2 = 0
    Estanquiedade_Aprovadas_L2 = 0
    Estanquiedade_Reprovadas_L2 = 0
    Pressurizacao_Aprovadas_L2 = 0
    Pressurizacao_Reprovadas_L2 = 0
    Hypot_Aprovadas_L2 = 0
    Hypot_Reprovadas_L2 = 0
    sistema_ativado_l2 = False
    sistema_iniciado_linha_2 = False
    contagem_projetada_l2 = 0



        # Linha 3
    subscriber_mesa_3 = MQTTSubscriber(broker, "Mesa3")
    subscriber_est_3_ap = MQTTSubscriber(broker, "EstA3")
    subscriber_est_3_rep = MQTTSubscriber(broker, "EstR3")
    subscriber_hy_3_ap = MQTTSubscriber(broker, "HyA3")
    subscriber_hy_3_rep = MQTTSubscriber(broker, "HyP3")
    subscriber_op_L3 = MQTTSubscriber(broker, "op_L3")




    Mesa_de_Montagem_L3 = 0
    Estanquiedade_Aprovadas_L3 = 0
    Estanquiedade_Reprovadas_L3 = 0
    Pressurizacao_Aprovadas_L3 = 0
    Pressurizacao_Reprovadas_L3 = 0
    Hypot_Aprovadas_L3 = 0
    Hypot_Reprovadas_L3 = 0
    sistema_ativado_l3 = False
    sistema_iniciado_linha_3 = False
    contagem_projetada_l3 = 0

        # Linha 4
    subscriber_mesa_4 = MQTTSubscriber(broker, "Mesa4")
    subscriber_est_4_ap = MQTTSubscriber(broker, "EstA4")
    subscriber_est_4_rep = MQTTSubscriber(broker, "EstR4")
    subscriber_pre_4_ap = MQTTSubscriber(broker, "PreA4")
    subscriber_pre_4_rep = MQTTSubscriber(broker, "PreR4")
    subscriber_hy_4_ap = MQTTSubscriber(broker, "HyA4")
    subscriber_hy_4_rep = MQTTSubscriber(broker, "HyR4")
    subscriber_op_L4 = MQTTSubscriber(broker, "op_L4")

    Mesa_de_Montagem_L4 = 0
    Estanquiedade_Aprovadas_L4 = 0
    Estanquiedade_Reprovadas_L4 = 0
    Pressurizacao_Aprovadas_L4 = 0
    Pressurizacao_Reprovadas_L4 = 0
    Hypot_Aprovadas_L4 = 0
    Hypot_Reprovadas_L4 = 0
    sistema_ativado_l4 = False
    sistema_iniciado_linha_4 = False
    contagem_projetada_l4 = 0



















    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1578, 769)
        MainWindow.setStyleSheet(u"background-color: rgb(9, 9, 9);\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0738636 rgba(40, 59, 100, 255), stop:0.485876 rgba(29, 51, 56, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 20, 1381, 561))
        self.tabWidget.setMouseTracking(False)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"background-color: rgb(61, 61, 61);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 85, 127);\n"
"alternate-background-color: rgb(0, 85, 127);\n"
"border-top-color: rgb(0, 85, 127);\n"
"border-left-color: rgb(0, 85, 127);\n"
"border-right-color: rgb(0, 85, 127);\n"
"border-bottom-color: rgb(0, 85, 127);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(12, 12))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_linha_1 = QWidget()
        self.tab_linha_1.setObjectName(u"tab_linha_1")
        self.f_mesa_l1 = QFrame(self.tab_linha_1)
        self.f_mesa_l1.setObjectName(u"f_mesa_l1")
        self.f_mesa_l1.setGeometry(QRect(170, 100, 311, 151))
        self.f_mesa_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_mesa_l1.setFrameShape(QFrame.StyledPanel)
        self.f_mesa_l1.setFrameShadow(QFrame.Raised)
        self.lcd_mesa_l1 = QLCDNumber(self.f_mesa_l1)
        self.lcd_mesa_l1.setObjectName(u"lcd_mesa_l1")
        self.lcd_mesa_l1.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_mesa_l1.setStyleSheet(u"\n"
"color: rgb(22, 102, 223);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_mesa_l1.setProperty("value", 0.000000000000000)
        self.text_est_l1 = QLabel(self.tab_linha_1)
        self.text_est_l1.setObjectName(u"text_est_l1")
        self.text_est_l1.setGeometry(QRect(640, 10, 191, 41))
        self.text_est_l1.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.text_pre_l1 = QLabel(self.tab_linha_1)
        self.text_pre_l1.setObjectName(u"text_pre_l1")
        self.text_pre_l1.setGeometry(QRect(900, 10, 181, 41))
        self.text_pre_l1.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.text_hypot_l1 = QLabel(self.tab_linha_1)
        self.text_hypot_l1.setObjectName(u"text_hypot_l1")
        self.text_hypot_l1.setGeometry(QRect(1190, 10, 91, 41))
        self.text_hypot_l1.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.text_mesa_l1 = QLabel(self.tab_linha_1)
        self.text_mesa_l1.setObjectName(u"text_mesa_l1")
        self.text_mesa_l1.setGeometry(QRect(190, 40, 281, 41))
        self.text_mesa_l1.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.label_status_l1 = QLabel(self.tab_linha_1)
        self.label_status_l1.setObjectName(u"label_status_l1")
        self.label_status_l1.setGeometry(QRect(10, 10, 111, 16))
        self.label_status_l1.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.status_l1 = QLabel(self.tab_linha_1)
        self.status_l1.setObjectName(u"status_l1")
        self.status_l1.setGeometry(QRect(110, 10, 121, 16))
        self.status_l1.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 85, 0);")
        self.f_cont_p_l1 = QFrame(self.tab_linha_1)
        self.f_cont_p_l1.setObjectName(u"f_cont_p_l1")
        self.f_cont_p_l1.setGeometry(QRect(170, 360, 311, 151))
        self.f_cont_p_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_cont_p_l1.setFrameShape(QFrame.StyledPanel)
        self.f_cont_p_l1.setFrameShadow(QFrame.Raised)
        self.lcd_cont_p_l1 = QLCDNumber(self.f_cont_p_l1)
        self.lcd_cont_p_l1.setObjectName(u"lcd_cont_p_l1")
        self.lcd_cont_p_l1.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_cont_p_l1.setStyleSheet(u"\n"
"color: rgb(125, 125, 125);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_cont_p_l1.setProperty("value", 0.000000000000000)
        self.text_cont_p_l1 = QLabel(self.tab_linha_1)
        self.text_cont_p_l1.setObjectName(u"text_cont_p_l1")
        self.text_cont_p_l1.setGeometry(QRect(180, 300, 291, 41))
        self.text_cont_p_l1.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.group_apr_l1 = QGroupBox(self.tab_linha_1)
        self.group_apr_l1.setObjectName(u"group_apr_l1")
        self.group_apr_l1.setGeometry(QRect(620, 90, 761, 181))
        self.group_apr_l1.setMouseTracking(False)
        self.group_apr_l1.setTabletTracking(False)
        self.group_apr_l1.setFocusPolicy(Qt.NoFocus)
        self.group_apr_l1.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.group_apr_l1.setAcceptDrops(False)
        self.group_apr_l1.setLayoutDirection(Qt.LeftToRight)
        self.group_apr_l1.setAutoFillBackground(False)
        self.group_apr_l1.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.group_apr_l1.setFlat(True)
        self.f_est_ap_l1 = QFrame(self.group_apr_l1)
        self.f_est_ap_l1.setObjectName(u"f_est_ap_l1")
        self.f_est_ap_l1.setGeometry(QRect(40, 40, 171, 91))
        self.f_est_ap_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_ap_l1.setFrameShape(QFrame.StyledPanel)
        self.f_est_ap_l1.setFrameShadow(QFrame.Raised)
        self.lcd_est_ap_l1 = QLCDNumber(self.f_est_ap_l1)
        self.lcd_est_ap_l1.setObjectName(u"lcd_est_ap_l1")
        self.lcd_est_ap_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_est_ap_l1.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.f_hy_ap_l1 = QFrame(self.group_apr_l1)
        self.f_hy_ap_l1.setObjectName(u"f_hy_ap_l1")
        self.f_hy_ap_l1.setGeometry(QRect(540, 40, 171, 91))
        self.f_hy_ap_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_ap_l1.setFrameShape(QFrame.StyledPanel)
        self.f_hy_ap_l1.setFrameShadow(QFrame.Raised)
        self.lcd_hy_ap_l1 = QLCDNumber(self.f_hy_ap_l1)
        self.lcd_hy_ap_l1.setObjectName(u"lcd_hy_ap_l1")
        self.lcd_hy_ap_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_hy_ap_l1.setStyleSheet(u"border-color: rgb(0, 255, 255);\n"
"color: rgb(0, 255, 0);")
        self.f_pre_ap_l1 = QFrame(self.group_apr_l1)
        self.f_pre_ap_l1.setObjectName(u"f_pre_ap_l1")
        self.f_pre_ap_l1.setGeometry(QRect(290, 40, 171, 91))
        self.f_pre_ap_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_pre_ap_l1.setFrameShape(QFrame.StyledPanel)
        self.f_pre_ap_l1.setFrameShadow(QFrame.Raised)
        self.lcd_pre_ap_l1 = QLCDNumber(self.f_pre_ap_l1)
        self.lcd_pre_ap_l1.setObjectName(u"lcd_pre_ap_l1")
        self.lcd_pre_ap_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_pre_ap_l1.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.group_rep_l1 = QGroupBox(self.tab_linha_1)
        self.group_rep_l1.setObjectName(u"group_rep_l1")
        self.group_rep_l1.setGeometry(QRect(620, 310, 761, 181))
        self.group_rep_l1.setLayoutDirection(Qt.LeftToRight)
        self.group_rep_l1.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.group_rep_l1.setFlat(True)
        self.group_rep_l1.setCheckable(False)
        self.f_est_rep_l1 = QFrame(self.group_rep_l1)
        self.f_est_rep_l1.setObjectName(u"f_est_rep_l1")
        self.f_est_rep_l1.setGeometry(QRect(40, 40, 171, 91))
        self.f_est_rep_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_rep_l1.setFrameShape(QFrame.StyledPanel)
        self.f_est_rep_l1.setFrameShadow(QFrame.Raised)
        self.lcd_est_rep_l1 = QLCDNumber(self.f_est_rep_l1)
        self.lcd_est_rep_l1.setObjectName(u"lcd_est_rep_l1")
        self.lcd_est_rep_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_est_rep_l1.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.f_pre_rep_l1 = QFrame(self.group_rep_l1)
        self.f_pre_rep_l1.setObjectName(u"f_pre_rep_l1")
        self.f_pre_rep_l1.setGeometry(QRect(290, 40, 171, 91))
        self.f_pre_rep_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_pre_rep_l1.setFrameShape(QFrame.StyledPanel)
        self.f_pre_rep_l1.setFrameShadow(QFrame.Raised)
        self.lcd_pre_rep_l1 = QLCDNumber(self.f_pre_rep_l1)
        self.lcd_pre_rep_l1.setObjectName(u"lcd_pre_rep_l1")
        self.lcd_pre_rep_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_pre_rep_l1.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.f_hyp_rep_l1 = QFrame(self.group_rep_l1)
        self.f_hyp_rep_l1.setObjectName(u"f_hyp_rep_l1")
        self.f_hyp_rep_l1.setGeometry(QRect(540, 40, 171, 91))
        self.f_hyp_rep_l1.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hyp_rep_l1.setFrameShape(QFrame.StyledPanel)
        self.f_hyp_rep_l1.setFrameShadow(QFrame.Raised)
        self.lcd_hy_rep_l1 = QLCDNumber(self.f_hyp_rep_l1)
        self.lcd_hy_rep_l1.setObjectName(u"lcd_hy_rep_l1")
        self.lcd_hy_rep_l1.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_hy_rep_l1.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        icon = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.tabWidget.addTab(self.tab_linha_1, icon, "")
        self.group_rep_l1.raise_()
        self.group_apr_l1.raise_()
        self.f_mesa_l1.raise_()
        self.text_est_l1.raise_()
        self.text_pre_l1.raise_()
        self.text_hypot_l1.raise_()
        self.text_mesa_l1.raise_()
        self.label_status_l1.raise_()
        self.status_l1.raise_()
        self.f_cont_p_l1.raise_()
        self.text_cont_p_l1.raise_()
        self.tab_linha_2 = QWidget()
        self.tab_linha_2.setObjectName(u"tab_linha_2")
        self.status_l2 = QLabel(self.tab_linha_2)
        self.status_l2.setObjectName(u"status_l2")
        self.status_l2.setGeometry(QRect(110, 10, 141, 16))
        self.status_l2.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 85, 0);")
        self.text_mesa_l2 = QLabel(self.tab_linha_2)
        self.text_mesa_l2.setObjectName(u"text_mesa_l2")
        self.text_mesa_l2.setGeometry(QRect(190, 40, 281, 41))
        self.text_mesa_l2.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.text_pre_l2 = QLabel(self.tab_linha_2)
        self.text_pre_l2.setObjectName(u"text_pre_l2")
        self.text_pre_l2.setGeometry(QRect(900, 10, 181, 41))
        self.text_pre_l2.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.text_est_l2 = QLabel(self.tab_linha_2)
        self.text_est_l2.setObjectName(u"text_est_l2")
        self.text_est_l2.setGeometry(QRect(640, 10, 191, 41))
        self.text_est_l2.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.text_cont_p_l2 = QLabel(self.tab_linha_2)
        self.text_cont_p_l2.setObjectName(u"text_cont_p_l2")
        self.text_cont_p_l2.setGeometry(QRect(180, 300, 291, 41))
        self.text_cont_p_l2.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.f_cont_p_l2 = QFrame(self.tab_linha_2)
        self.f_cont_p_l2.setObjectName(u"f_cont_p_l2")
        self.f_cont_p_l2.setGeometry(QRect(170, 360, 311, 151))
        self.f_cont_p_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_cont_p_l2.setFrameShape(QFrame.StyledPanel)
        self.f_cont_p_l2.setFrameShadow(QFrame.Raised)
        self.lcd_cont_p_l2 = QLCDNumber(self.f_cont_p_l2)
        self.lcd_cont_p_l2.setObjectName(u"lcd_cont_p_l2")
        self.lcd_cont_p_l2.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_cont_p_l2.setStyleSheet(u"\n"
"color: rgb(125, 125, 125);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_cont_p_l2.setProperty("value", 0.000000000000000)
        self.f_mesa_l2 = QFrame(self.tab_linha_2)
        self.f_mesa_l2.setObjectName(u"f_mesa_l2")
        self.f_mesa_l2.setGeometry(QRect(170, 100, 311, 151))
        self.f_mesa_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_mesa_l2.setFrameShape(QFrame.StyledPanel)
        self.f_mesa_l2.setFrameShadow(QFrame.Raised)
        self.lcd_mesa_l2 = QLCDNumber(self.f_mesa_l2)
        self.lcd_mesa_l2.setObjectName(u"lcd_mesa_l2")
        self.lcd_mesa_l2.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_mesa_l2.setStyleSheet(u"\n"
"color: rgb(22, 102, 223);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_mesa_l2.setProperty("value", 0.000000000000000)
        self.group_rep_l2 = QGroupBox(self.tab_linha_2)
        self.group_rep_l2.setObjectName(u"group_rep_l2")
        self.group_rep_l2.setGeometry(QRect(620, 310, 761, 181))
        self.group_rep_l2.setLayoutDirection(Qt.LeftToRight)
        self.group_rep_l2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.group_rep_l2.setFlat(True)
        self.group_rep_l2.setCheckable(False)
        self.f_hy_rep_l2 = QFrame(self.group_rep_l2)
        self.f_hy_rep_l2.setObjectName(u"f_hy_rep_l2")
        self.f_hy_rep_l2.setGeometry(QRect(540, 40, 171, 91))
        self.f_hy_rep_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_rep_l2.setFrameShape(QFrame.StyledPanel)
        self.f_hy_rep_l2.setFrameShadow(QFrame.Raised)
        self.lcd_hy_rep_l2 = QLCDNumber(self.f_hy_rep_l2)
        self.lcd_hy_rep_l2.setObjectName(u"lcd_hy_rep_l2")
        self.lcd_hy_rep_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_hy_rep_l2.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"border-color: rgb(255, 0, 0);")
        self.f_est_rep_l2 = QFrame(self.group_rep_l2)
        self.f_est_rep_l2.setObjectName(u"f_est_rep_l2")
        self.f_est_rep_l2.setGeometry(QRect(40, 40, 171, 91))
        self.f_est_rep_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_rep_l2.setFrameShape(QFrame.StyledPanel)
        self.f_est_rep_l2.setFrameShadow(QFrame.Raised)
        self.lcd_est_rep_l2 = QLCDNumber(self.f_est_rep_l2)
        self.lcd_est_rep_l2.setObjectName(u"lcd_est_rep_l2")
        self.lcd_est_rep_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_est_rep_l2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.f_pre_rep_l2 = QFrame(self.group_rep_l2)
        self.f_pre_rep_l2.setObjectName(u"f_pre_rep_l2")
        self.f_pre_rep_l2.setGeometry(QRect(290, 40, 171, 91))
        self.f_pre_rep_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_pre_rep_l2.setFrameShape(QFrame.StyledPanel)
        self.f_pre_rep_l2.setFrameShadow(QFrame.Raised)
        self.lcd_pre_rep_l2 = QLCDNumber(self.f_pre_rep_l2)
        self.lcd_pre_rep_l2.setObjectName(u"lcd_pre_rep_l2")
        self.lcd_pre_rep_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_pre_rep_l2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_status_l2 = QLabel(self.tab_linha_2)
        self.label_status_l2.setObjectName(u"label_status_l2")
        self.label_status_l2.setGeometry(QRect(10, 10, 111, 16))
        self.label_status_l2.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.text_hy_l2 = QLabel(self.tab_linha_2)
        self.text_hy_l2.setObjectName(u"text_hy_l2")
        self.text_hy_l2.setGeometry(QRect(1190, 10, 91, 41))
        self.text_hy_l2.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.group_apr_l2 = QGroupBox(self.tab_linha_2)
        self.group_apr_l2.setObjectName(u"group_apr_l2")
        self.group_apr_l2.setGeometry(QRect(620, 90, 761, 181))
        self.group_apr_l2.setMouseTracking(False)
        self.group_apr_l2.setTabletTracking(False)
        self.group_apr_l2.setFocusPolicy(Qt.NoFocus)
        self.group_apr_l2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.group_apr_l2.setAcceptDrops(False)
        self.group_apr_l2.setLayoutDirection(Qt.LeftToRight)
        self.group_apr_l2.setAutoFillBackground(False)
        self.group_apr_l2.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.group_apr_l2.setFlat(True)
        self.f_est_ap_l2 = QFrame(self.group_apr_l2)
        self.f_est_ap_l2.setObjectName(u"f_est_ap_l2")
        self.f_est_ap_l2.setGeometry(QRect(40, 40, 171, 91))
        self.f_est_ap_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_ap_l2.setFrameShape(QFrame.StyledPanel)
        self.f_est_ap_l2.setFrameShadow(QFrame.Raised)
        self.lcd_est_ap_l2 = QLCDNumber(self.f_est_ap_l2)
        self.lcd_est_ap_l2.setObjectName(u"lcd_est_ap_l2")
        self.lcd_est_ap_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_est_ap_l2.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.f_hy_ap_l2 = QFrame(self.group_apr_l2)
        self.f_hy_ap_l2.setObjectName(u"f_hy_ap_l2")
        self.f_hy_ap_l2.setGeometry(QRect(540, 40, 171, 91))
        self.f_hy_ap_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_ap_l2.setFrameShape(QFrame.StyledPanel)
        self.f_hy_ap_l2.setFrameShadow(QFrame.Raised)
        self.lcd_hy_ap_l2 = QLCDNumber(self.f_hy_ap_l2)
        self.lcd_hy_ap_l2.setObjectName(u"lcd_hy_ap_l2")
        self.lcd_hy_ap_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_hy_ap_l2.setStyleSheet(u"border-color: rgb(0, 255, 255);\n"
"color: rgb(0, 255, 0);")
        self.f_pre_ap_l2 = QFrame(self.group_apr_l2)
        self.f_pre_ap_l2.setObjectName(u"f_pre_ap_l2")
        self.f_pre_ap_l2.setGeometry(QRect(290, 40, 171, 91))
        self.f_pre_ap_l2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_pre_ap_l2.setFrameShape(QFrame.StyledPanel)
        self.f_pre_ap_l2.setFrameShadow(QFrame.Raised)
        self.lcd_pre_ap_l2 = QLCDNumber(self.f_pre_ap_l2)
        self.lcd_pre_ap_l2.setObjectName(u"lcd_pre_ap_l2")
        self.lcd_pre_ap_l2.setGeometry(QRect(10, 20, 151, 51))
        self.lcd_pre_ap_l2.setStyleSheet(u"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.tabWidget.addTab(self.tab_linha_2, "")
        self.group_rep_l2.raise_()
        self.text_mesa_l2.raise_()
        self.text_pre_l2.raise_()
        self.text_est_l2.raise_()
        self.text_cont_p_l2.raise_()
        self.f_cont_p_l2.raise_()
        self.f_mesa_l2.raise_()
        self.label_status_l2.raise_()
        self.text_hy_l2.raise_()
        self.group_apr_l2.raise_()
        self.status_l2.raise_()
        self.tab_linha_3 = QWidget()
        self.tab_linha_3.setObjectName(u"tab_linha_3")
        self.f_lcd_mesa_l3 = QFrame(self.tab_linha_3)
        self.f_lcd_mesa_l3.setObjectName(u"f_lcd_mesa_l3")
        self.f_lcd_mesa_l3.setGeometry(QRect(170, 100, 311, 151))
        self.f_lcd_mesa_l3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_lcd_mesa_l3.setFrameShape(QFrame.StyledPanel)
        self.f_lcd_mesa_l3.setFrameShadow(QFrame.Raised)
        self.lcd_mesa_l3 = QLCDNumber(self.f_lcd_mesa_l3)
        self.lcd_mesa_l3.setObjectName(u"lcd_mesa_l3")
        self.lcd_mesa_l3.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_mesa_l3.setStyleSheet(u"\n"
"color: rgb(22, 102, 223);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_mesa_l3.setProperty("value", 0.000000000000000)
        self.text_mesa_l3 = QLabel(self.tab_linha_3)
        self.text_mesa_l3.setObjectName(u"text_mesa_l3")
        self.text_mesa_l3.setGeometry(QRect(190, 40, 281, 41))
        self.text_mesa_l3.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.text_est_l3 = QLabel(self.tab_linha_3)
        self.text_est_l3.setObjectName(u"text_est_l3")
        self.text_est_l3.setGeometry(QRect(730, 10, 191, 41))
        self.text_est_l3.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.group_apr_l3 = QGroupBox(self.tab_linha_3)
        self.group_apr_l3.setObjectName(u"group_apr_l3")
        self.group_apr_l3.setGeometry(QRect(620, 90, 761, 181))
        self.group_apr_l3.setMouseTracking(False)
        self.group_apr_l3.setTabletTracking(False)
        self.group_apr_l3.setFocusPolicy(Qt.NoFocus)
        self.group_apr_l3.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.group_apr_l3.setAcceptDrops(False)
        self.group_apr_l3.setLayoutDirection(Qt.LeftToRight)
        self.group_apr_l3.setAutoFillBackground(False)
        self.group_apr_l3.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.group_apr_l3.setFlat(True)
        self.f_est_ap_l3 = QFrame(self.group_apr_l3)
        self.f_est_ap_l3.setObjectName(u"f_est_ap_l3")
        self.f_est_ap_l3.setGeometry(QRect(90, 50, 211, 121))
        self.f_est_ap_l3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_ap_l3.setFrameShape(QFrame.StyledPanel)
        self.f_est_ap_l3.setFrameShadow(QFrame.Raised)
        self.lcd_est_ap_l3 = QLCDNumber(self.f_est_ap_l3)
        self.lcd_est_ap_l3.setObjectName(u"lcd_est_ap_l3")
        self.lcd_est_ap_l3.setGeometry(QRect(20, 20, 171, 71))
        self.lcd_est_ap_l3.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.f_hy_ap_l3 = QFrame(self.group_apr_l3)
        self.f_hy_ap_l3.setObjectName(u"f_hy_ap_l3")
        self.f_hy_ap_l3.setGeometry(QRect(450, 50, 211, 121))
        self.f_hy_ap_l3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_ap_l3.setFrameShape(QFrame.StyledPanel)
        self.f_hy_ap_l3.setFrameShadow(QFrame.Raised)
        self.lcd_hy_ap_l3 = QLCDNumber(self.f_hy_ap_l3)
        self.lcd_hy_ap_l3.setObjectName(u"lcd_hy_ap_l3")
        self.lcd_hy_ap_l3.setGeometry(QRect(20, 20, 171, 71))
        self.lcd_hy_ap_l3.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.frame_72 = QFrame(self.tab_linha_3)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setGeometry(QRect(170, 360, 311, 151))
        self.frame_72.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.lcd_cont_prog_l3 = QLCDNumber(self.frame_72)
        self.lcd_cont_prog_l3.setObjectName(u"lcd_cont_prog_l3")
        self.lcd_cont_prog_l3.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_cont_prog_l3.setStyleSheet(u"\n"
"color: rgb(125, 125, 125);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_cont_prog_l3.setProperty("value", 0.000000000000000)
        self.status_l3 = QLabel(self.tab_linha_3)
        self.status_l3.setObjectName(u"status_l3")
        self.status_l3.setGeometry(QRect(110, 10, 141, 16))
        self.status_l3.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 85, 0);")
        self.text_hy_l3 = QLabel(self.tab_linha_3)
        self.text_hy_l3.setObjectName(u"text_hy_l3")
        self.text_hy_l3.setGeometry(QRect(1120, 10, 91, 41))
        self.text_hy_l3.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.label_status_l3 = QLabel(self.tab_linha_3)
        self.label_status_l3.setObjectName(u"label_status_l3")
        self.label_status_l3.setGeometry(QRect(10, 10, 111, 16))
        self.label_status_l3.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.group_rep_l3 = QGroupBox(self.tab_linha_3)
        self.group_rep_l3.setObjectName(u"group_rep_l3")
        self.group_rep_l3.setGeometry(QRect(620, 310, 761, 181))
        self.group_rep_l3.setLayoutDirection(Qt.LeftToRight)
        self.group_rep_l3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.group_rep_l3.setFlat(True)
        self.group_rep_l3.setCheckable(False)
        self.f_est_rep_l3 = QFrame(self.group_rep_l3)
        self.f_est_rep_l3.setObjectName(u"f_est_rep_l3")
        self.f_est_rep_l3.setGeometry(QRect(90, 40, 211, 121))
        self.f_est_rep_l3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_rep_l3.setFrameShape(QFrame.StyledPanel)
        self.f_est_rep_l3.setFrameShadow(QFrame.Raised)
        self.lcd_est_rep_l3 = QLCDNumber(self.f_est_rep_l3)
        self.lcd_est_rep_l3.setObjectName(u"lcd_est_rep_l3")
        self.lcd_est_rep_l3.setGeometry(QRect(20, 20, 171, 81))
        self.lcd_est_rep_l3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.f_hy_rep_l3 = QFrame(self.group_rep_l3)
        self.f_hy_rep_l3.setObjectName(u"f_hy_rep_l3")
        self.f_hy_rep_l3.setGeometry(QRect(450, 40, 211, 121))
        self.f_hy_rep_l3.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_rep_l3.setFrameShape(QFrame.StyledPanel)
        self.f_hy_rep_l3.setFrameShadow(QFrame.Raised)
        self.lcd_hy_rep_l3 = QLCDNumber(self.f_hy_rep_l3)
        self.lcd_hy_rep_l3.setObjectName(u"lcd_hy_rep_l3")
        self.lcd_hy_rep_l3.setGeometry(QRect(20, 20, 171, 81))
        self.lcd_hy_rep_l3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_cont_p_l3 = QLabel(self.tab_linha_3)
        self.text_cont_p_l3.setObjectName(u"text_cont_p_l3")
        self.text_cont_p_l3.setGeometry(QRect(180, 300, 291, 41))
        self.text_cont_p_l3.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.tabWidget.addTab(self.tab_linha_3, "")
        self.f_lcd_mesa_l3.raise_()
        self.text_mesa_l3.raise_()
        self.text_est_l3.raise_()
        self.group_apr_l3.raise_()
        self.frame_72.raise_()
        self.text_hy_l3.raise_()
        self.label_status_l3.raise_()
        self.group_rep_l3.raise_()
        self.text_cont_p_l3.raise_()
        self.status_l3.raise_()
        self.tab_linha_4 = QWidget()
        self.tab_linha_4.setObjectName(u"tab_linha_4")
        self.text_cont_p_l4 = QLabel(self.tab_linha_4)
        self.text_cont_p_l4.setObjectName(u"text_cont_p_l4")
        self.text_cont_p_l4.setGeometry(QRect(180, 300, 291, 41))
        self.text_cont_p_l4.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.f_mesa_l4 = QFrame(self.tab_linha_4)
        self.f_mesa_l4.setObjectName(u"f_mesa_l4")
        self.f_mesa_l4.setGeometry(QRect(170, 100, 311, 151))
        self.f_mesa_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_mesa_l4.setFrameShape(QFrame.StyledPanel)
        self.f_mesa_l4.setFrameShadow(QFrame.Raised)
        self.lcd_mesa_l4 = QLCDNumber(self.f_mesa_l4)
        self.lcd_mesa_l4.setObjectName(u"lcd_mesa_l4")
        self.lcd_mesa_l4.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_mesa_l4.setStyleSheet(u"\n"
"color: rgb(22, 102, 223);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_mesa_l4.setProperty("value", 0.000000000000000)
        self.label_status_l4 = QLabel(self.tab_linha_4)
        self.label_status_l4.setObjectName(u"label_status_l4")
        self.label_status_l4.setGeometry(QRect(10, 10, 111, 16))
        self.label_status_l4.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.group_apr_l4 = QGroupBox(self.tab_linha_4)
        self.group_apr_l4.setObjectName(u"group_apr_l4")
        self.group_apr_l4.setGeometry(QRect(620, 90, 761, 181))
        self.group_apr_l4.setMouseTracking(False)
        self.group_apr_l4.setTabletTracking(False)
        self.group_apr_l4.setFocusPolicy(Qt.NoFocus)
        self.group_apr_l4.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.group_apr_l4.setAcceptDrops(False)
        self.group_apr_l4.setLayoutDirection(Qt.LeftToRight)
        self.group_apr_l4.setAutoFillBackground(False)
        self.group_apr_l4.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.group_apr_l4.setFlat(True)
        self.f_est_ap_l4 = QFrame(self.group_apr_l4)
        self.f_est_ap_l4.setObjectName(u"f_est_ap_l4")
        self.f_est_ap_l4.setGeometry(QRect(90, 50, 211, 121))
        self.f_est_ap_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_ap_l4.setFrameShape(QFrame.StyledPanel)
        self.f_est_ap_l4.setFrameShadow(QFrame.Raised)
        self.lcd_est_ap_l4 = QLCDNumber(self.f_est_ap_l4)
        self.lcd_est_ap_l4.setObjectName(u"lcd_est_ap_l4")
        self.lcd_est_ap_l4.setGeometry(QRect(20, 20, 171, 71))
        self.lcd_est_ap_l4.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.f_hy_ap_l4 = QFrame(self.group_apr_l4)
        self.f_hy_ap_l4.setObjectName(u"f_hy_ap_l4")
        self.f_hy_ap_l4.setGeometry(QRect(450, 50, 211, 121))
        self.f_hy_ap_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_ap_l4.setFrameShape(QFrame.StyledPanel)
        self.f_hy_ap_l4.setFrameShadow(QFrame.Raised)
        self.lcd_hy_ap_l4 = QLCDNumber(self.f_hy_ap_l4)
        self.lcd_hy_ap_l4.setObjectName(u"lcd_hy_ap_l4")
        self.lcd_hy_ap_l4.setGeometry(QRect(20, 20, 171, 71))
        self.lcd_hy_ap_l4.setStyleSheet(u"\n"
"color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 255);")
        self.group_rep_l4 = QGroupBox(self.tab_linha_4)
        self.group_rep_l4.setObjectName(u"group_rep_l4")
        self.group_rep_l4.setGeometry(QRect(620, 310, 761, 181))
        self.group_rep_l4.setLayoutDirection(Qt.LeftToRight)
        self.group_rep_l4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.group_rep_l4.setFlat(True)
        self.group_rep_l4.setCheckable(False)
        self.f_est_rep_l4 = QFrame(self.group_rep_l4)
        self.f_est_rep_l4.setObjectName(u"f_est_rep_l4")
        self.f_est_rep_l4.setGeometry(QRect(90, 40, 211, 121))
        self.f_est_rep_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_est_rep_l4.setFrameShape(QFrame.StyledPanel)
        self.f_est_rep_l4.setFrameShadow(QFrame.Raised)
        self.lcd_est_rep_l4 = QLCDNumber(self.f_est_rep_l4)
        self.lcd_est_rep_l4.setObjectName(u"lcd_est_rep_l4")
        self.lcd_est_rep_l4.setGeometry(QRect(20, 20, 171, 81))
        self.lcd_est_rep_l4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.f_hy_rep_l4 = QFrame(self.group_rep_l4)
        self.f_hy_rep_l4.setObjectName(u"f_hy_rep_l4")
        self.f_hy_rep_l4.setGeometry(QRect(450, 40, 211, 121))
        self.f_hy_rep_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_hy_rep_l4.setFrameShape(QFrame.StyledPanel)
        self.f_hy_rep_l4.setFrameShadow(QFrame.Raised)
        self.lcd_hy_rep_l4 = QLCDNumber(self.f_hy_rep_l4)
        self.lcd_hy_rep_l4.setObjectName(u"lcd_hy_rep_l4")
        self.lcd_hy_rep_l4.setGeometry(QRect(20, 20, 171, 81))
        self.lcd_hy_rep_l4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.text_mesa_l4 = QLabel(self.tab_linha_4)
        self.text_mesa_l4.setObjectName(u"text_mesa_l4")
        self.text_mesa_l4.setGeometry(QRect(190, 40, 281, 41))
        self.text_mesa_l4.setStyleSheet(u"font: 700 22pt \"Segoe UI\";\n"
"")
        self.text_est_l4 = QLabel(self.tab_linha_4)
        self.text_est_l4.setObjectName(u"text_est_l4")
        self.text_est_l4.setGeometry(QRect(730, 10, 191, 41))
        self.text_est_l4.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.f_cont_p_l4 = QFrame(self.tab_linha_4)
        self.f_cont_p_l4.setObjectName(u"f_cont_p_l4")
        self.f_cont_p_l4.setGeometry(QRect(170, 360, 311, 151))
        self.f_cont_p_l4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.f_cont_p_l4.setFrameShape(QFrame.StyledPanel)
        self.f_cont_p_l4.setFrameShadow(QFrame.Raised)
        self.lcd_cont_p_l4 = QLCDNumber(self.f_cont_p_l4)
        self.lcd_cont_p_l4.setObjectName(u"lcd_cont_p_l4")
        self.lcd_cont_p_l4.setGeometry(QRect(20, 30, 261, 91))
        self.lcd_cont_p_l4.setStyleSheet(u"\n"
"color: rgb(125, 125, 125);\n"
"border-color: rgb(0, 255, 255);")
        self.lcd_cont_p_l4.setProperty("value", 0.000000000000000)
        self.text_hy_l4 = QLabel(self.tab_linha_4)
        self.text_hy_l4.setObjectName(u"text_hy_l4")
        self.text_hy_l4.setGeometry(QRect(1120, 10, 91, 41))
        self.text_hy_l4.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"")
        self.status_l4 = QLabel(self.tab_linha_4)
        self.status_l4.setObjectName(u"status_l4")
        self.status_l4.setGeometry(QRect(110, 10, 141, 16))
        self.status_l4.setStyleSheet(u"background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 85, 0);")
        self.tabWidget.addTab(self.tab_linha_4, "")
        self.tab_config_l1 = QWidget()
        self.tab_config_l1.setObjectName(u"tab_config_l1")
        self.group_primeiro_t_l1 = QGroupBox(self.tab_config_l1)
        self.group_primeiro_t_l1.setObjectName(u"group_primeiro_t_l1")
        self.group_primeiro_t_l1.setGeometry(QRect(70, 10, 611, 461))
        self.group_primeiro_t_l1.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_turno_inicio_1_l1.setObjectName(u"t_turno_inicio_1_l1")
        self.t_turno_inicio_1_l1.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_intervalo_inicio_1_l1.setObjectName(u"t_intervalo_inicio_1_l1")
        self.t_intervalo_inicio_1_l1.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_intervalo_fim_1_l1.setObjectName(u"t_intervalo_fim_1_l1")
        self.t_intervalo_fim_1_l1.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_laboral_inicio_1_l1.setObjectName(u"t_laboral_inicio_1_l1")
        self.t_laboral_inicio_1_l1.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_laboral_fim_1_l1.setObjectName(u"t_laboral_fim_1_l1")
        self.t_laboral_fim_1_l1.setGeometry(QRect(330, 210, 118, 22))
        self.t_almoco_inicio_1_L1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_almoco_inicio_1_L1.setObjectName(u"t_almoco_inicio_1_L1")
        self.t_almoco_inicio_1_L1.setGeometry(QRect(190, 260, 118, 22))
        self.t_almoco_fim_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_almoco_fim_1_l1.setObjectName(u"t_almoco_fim_1_l1")
        self.t_almoco_fim_1_l1.setGeometry(QRect(330, 260, 118, 22))
        self.box_almoco_1_l1 = QCheckBox(self.group_primeiro_t_l1)
        self.box_almoco_1_l1.setObjectName(u"box_almoco_1_l1")
        self.box_almoco_1_l1.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_1_l1 = QCheckBox(self.group_primeiro_t_l1)
        self.box_laboral_1_l1.setObjectName(u"box_laboral_1_l1")
        self.box_laboral_1_l1.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_1_l1 = QCheckBox(self.group_primeiro_t_l1)
        self.box_intervalo_1_l1.setObjectName(u"box_intervalo_1_l1")
        self.box_intervalo_1_l1.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_1_l1 = QCheckBox(self.group_primeiro_t_l1)
        self.box_turno_1_l1.setObjectName(u"box_turno_1_l1")
        self.box_turno_1_l1.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_1_l1 = QLabel(self.group_primeiro_t_l1)
        self.text_inicio_1_l1.setObjectName(u"text_inicio_1_l1")
        self.text_inicio_1_l1.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_1_l1 = QLabel(self.group_primeiro_t_l1)
        self.text_fim_1_l1.setObjectName(u"text_fim_1_l1")
        self.text_fim_1_l1.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_1_l1 = QSpinBox(self.group_primeiro_t_l1)
        self.spin_meta_1_l1.setObjectName(u"spin_meta_1_l1")
        self.spin_meta_1_l1.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_1_l1.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_1_l1.setMaximum(2000)
        self.text_meta_1_l1 = QLabel(self.group_primeiro_t_l1)
        self.text_meta_1_l1.setObjectName(u"text_meta_1_l1")
        self.text_meta_1_l1.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_1_l1.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_1_l1 = QLabel(self.group_primeiro_t_l1)
        self.text_temp_peca_1_l1.setObjectName(u"text_temp_peca_1_l1")
        self.text_temp_peca_1_l1.setGeometry(QRect(42, 370, 201, 21))
        self.text_temp_peca_1_l1.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_1_l1 = QLabel(self.group_primeiro_t_l1)
        self.temp_peca_1_l1.setObjectName(u"temp_peca_1_l1")
        self.temp_peca_1_l1.setGeometry(QRect(200, 370, 371, 21))
        self.temp_peca_1_l1.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_1_l1 = QTimeEdit(self.group_primeiro_t_l1)
        self.t_turno_fim_1_l1.setObjectName(u"t_turno_fim_1_l1")
        self.t_turno_fim_1_l1.setGeometry(QRect(330, 110, 118, 22))
        self.group_segundo_t_l1 = QGroupBox(self.tab_config_l1)
        self.group_segundo_t_l1.setObjectName(u"group_segundo_t_l1")
        self.group_segundo_t_l1.setGeometry(QRect(700, 10, 601, 461))
        self.group_segundo_t_l1.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_turno_inicio_2_l1.setObjectName(u"t_turno_inicio_2_l1")
        self.t_turno_inicio_2_l1.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_intervalo_inicio_2_l1.setObjectName(u"t_intervalo_inicio_2_l1")
        self.t_intervalo_inicio_2_l1.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_intervalo_fim_2_l1.setObjectName(u"t_intervalo_fim_2_l1")
        self.t_intervalo_fim_2_l1.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_laboral_inicio_2_l1.setObjectName(u"t_laboral_inicio_2_l1")
        self.t_laboral_inicio_2_l1.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_laboral_fim_2_l1.setObjectName(u"t_laboral_fim_2_l1")
        self.t_laboral_fim_2_l1.setGeometry(QRect(330, 210, 118, 22))
        self.t_janta_inicio_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_janta_inicio_2_l1.setObjectName(u"t_janta_inicio_2_l1")
        self.t_janta_inicio_2_l1.setGeometry(QRect(190, 260, 118, 22))
        self.t_janta_fim_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_janta_fim_2_l1.setObjectName(u"t_janta_fim_2_l1")
        self.t_janta_fim_2_l1.setGeometry(QRect(330, 260, 118, 22))
        self.box_janta_2_l1 = QCheckBox(self.group_segundo_t_l1)
        self.box_janta_2_l1.setObjectName(u"box_janta_2_l1")
        self.box_janta_2_l1.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_2_l1 = QCheckBox(self.group_segundo_t_l1)
        self.box_laboral_2_l1.setObjectName(u"box_laboral_2_l1")
        self.box_laboral_2_l1.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_2_l1 = QCheckBox(self.group_segundo_t_l1)
        self.box_intervalo_2_l1.setObjectName(u"box_intervalo_2_l1")
        self.box_intervalo_2_l1.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_2_l1 = QCheckBox(self.group_segundo_t_l1)
        self.box_turno_2_l1.setObjectName(u"box_turno_2_l1")
        self.box_turno_2_l1.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_2_l1 = QLabel(self.group_segundo_t_l1)
        self.text_inicio_2_l1.setObjectName(u"text_inicio_2_l1")
        self.text_inicio_2_l1.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_2_l1 = QLabel(self.group_segundo_t_l1)
        self.text_fim_2_l1.setObjectName(u"text_fim_2_l1")
        self.text_fim_2_l1.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_2_l1 = QSpinBox(self.group_segundo_t_l1)
        self.spin_meta_2_l1.setObjectName(u"spin_meta_2_l1")
        self.spin_meta_2_l1.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_2_l1.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_2_l1.setMaximum(2000)
        self.text_meta_2_l1 = QLabel(self.group_segundo_t_l1)
        self.text_meta_2_l1.setObjectName(u"text_meta_2_l1")
        self.text_meta_2_l1.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_2_l1.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_2_l1 = QLabel(self.group_segundo_t_l1)
        self.text_temp_peca_2_l1.setObjectName(u"text_temp_peca_2_l1")
        self.text_temp_peca_2_l1.setGeometry(QRect(50, 370, 201, 21))
        self.text_temp_peca_2_l1.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_2_l1 = QLabel(self.group_segundo_t_l1)
        self.temp_peca_2_l1.setObjectName(u"temp_peca_2_l1")
        self.temp_peca_2_l1.setGeometry(QRect(210, 370, 371, 21))
        self.temp_peca_2_l1.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_2_l1 = QTimeEdit(self.group_segundo_t_l1)
        self.t_turno_fim_2_l1.setObjectName(u"t_turno_fim_2_l1")
        self.t_turno_fim_2_l1.setGeometry(QRect(330, 110, 118, 22))
        self.button_set_linha_1 = QPushButton(self.tab_config_l1)
        self.button_set_linha_1.setObjectName(u"button_set_linha_1")
        self.button_set_linha_1.setGeometry(QRect(70, 490, 131, 31))
        self.button_set_linha_1.setStyleSheet(u"background-color: rgb(66, 199, 97);")
        self.button_reset_linha_1 = QPushButton(self.tab_config_l1)
        self.button_reset_linha_1.setObjectName(u"button_reset_linha_1")
        self.button_reset_linha_1.setGeometry(QRect(210, 490, 131, 31))
        self.button_reset_linha_1.setStyleSheet(u"background-color: rgb(170, 62, 43);")
        self.tabWidget.addTab(self.tab_config_l1, "")
        self.tab_config_l2 = QWidget()
        self.tab_config_l2.setObjectName(u"tab_config_l2")
        self.groupBox_5 = QGroupBox(self.tab_config_l2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(700, 10, 601, 461))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_turno_inicio_2_l2.setObjectName(u"t_turno_inicio_2_l2")
        self.t_turno_inicio_2_l2.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_intervalo_inicio_2_l2.setObjectName(u"t_intervalo_inicio_2_l2")
        self.t_intervalo_inicio_2_l2.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_intervalo_fim_2_l2.setObjectName(u"t_intervalo_fim_2_l2")
        self.t_intervalo_fim_2_l2.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_laboral_inicio_2_l2.setObjectName(u"t_laboral_inicio_2_l2")
        self.t_laboral_inicio_2_l2.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_laboral_fim_2_l2.setObjectName(u"t_laboral_fim_2_l2")
        self.t_laboral_fim_2_l2.setGeometry(QRect(330, 210, 118, 22))
        self.t_janta_inicio_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_janta_inicio_2_l2.setObjectName(u"t_janta_inicio_2_l2")
        self.t_janta_inicio_2_l2.setGeometry(QRect(190, 260, 118, 22))
        self.t_janta_fim_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_janta_fim_2_l2.setObjectName(u"t_janta_fim_2_l2")
        self.t_janta_fim_2_l2.setGeometry(QRect(330, 260, 118, 22))
        self.box_janta_2_l2 = QCheckBox(self.groupBox_5)
        self.box_janta_2_l2.setObjectName(u"box_janta_2_l2")
        self.box_janta_2_l2.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_2_l2 = QCheckBox(self.groupBox_5)
        self.box_laboral_2_l2.setObjectName(u"box_laboral_2_l2")
        self.box_laboral_2_l2.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_2_l2 = QCheckBox(self.groupBox_5)
        self.box_intervalo_2_l2.setObjectName(u"box_intervalo_2_l2")
        self.box_intervalo_2_l2.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_2_l2 = QCheckBox(self.groupBox_5)
        self.box_turno_2_l2.setObjectName(u"box_turno_2_l2")
        self.box_turno_2_l2.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_2_l2 = QLabel(self.groupBox_5)
        self.text_inicio_2_l2.setObjectName(u"text_inicio_2_l2")
        self.text_inicio_2_l2.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_2_l2 = QLabel(self.groupBox_5)
        self.text_fim_2_l2.setObjectName(u"text_fim_2_l2")
        self.text_fim_2_l2.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_2_l2 = QSpinBox(self.groupBox_5)
        self.spin_meta_2_l2.setObjectName(u"spin_meta_2_l2")
        self.spin_meta_2_l2.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_2_l2.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_2_l2.setMaximum(2000)
        self.text_meta_2_l2 = QLabel(self.groupBox_5)
        self.text_meta_2_l2.setObjectName(u"text_meta_2_l2")
        self.text_meta_2_l2.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_2_l2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_2_l2 = QLabel(self.groupBox_5)
        self.text_temp_peca_2_l2.setObjectName(u"text_temp_peca_2_l2")
        self.text_temp_peca_2_l2.setGeometry(QRect(50, 370, 201, 21))
        self.text_temp_peca_2_l2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_2_l2 = QLabel(self.groupBox_5)
        self.temp_peca_2_l2.setObjectName(u"temp_peca_2_l2")
        self.temp_peca_2_l2.setGeometry(QRect(210, 370, 371, 21))
        self.temp_peca_2_l2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_2_l2 = QTimeEdit(self.groupBox_5)
        self.t_turno_fim_2_l2.setObjectName(u"t_turno_fim_2_l2")
        self.t_turno_fim_2_l2.setGeometry(QRect(330, 110, 118, 22))
        self.button_reset_linha_2 = QPushButton(self.tab_config_l2)
        self.button_reset_linha_2.setObjectName(u"button_reset_linha_2")
        self.button_reset_linha_2.setGeometry(QRect(210, 490, 131, 31))
        self.button_reset_linha_2.setStyleSheet(u"background-color: rgb(170, 62, 43);")
        self.button_set_linha_2 = QPushButton(self.tab_config_l2)
        self.button_set_linha_2.setObjectName(u"button_set_linha_2")
        self.button_set_linha_2.setGeometry(QRect(70, 490, 131, 31))
        self.button_set_linha_2.setStyleSheet(u"background-color: rgb(66, 199, 97);")
        self.group_primeiro_t_l2 = QGroupBox(self.tab_config_l2)
        self.group_primeiro_t_l2.setObjectName(u"group_primeiro_t_l2")
        self.group_primeiro_t_l2.setGeometry(QRect(70, 10, 611, 461))
        self.group_primeiro_t_l2.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_turno_inicio_1_l2.setObjectName(u"t_turno_inicio_1_l2")
        self.t_turno_inicio_1_l2.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_intervalo_inicio_1_l2.setObjectName(u"t_intervalo_inicio_1_l2")
        self.t_intervalo_inicio_1_l2.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_intervalo_fim_1_l2.setObjectName(u"t_intervalo_fim_1_l2")
        self.t_intervalo_fim_1_l2.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_laboral_inicio_1_l2.setObjectName(u"t_laboral_inicio_1_l2")
        self.t_laboral_inicio_1_l2.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_laboral_fim_1_l2.setObjectName(u"t_laboral_fim_1_l2")
        self.t_laboral_fim_1_l2.setGeometry(QRect(330, 210, 118, 22))
        self.t_almoco_inicio_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_almoco_inicio_1_l2.setObjectName(u"t_almoco_inicio_1_l2")
        self.t_almoco_inicio_1_l2.setGeometry(QRect(190, 260, 118, 22))
        self.t_almoco_fim_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_almoco_fim_1_l2.setObjectName(u"t_almoco_fim_1_l2")
        self.t_almoco_fim_1_l2.setGeometry(QRect(330, 260, 118, 22))
        self.box_almoco_1_l2 = QCheckBox(self.group_primeiro_t_l2)
        self.box_almoco_1_l2.setObjectName(u"box_almoco_1_l2")
        self.box_almoco_1_l2.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_1_l2 = QCheckBox(self.group_primeiro_t_l2)
        self.box_laboral_1_l2.setObjectName(u"box_laboral_1_l2")
        self.box_laboral_1_l2.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_1_l2 = QCheckBox(self.group_primeiro_t_l2)
        self.box_intervalo_1_l2.setObjectName(u"box_intervalo_1_l2")
        self.box_intervalo_1_l2.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_1_l2 = QCheckBox(self.group_primeiro_t_l2)
        self.box_turno_1_l2.setObjectName(u"box_turno_1_l2")
        self.box_turno_1_l2.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_1_l2 = QLabel(self.group_primeiro_t_l2)
        self.text_inicio_1_l2.setObjectName(u"text_inicio_1_l2")
        self.text_inicio_1_l2.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_1_l2 = QLabel(self.group_primeiro_t_l2)
        self.text_fim_1_l2.setObjectName(u"text_fim_1_l2")
        self.text_fim_1_l2.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_1_l2 = QSpinBox(self.group_primeiro_t_l2)
        self.spin_meta_1_l2.setObjectName(u"spin_meta_1_l2")
        self.spin_meta_1_l2.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_1_l2.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_1_l2.setMaximum(2000)
        self.text_meta_1_l2 = QLabel(self.group_primeiro_t_l2)
        self.text_meta_1_l2.setObjectName(u"text_meta_1_l2")
        self.text_meta_1_l2.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_1_l2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_1_l2 = QLabel(self.group_primeiro_t_l2)
        self.text_temp_peca_1_l2.setObjectName(u"text_temp_peca_1_l2")
        self.text_temp_peca_1_l2.setGeometry(QRect(42, 370, 201, 21))
        self.text_temp_peca_1_l2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_1_l2 = QLabel(self.group_primeiro_t_l2)
        self.temp_peca_1_l2.setObjectName(u"temp_peca_1_l2")
        self.temp_peca_1_l2.setGeometry(QRect(200, 370, 371, 21))
        self.temp_peca_1_l2.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_1_l2 = QTimeEdit(self.group_primeiro_t_l2)
        self.t_turno_fim_1_l2.setObjectName(u"t_turno_fim_1_l2")
        self.t_turno_fim_1_l2.setGeometry(QRect(330, 110, 118, 22))
        self.tabWidget.addTab(self.tab_config_l2, "")
        self.tab_config_l3 = QWidget()
        self.tab_config_l3.setObjectName(u"tab_config_l3")
        self.button_set_linha_3 = QPushButton(self.tab_config_l3)
        self.button_set_linha_3.setObjectName(u"button_set_linha_3")
        self.button_set_linha_3.setGeometry(QRect(70, 490, 131, 31))
        self.button_set_linha_3.setStyleSheet(u"background-color: rgb(66, 199, 97);")
        self.group_segundo_t_l3 = QGroupBox(self.tab_config_l3)
        self.group_segundo_t_l3.setObjectName(u"group_segundo_t_l3")
        self.group_segundo_t_l3.setGeometry(QRect(700, 10, 601, 461))
        self.group_segundo_t_l3.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_turno_inicio_2_l3.setObjectName(u"t_turno_inicio_2_l3")
        self.t_turno_inicio_2_l3.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_intervalo_inicio_2_l3.setObjectName(u"t_intervalo_inicio_2_l3")
        self.t_intervalo_inicio_2_l3.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_intervalo_fim_2_l3.setObjectName(u"t_intervalo_fim_2_l3")
        self.t_intervalo_fim_2_l3.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_laboral_inicio_2_l3.setObjectName(u"t_laboral_inicio_2_l3")
        self.t_laboral_inicio_2_l3.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_laboral_fim_2_l3.setObjectName(u"t_laboral_fim_2_l3")
        self.t_laboral_fim_2_l3.setGeometry(QRect(330, 210, 118, 22))
        self.t_janta_inicio_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_janta_inicio_2_l3.setObjectName(u"t_janta_inicio_2_l3")
        self.t_janta_inicio_2_l3.setGeometry(QRect(190, 260, 118, 22))
        self.t_janta_fim_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_janta_fim_2_l3.setObjectName(u"t_janta_fim_2_l3")
        self.t_janta_fim_2_l3.setGeometry(QRect(330, 260, 118, 22))
        self.box_janta_2_l3 = QCheckBox(self.group_segundo_t_l3)
        self.box_janta_2_l3.setObjectName(u"box_janta_2_l3")
        self.box_janta_2_l3.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_2_l3 = QCheckBox(self.group_segundo_t_l3)
        self.box_laboral_2_l3.setObjectName(u"box_laboral_2_l3")
        self.box_laboral_2_l3.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_2_l3 = QCheckBox(self.group_segundo_t_l3)
        self.box_intervalo_2_l3.setObjectName(u"box_intervalo_2_l3")
        self.box_intervalo_2_l3.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_2_l3 = QCheckBox(self.group_segundo_t_l3)
        self.box_turno_2_l3.setObjectName(u"box_turno_2_l3")
        self.box_turno_2_l3.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_2_l3 = QLabel(self.group_segundo_t_l3)
        self.text_inicio_2_l3.setObjectName(u"text_inicio_2_l3")
        self.text_inicio_2_l3.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_2_l3 = QLabel(self.group_segundo_t_l3)
        self.text_fim_2_l3.setObjectName(u"text_fim_2_l3")
        self.text_fim_2_l3.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_2_l3 = QSpinBox(self.group_segundo_t_l3)
        self.spin_meta_2_l3.setObjectName(u"spin_meta_2_l3")
        self.spin_meta_2_l3.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_2_l3.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_2_l3.setMaximum(2000)
        self.text_meta_2_l3 = QLabel(self.group_segundo_t_l3)
        self.text_meta_2_l3.setObjectName(u"text_meta_2_l3")
        self.text_meta_2_l3.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_2_l3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_2_l3 = QLabel(self.group_segundo_t_l3)
        self.text_temp_peca_2_l3.setObjectName(u"text_temp_peca_2_l3")
        self.text_temp_peca_2_l3.setGeometry(QRect(50, 370, 201, 21))
        self.text_temp_peca_2_l3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_2_l3 = QLabel(self.group_segundo_t_l3)
        self.temp_peca_2_l3.setObjectName(u"temp_peca_2_l3")
        self.temp_peca_2_l3.setGeometry(QRect(210, 370, 371, 21))
        self.temp_peca_2_l3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_2_l3 = QTimeEdit(self.group_segundo_t_l3)
        self.t_turno_fim_2_l3.setObjectName(u"t_turno_fim_2_l3")
        self.t_turno_fim_2_l3.setGeometry(QRect(330, 110, 118, 22))
        self.button_reset_linha_3 = QPushButton(self.tab_config_l3)
        self.button_reset_linha_3.setObjectName(u"button_reset_linha_3")
        self.button_reset_linha_3.setGeometry(QRect(210, 490, 131, 31))
        self.button_reset_linha_3.setStyleSheet(u"background-color: rgb(170, 62, 43);")
        self.group_primeiro_t_l3 = QGroupBox(self.tab_config_l3)
        self.group_primeiro_t_l3.setObjectName(u"group_primeiro_t_l3")
        self.group_primeiro_t_l3.setGeometry(QRect(70, 10, 611, 461))
        self.group_primeiro_t_l3.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_turno_inicio_1_l3.setObjectName(u"t_turno_inicio_1_l3")
        self.t_turno_inicio_1_l3.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_intervalo_inicio_1_l3.setObjectName(u"t_intervalo_inicio_1_l3")
        self.t_intervalo_inicio_1_l3.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_intervalo_fim_1_l3.setObjectName(u"t_intervalo_fim_1_l3")
        self.t_intervalo_fim_1_l3.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_laboral_inicio_1_l3.setObjectName(u"t_laboral_inicio_1_l3")
        self.t_laboral_inicio_1_l3.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_laboral_fim_1_l3.setObjectName(u"t_laboral_fim_1_l3")
        self.t_laboral_fim_1_l3.setGeometry(QRect(330, 210, 118, 22))
        self.t_almoco_inicio_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_almoco_inicio_1_l3.setObjectName(u"t_almoco_inicio_1_l3")
        self.t_almoco_inicio_1_l3.setGeometry(QRect(190, 260, 118, 22))
        self.t_almoco_fim_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_almoco_fim_1_l3.setObjectName(u"t_almoco_fim_1_l3")
        self.t_almoco_fim_1_l3.setGeometry(QRect(330, 260, 118, 22))
        self.box_almoco_1_l3 = QCheckBox(self.group_primeiro_t_l3)
        self.box_almoco_1_l3.setObjectName(u"box_almoco_1_l3")
        self.box_almoco_1_l3.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_1_l3 = QCheckBox(self.group_primeiro_t_l3)
        self.box_laboral_1_l3.setObjectName(u"box_laboral_1_l3")
        self.box_laboral_1_l3.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_1_l3 = QCheckBox(self.group_primeiro_t_l3)
        self.box_intervalo_1_l3.setObjectName(u"box_intervalo_1_l3")
        self.box_intervalo_1_l3.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_1_l3 = QCheckBox(self.group_primeiro_t_l3)
        self.box_turno_1_l3.setObjectName(u"box_turno_1_l3")
        self.box_turno_1_l3.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_1_l3 = QLabel(self.group_primeiro_t_l3)
        self.text_inicio_1_l3.setObjectName(u"text_inicio_1_l3")
        self.text_inicio_1_l3.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_1_l3 = QLabel(self.group_primeiro_t_l3)
        self.text_fim_1_l3.setObjectName(u"text_fim_1_l3")
        self.text_fim_1_l3.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_1_l3 = QSpinBox(self.group_primeiro_t_l3)
        self.spin_meta_1_l3.setObjectName(u"spin_meta_1_l3")
        self.spin_meta_1_l3.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_1_l3.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_1_l3.setMaximum(2000)
        self.text_meta_1_l3 = QLabel(self.group_primeiro_t_l3)
        self.text_meta_1_l3.setObjectName(u"text_meta_1_l3")
        self.text_meta_1_l3.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_1_l3.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_1_l3 = QLabel(self.group_primeiro_t_l3)
        self.text_temp_peca_1_l3.setObjectName(u"text_temp_peca_1_l3")
        self.text_temp_peca_1_l3.setGeometry(QRect(42, 370, 201, 21))
        self.text_temp_peca_1_l3.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_1_l3 = QLabel(self.group_primeiro_t_l3)
        self.temp_peca_1_l3.setObjectName(u"temp_peca_1_l3")
        self.temp_peca_1_l3.setGeometry(QRect(200, 370, 371, 21))
        self.temp_peca_1_l3.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_1_l3 = QTimeEdit(self.group_primeiro_t_l3)
        self.t_turno_fim_1_l3.setObjectName(u"t_turno_fim_1_l3")
        self.t_turno_fim_1_l3.setGeometry(QRect(330, 110, 118, 22))
        self.tabWidget.addTab(self.tab_config_l3, "")
        self.tab_config_l4 = QWidget()
        self.tab_config_l4.setObjectName(u"tab_config_l4")
        self.button_reset_linha_4 = QPushButton(self.tab_config_l4)
        self.button_reset_linha_4.setObjectName(u"button_reset_linha_4")
        self.button_reset_linha_4.setGeometry(QRect(210, 490, 131, 31))
        self.button_reset_linha_4.setStyleSheet(u"background-color: rgb(170, 62, 43);")
        self.button_set_linha_4 = QPushButton(self.tab_config_l4)
        self.button_set_linha_4.setObjectName(u"button_set_linha_4")
        self.button_set_linha_4.setGeometry(QRect(70, 490, 131, 31))
        self.button_set_linha_4.setStyleSheet(u"background-color: rgb(66, 199, 97);")
        self.group_primeiro_t_l4 = QGroupBox(self.tab_config_l4)
        self.group_primeiro_t_l4.setObjectName(u"group_primeiro_t_l4")
        self.group_primeiro_t_l4.setGeometry(QRect(70, 10, 611, 461))
        self.group_primeiro_t_l4.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_turno_inicio_1_l4.setObjectName(u"t_turno_inicio_1_l4")
        self.t_turno_inicio_1_l4.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_intervalo_inicio_1_l4.setObjectName(u"t_intervalo_inicio_1_l4")
        self.t_intervalo_inicio_1_l4.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_intervalo_fim_1_l4.setObjectName(u"t_intervalo_fim_1_l4")
        self.t_intervalo_fim_1_l4.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_1_L4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_laboral_inicio_1_L4.setObjectName(u"t_laboral_inicio_1_L4")
        self.t_laboral_inicio_1_L4.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_laboral_fim_1_l4.setObjectName(u"t_laboral_fim_1_l4")
        self.t_laboral_fim_1_l4.setGeometry(QRect(330, 210, 118, 22))
        self.t_almoco_inicio_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_almoco_inicio_1_l4.setObjectName(u"t_almoco_inicio_1_l4")
        self.t_almoco_inicio_1_l4.setGeometry(QRect(190, 260, 118, 22))
        self.t_almoco_fim_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_almoco_fim_1_l4.setObjectName(u"t_almoco_fim_1_l4")
        self.t_almoco_fim_1_l4.setGeometry(QRect(330, 260, 118, 22))
        self.box_almoco_1_l4 = QCheckBox(self.group_primeiro_t_l4)
        self.box_almoco_1_l4.setObjectName(u"box_almoco_1_l4")
        self.box_almoco_1_l4.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_1_l4 = QCheckBox(self.group_primeiro_t_l4)
        self.box_laboral_1_l4.setObjectName(u"box_laboral_1_l4")
        self.box_laboral_1_l4.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_1_l4 = QCheckBox(self.group_primeiro_t_l4)
        self.box_intervalo_1_l4.setObjectName(u"box_intervalo_1_l4")
        self.box_intervalo_1_l4.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_1_l4 = QCheckBox(self.group_primeiro_t_l4)
        self.box_turno_1_l4.setObjectName(u"box_turno_1_l4")
        self.box_turno_1_l4.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_1_l4 = QLabel(self.group_primeiro_t_l4)
        self.text_inicio_1_l4.setObjectName(u"text_inicio_1_l4")
        self.text_inicio_1_l4.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_1_l4 = QLabel(self.group_primeiro_t_l4)
        self.text_fim_1_l4.setObjectName(u"text_fim_1_l4")
        self.text_fim_1_l4.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_1_L4 = QSpinBox(self.group_primeiro_t_l4)
        self.spin_meta_1_L4.setObjectName(u"spin_meta_1_L4")
        self.spin_meta_1_L4.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_1_L4.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_1_L4.setMaximum(2000)
        self.text_meta_1_l4 = QLabel(self.group_primeiro_t_l4)
        self.text_meta_1_l4.setObjectName(u"text_meta_1_l4")
        self.text_meta_1_l4.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_1_l4.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_1_l4 = QLabel(self.group_primeiro_t_l4)
        self.text_temp_peca_1_l4.setObjectName(u"text_temp_peca_1_l4")
        self.text_temp_peca_1_l4.setGeometry(QRect(42, 370, 201, 21))
        self.text_temp_peca_1_l4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_1_l4 = QLabel(self.group_primeiro_t_l4)
        self.temp_peca_1_l4.setObjectName(u"temp_peca_1_l4")
        self.temp_peca_1_l4.setGeometry(QRect(200, 370, 371, 21))
        self.temp_peca_1_l4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_1_l4 = QTimeEdit(self.group_primeiro_t_l4)
        self.t_turno_fim_1_l4.setObjectName(u"t_turno_fim_1_l4")
        self.t_turno_fim_1_l4.setGeometry(QRect(330, 110, 118, 22))
        self.group_segundo_t_l4 = QGroupBox(self.tab_config_l4)
        self.group_segundo_t_l4.setObjectName(u"group_segundo_t_l4")
        self.group_segundo_t_l4.setGeometry(QRect(700, 10, 601, 461))
        self.group_segundo_t_l4.setStyleSheet(u"background-color: rgb(134, 134, 134);")
        self.t_turno_inicio_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_turno_inicio_2_l4.setObjectName(u"t_turno_inicio_2_l4")
        self.t_turno_inicio_2_l4.setGeometry(QRect(190, 110, 118, 22))
        self.t_intervalo_inicio_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_intervalo_inicio_2_l4.setObjectName(u"t_intervalo_inicio_2_l4")
        self.t_intervalo_inicio_2_l4.setGeometry(QRect(190, 160, 118, 22))
        self.t_intervalo_fim_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_intervalo_fim_2_l4.setObjectName(u"t_intervalo_fim_2_l4")
        self.t_intervalo_fim_2_l4.setGeometry(QRect(330, 160, 118, 22))
        self.t_laboral_inicio_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_laboral_inicio_2_l4.setObjectName(u"t_laboral_inicio_2_l4")
        self.t_laboral_inicio_2_l4.setGeometry(QRect(190, 210, 118, 22))
        self.t_laboral_fim_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_laboral_fim_2_l4.setObjectName(u"t_laboral_fim_2_l4")
        self.t_laboral_fim_2_l4.setGeometry(QRect(330, 210, 118, 22))
        self.t_janta_inicio_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_janta_inicio_2_l4.setObjectName(u"t_janta_inicio_2_l4")
        self.t_janta_inicio_2_l4.setGeometry(QRect(190, 260, 118, 22))
        self.t_janta_fim_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_janta_fim_2_l4.setObjectName(u"t_janta_fim_2_l4")
        self.t_janta_fim_2_l4.setGeometry(QRect(330, 260, 118, 22))
        self.box_janta_2_l4 = QCheckBox(self.group_segundo_t_l4)
        self.box_janta_2_l4.setObjectName(u"box_janta_2_l4")
        self.box_janta_2_l4.setGeometry(QRect(60, 260, 91, 20))
        self.box_laboral_2_l4 = QCheckBox(self.group_segundo_t_l4)
        self.box_laboral_2_l4.setObjectName(u"box_laboral_2_l4")
        self.box_laboral_2_l4.setGeometry(QRect(60, 210, 101, 20))
        self.box_intervalo_2_l4 = QCheckBox(self.group_segundo_t_l4)
        self.box_intervalo_2_l4.setObjectName(u"box_intervalo_2_l4")
        self.box_intervalo_2_l4.setGeometry(QRect(60, 160, 111, 20))
        self.box_turno_2_l4 = QCheckBox(self.group_segundo_t_l4)
        self.box_turno_2_l4.setObjectName(u"box_turno_2_l4")
        self.box_turno_2_l4.setGeometry(QRect(60, 110, 91, 20))
        self.text_inicio_2_l4 = QLabel(self.group_segundo_t_l4)
        self.text_inicio_2_l4.setObjectName(u"text_inicio_2_l4")
        self.text_inicio_2_l4.setGeometry(QRect(230, 90, 49, 16))
        self.text_fim_2_l4 = QLabel(self.group_segundo_t_l4)
        self.text_fim_2_l4.setObjectName(u"text_fim_2_l4")
        self.text_fim_2_l4.setGeometry(QRect(370, 90, 49, 16))
        self.spin_meta_2_l4 = QSpinBox(self.group_segundo_t_l4)
        self.spin_meta_2_l4.setObjectName(u"spin_meta_2_l4")
        self.spin_meta_2_l4.setGeometry(QRect(190, 40, 101, 22))
        self.spin_meta_2_l4.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.spin_meta_2_l4.setMaximum(2000)
        self.text_meta_2_l4 = QLabel(self.group_segundo_t_l4)
        self.text_meta_2_l4.setObjectName(u"text_meta_2_l4")
        self.text_meta_2_l4.setGeometry(QRect(50, 40, 141, 21))
        self.text_meta_2_l4.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")
        self.text_temp_peca_2_l4 = QLabel(self.group_segundo_t_l4)
        self.text_temp_peca_2_l4.setObjectName(u"text_temp_peca_2_l4")
        self.text_temp_peca_2_l4.setGeometry(QRect(50, 370, 201, 21))
        self.text_temp_peca_2_l4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.temp_peca_2_l4 = QLabel(self.group_segundo_t_l4)
        self.temp_peca_2_l4.setObjectName(u"temp_peca_2_l4")
        self.temp_peca_2_l4.setGeometry(QRect(210, 370, 371, 21))
        self.temp_peca_2_l4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.t_turno_fim_2_l4 = QTimeEdit(self.group_segundo_t_l4)
        self.t_turno_fim_2_l4.setObjectName(u"t_turno_fim_2_l4")
        self.t_turno_fim_2_l4.setGeometry(QRect(330, 110, 118, 22))
        self.tabWidget.addTab(self.tab_config_l4, "")
        self.tab_relatorio = QWidget()
        self.tab_relatorio.setObjectName(u"tab_relatorio")
        self.calendarWidget = QCalendarWidget(self.tab_relatorio)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(400, 50, 581, 361))
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setTabletTracking(False)
        self.calendarWidget.setStyleSheet(u"background-color: rgb(167, 167, 167);")
        self.calendarWidget.setMinimumDate(QDate(2023, 1, 1))
        self.calendarWidget.setMaximumDate(QDate(2024, 12, 31))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.pushButton_2 = QPushButton(self.tab_relatorio)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 480, 151, 41))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(121, 121, 121);")
        self.tabWidget.addTab(self.tab_relatorio, "")
        self.text_status_servidor = QLabel(self.centralwidget)
        self.text_status_servidor.setObjectName(u"text_status_servidor")
        self.text_status_servidor.setGeometry(QRect(1210, 0, 141, 21))
        self.text_status_servidor.setStyleSheet(u"background-color: rgb(0, 1, 1);")
        self.status_servidor = QLabel(self.centralwidget)
        self.status_servidor.setObjectName(u"status_servidor")
        self.status_servidor.setGeometry(QRect(1220, 20, 101, 20))
        self.status_servidor.setStyleSheet(u"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(0, 1, 1);\n"
"color: rgb(203, 0, 0);\n"
"")
        self.msg_box_name = QMessageBox()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1578, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


    # inicia objeto self.time responsável por atualizar a interface com respectivo tempo de 500ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_interface)

        self.timer.start(200)
        self.elapsed_timer = QElapsedTimer()
        self.elapsed_timer.start()
        self.counter1 = 0
        self.counter2 = 0

    #eventos de botões para setar e resetar contagem de tempo das linhas
        self.button_set_linha_1.clicked.connect(self.press_botao_set_linha_1)
        self.button_reset_linha_1.clicked.connect(self.press_botao_reset_linha_1)
        self.button_set_linha_2.clicked.connect(self.press_botao_set_linha_2)
        self.button_reset_linha_2.clicked.connect(self.press_botao_reset_linha_2)
        self.button_set_linha_3.clicked.connect(self.press_botao_set_linha_3)
        self.button_reset_linha_3.clicked.connect(self.press_botao_reset_linha_3)
        self.button_set_linha_4.clicked.connect(self.press_botao_set_linha_4)
        self.button_reset_linha_4.clicked.connect(self.press_botao_reset_linha_4)
        self.pushButton_2.clicked.connect(self.gerar_relatorio)



        QMetaObject.connectSlotsByName(MainWindow)


















    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.text_est_l1.setText(QCoreApplication.translate("MainWindow", u"Estanquiedade", None))
        self.text_pre_l1.setText(QCoreApplication.translate("MainWindow", u"Pressuriza\u00e7\u00e3o", None))
        self.text_hypot_l1.setText(QCoreApplication.translate("MainWindow", u"Hypot", None))
        self.text_mesa_l1.setText(QCoreApplication.translate("MainWindow", u"Mesa de Montagem", None))
        self.label_status_l1.setText(QCoreApplication.translate("MainWindow", u"Status Linha ", None))
        self.status_l1.setText(QCoreApplication.translate("MainWindow", u"Parada", None))
        self.text_cont_p_l1.setText(QCoreApplication.translate("MainWindow", u"Contagem Projetada", None))
        self.group_apr_l1.setTitle(QCoreApplication.translate("MainWindow", u"Aprovado", None))
        self.group_rep_l1.setTitle(QCoreApplication.translate("MainWindow", u"Reprovado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linha_1), QCoreApplication.translate("MainWindow", u"Linha 1", None))
        self.status_l2.setText(QCoreApplication.translate("MainWindow", u"Parada", None))
        self.text_mesa_l2.setText(QCoreApplication.translate("MainWindow", u"Mesa de Montagem", None))
        self.text_pre_l2.setText(QCoreApplication.translate("MainWindow", u"Pressuriza\u00e7\u00e3o", None))
        self.text_est_l2.setText(QCoreApplication.translate("MainWindow", u"Estanquiedade", None))
        self.text_cont_p_l2.setText(QCoreApplication.translate("MainWindow", u"Contagem Projetada", None))
        self.group_rep_l2.setTitle(QCoreApplication.translate("MainWindow", u"Reprovado", None))
        self.label_status_l2.setText(QCoreApplication.translate("MainWindow", u"Status Linha ", None))
        self.text_hy_l2.setText(QCoreApplication.translate("MainWindow", u"Hypot", None))
        self.group_apr_l2.setTitle(QCoreApplication.translate("MainWindow", u"Aprovado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linha_2), QCoreApplication.translate("MainWindow", u"Linha 2", None))
        self.text_mesa_l3.setText(QCoreApplication.translate("MainWindow", u"Mesa de Montagem", None))
        self.text_est_l3.setText(QCoreApplication.translate("MainWindow", u"Estanquiedade", None))
        self.group_apr_l3.setTitle(QCoreApplication.translate("MainWindow", u"Aprovado", None))
        self.status_l3.setText(QCoreApplication.translate("MainWindow", u"Parada", None))
        self.text_hy_l3.setText(QCoreApplication.translate("MainWindow", u"Hypot", None))
        self.label_status_l3.setText(QCoreApplication.translate("MainWindow", u"Status Linha ", None))
        self.group_rep_l3.setTitle(QCoreApplication.translate("MainWindow", u"Reprovado", None))
        self.text_cont_p_l3.setText(QCoreApplication.translate("MainWindow", u"Contagem Projetada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linha_3), QCoreApplication.translate("MainWindow", u"Linha 3", None))
        self.text_cont_p_l4.setText(QCoreApplication.translate("MainWindow", u"Contagem Projetada", None))
        self.label_status_l4.setText(QCoreApplication.translate("MainWindow", u"Status Linha ", None))
        self.group_apr_l4.setTitle(QCoreApplication.translate("MainWindow", u"Aprovado", None))
        self.group_rep_l4.setTitle(QCoreApplication.translate("MainWindow", u"Reprovado", None))
        self.text_mesa_l4.setText(QCoreApplication.translate("MainWindow", u"Mesa de Montagem", None))
        self.text_est_l4.setText(QCoreApplication.translate("MainWindow", u"Estanquiedade", None))
        self.text_hy_l4.setText(QCoreApplication.translate("MainWindow", u"Hypot", None))
        self.status_l4.setText(QCoreApplication.translate("MainWindow", u"Parada", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_linha_4), QCoreApplication.translate("MainWindow", u"Linha 4", None))
        self.group_primeiro_t_l1.setTitle(QCoreApplication.translate("MainWindow", u"Primeiro Turno", None))
        self.box_almoco_1_l1.setText(QCoreApplication.translate("MainWindow", u"Almoco", None))
        self.box_laboral_1_l1.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_1_l1.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_1_l1.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_1_l1.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_1_l1.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_1_l1.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_1_l1.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_1_l1.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.group_segundo_t_l1.setTitle(QCoreApplication.translate("MainWindow", u"Segundo Turno", None))
        self.box_janta_2_l1.setText(QCoreApplication.translate("MainWindow", u"Janta", None))
        self.box_laboral_2_l1.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_2_l1.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_2_l1.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_2_l1.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_2_l1.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_2_l1.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_2_l1.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_2_l1.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.button_set_linha_1.setText(QCoreApplication.translate("MainWindow", u"Setar Linha 1", None))
        self.button_reset_linha_1.setText(QCoreApplication.translate("MainWindow", u"Reset Linha 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config_l1), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o L1", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Segundo Turno", None))
        self.box_janta_2_l2.setText(QCoreApplication.translate("MainWindow", u"Janta", None))
        self.box_laboral_2_l2.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_2_l2.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_2_l2.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_2_l2.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_2_l2.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_2_l2.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_2_l2.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_2_l2.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.button_reset_linha_2.setText(QCoreApplication.translate("MainWindow", u"Reset Linha 2", None))
        self.button_set_linha_2.setText(QCoreApplication.translate("MainWindow", u"Setar Linha 2", None))
        self.group_primeiro_t_l2.setTitle(QCoreApplication.translate("MainWindow", u"Primeiro Turno", None))
        self.box_almoco_1_l2.setText(QCoreApplication.translate("MainWindow", u"Almoco", None))
        self.box_laboral_1_l2.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_1_l2.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_1_l2.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_1_l2.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_1_l2.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_1_l2.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_1_l2.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_1_l2.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config_l2), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o L2", None))
        self.button_set_linha_3.setText(QCoreApplication.translate("MainWindow", u"Setar Linha 3", None))
        self.group_segundo_t_l3.setTitle(QCoreApplication.translate("MainWindow", u"Segundo Turno", None))
        self.box_janta_2_l3.setText(QCoreApplication.translate("MainWindow", u"Janta", None))
        self.box_laboral_2_l3.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_2_l3.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_2_l3.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_2_l3.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_2_l3.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_2_l3.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_2_l3.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_2_l3.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.button_reset_linha_3.setText(QCoreApplication.translate("MainWindow", u"Reset Linha 3", None))
        self.group_primeiro_t_l3.setTitle(QCoreApplication.translate("MainWindow", u"Primeiro Turno", None))
        self.box_almoco_1_l3.setText(QCoreApplication.translate("MainWindow", u"Almoco", None))
        self.box_laboral_1_l3.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_1_l3.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_1_l3.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_1_l3.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_1_l3.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_1_l3.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_1_l3.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_1_l3.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config_l3), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o L3", None))
        self.button_reset_linha_4.setText(QCoreApplication.translate("MainWindow", u"Reset Linha 4", None))
        self.button_set_linha_4.setText(QCoreApplication.translate("MainWindow", u"Setar Linha 4", None))
        self.group_primeiro_t_l4.setTitle(QCoreApplication.translate("MainWindow", u"Primeiro Turno", None))
        self.box_almoco_1_l4.setText(QCoreApplication.translate("MainWindow", u"Almoco", None))
        self.box_laboral_1_l4.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_1_l4.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_1_l4.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_1_l4.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_1_l4.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_1_l4.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_1_l4.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_1_l4.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.group_segundo_t_l4.setTitle(QCoreApplication.translate("MainWindow", u"Segundo Turno", None))
        self.box_janta_2_l4.setText(QCoreApplication.translate("MainWindow", u"Janta", None))
        self.box_laboral_2_l4.setText(QCoreApplication.translate("MainWindow", u"Laboral", None))
        self.box_intervalo_2_l4.setText(QCoreApplication.translate("MainWindow", u"Intervalo", None))
        self.box_turno_2_l4.setText(QCoreApplication.translate("MainWindow", u"Turno", None))
        self.text_inicio_2_l4.setText(QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.text_fim_2_l4.setText(QCoreApplication.translate("MainWindow", u"Fim", None))
        self.text_meta_2_l4.setText(QCoreApplication.translate("MainWindow", u"Meta de Pecas", None))
        self.text_temp_peca_2_l4.setText(QCoreApplication.translate("MainWindow", u"Tempo por Peca =", None))
        self.temp_peca_2_l4.setText(QCoreApplication.translate("MainWindow", u" 0 s", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config_l4), QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o L4", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Gerar Relatorio ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_relatorio), QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.text_status_servidor.setText(QCoreApplication.translate("MainWindow", u"Status Servidor", None))
        self.status_servidor.setText(QCoreApplication.translate("MainWindow", u"Conectando ...", None))

    # retranslateUi


    def gerar_relatorio(self):

        gerar_relatorio_manual(self.calendarWidget.selectedDate())


    def gravar_banco_de_dados(self):

                Data_Horario = datetime.datetime.now()

                data_dia = Data_Horario.strftime('-%Y-%m-%d')

                Data_Horario = Data_Horario.strftime('%Y-%m-%d %H:%M:%S')

                Registro = "Registro" + data_dia + ".db"

                conn = sqlite3.connect(Registro)
                cursor = conn.cursor()

                # Criando uma tabela
                cursor.execute('''CREATE TABLE IF NOT EXISTS leituras (
                        id INTEGER PRIMARY KEY,
                        data TEXT,
                        contagem_projetada_l1 INTEGER,
                        mesa_l1 INTEGER,
                        estanquiedade_ap_l1 INTEGER,
                        estanquiedade_rep_l1 INTEGER,
                        pressurizacao_ap_l1 INTEGER,
                        pressurizacao_rep_l1 INTEGER,
                        hypot_ap_l1 INTEGER,
                        hypot_rep_l1 INTEGER,
                        contagem_projetada_l2 INTEGER,
                        mesa_l2 INTEGER,
                        estanquiedade_ap_l2 INTEGER,
                        estanquiedade_rep_l2 INTEGER,
                        pressurizacao_ap_l2 INTEGER,
                        pressurizacao_rep_l2 INTEGER,
                        hypot_ap_l2 INTEGER,
                        hypot_rep_l2 INTEGER,
                        contagem_projetada_l3 INTEGER,
                        mesa_l3 INTEGER,
                        estanquiedade_ap_l3 INTEGER,
                        estanquiedade_rep_l3 INTEGER,
                        hypot_ap_l3 INTEGER,
                        hypot_rep_l3 INTEGER,
                        contagem_projetada_l4 INTEGER,
                        mesa_l4 INTEGER,
                        estanquiedade_ap_l4 INTEGER,
                        estanquiedade_rep_l4 INTEGER,
                        hypot_ap_l4 INTEGER,
                        hypot_rep_l4 INTEGER)''')

                # Inserindo dados na tabela
                dados_linhas = (
                Data_Horario, self.contagem_projetada_l1, self.Mesa_de_Montagem_L1, self.Estanquiedade_Aprovadas_L1,
                self.Estanquiedade_Reprovadas_L1, self.Pressurizacao_Aprovadas_L1, self.Pressurizacao_Reprovadas_L1,
                self.Hypot_Aprovadas_L1, self.Hypot_Reprovadas_L1, self.contagem_projetada_l2, self.Mesa_de_Montagem_L2,
                self.Estanquiedade_Aprovadas_L2, self.Estanquiedade_Reprovadas_L2, self.Pressurizacao_Aprovadas_L2,
                self.Pressurizacao_Reprovadas_L2,
                self.Hypot_Aprovadas_L2, self.Hypot_Reprovadas_L2, self.contagem_projetada_l3, self.Mesa_de_Montagem_L3,
                self.Estanquiedade_Aprovadas_L3, self.Estanquiedade_Reprovadas_L3, self.Hypot_Aprovadas_L3,
                self.Hypot_Reprovadas_L3,
                self.contagem_projetada_l4, self.Mesa_de_Montagem_L4, self.Estanquiedade_Aprovadas_L4,
                self.Estanquiedade_Reprovadas_L4,
                self.Hypot_Aprovadas_L4, self.Hypot_Reprovadas_L4
                )
                cursor.execute(
                        'INSERT INTO leituras (data, contagem_projetada_l1, mesa_l1, estanquiedade_ap_l1, estanquiedade_rep_l1, pressurizacao_ap_l1, pressurizacao_rep_l1, hypot_ap_l1, hypot_rep_l1,'
                        'contagem_projetada_l2, mesa_l2, estanquiedade_ap_l2, estanquiedade_rep_l2, pressurizacao_ap_l2, pressurizacao_rep_l2, hypot_ap_l2, hypot_rep_l2,'
                        'contagem_projetada_l3, mesa_l3, estanquiedade_ap_l3, estanquiedade_rep_l3, hypot_ap_l3, hypot_rep_l3,'
                        'contagem_projetada_l4, mesa_l4, estanquiedade_ap_l4, estanquiedade_rep_l4, hypot_ap_l4, hypot_rep_l4) '
                        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? )',
                        dados_linhas)

                # Fazendo commit das alterações e fechando a conexão
                conn.commit()
                conn.close()
                print("Gravado Banco de Dados")

    def show_info_messagebox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)





        def alerta_tempo_anormal():

                print("Parametros de tempo anormal")

                msg.setText("Parâmetros de tempo inaceitáveis, verifique novamente. ")

                        # setting Message box window title
                msg.setWindowTitle("Aviso")

                        # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok )

                        # start the app
                retval = msg.exec_()

                self.inicio_turno_l1 = None
                self.final_turno_l1 = None
                self.inicio_intervalo_l1 = None
                self.final_intervalo_l1 = None
                self.inicio_laboral_l1 = None
                self.final_laboral_l1 = None
                self.inicio_almoco_l1 = None
                self.final_laboral_l1 = None

                self.inicio_turno_l1_2 = None
                self.final_turno_l1_2 = None
                self.inicio_intervalo_l1_2 = None
                self.final_intervalo_l1_2 = None
                self.inicio_laboral_l1_2 = None
                self.final_laboral_l1_2 = None
                self.inicio_janta_l1 = None
                self.final_janta_l1 = None

                self.primeiro_turno_start = False
                self.segundo_turno_start = False


                self.estado_controle_sistema_linha_1 = False
                self.sistema_iniciado_linha_1 = False
                self.sistema_ativado_l1 = False

                self.meta_linha_1_manha_registro = 0
                self.meta_linha_1 = 0

                self.meta_linha_1_tarde_registro = 0
                self.meta_linha_1_tarde = 0

                self.tempo_estimado_por_peca_l1_1 = 0
                self.tempo_estimado_por_peca_l1_2 = 0

                self.temp_peca_1_l1.setText(f'{str(self.tempo_estimado_por_peca_l1_1)} (s)')
                self.temp_peca_2_l1.setText(f'{str(self.tempo_estimado_por_peca_l1_2)} (s)')




        def alerta_tempo_anormal_l2():

                print("Parametros de tempo anormal")

                msg.setText("Parâmetros de tempo inaceitáveis, verifique novamente. ")

                        # setting Message box window title
                msg.setWindowTitle("Aviso")

                        # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok )

                        # start the app
                retval = msg.exec_()

                self.inicio_turno_l2 = None
                self.final_turno_l2 = None
                self.inicio_intervalo_l2 = None
                self.final_intervalo_l2 = None
                self.inicio_laboral_l2 = None
                self.final_laboral_l2 = None
                self.inicio_almoco_l2 = None
                self.final_laboral_l2 = None

                self.inicio_turno_l2_2 = None
                self.final_turno_l2_2 = None
                self.inicio_intervalo_l2_2 = None
                self.final_intervalo_l2_2 = None
                self.inicio_laboral_l2_2 = None
                self.final_laboral_l2_2 = None
                self.inicio_janta_l2 = None
                self.final_janta_l2 = None

                self.primeiro_turno_start_l2 = False
                self.segundo_turno_start_l2 = False


                self.estado_controle_sistema_linha_2 = False
                self.sistema_iniciado_linha_2 = False
                self.sistema_ativado_l2 = False

                self.meta_linha_2_tarde_registro = 0
                self.meta_linha_2_tarde = 0
                self.meta_linha_2 = 0
                self.meta_linha_2_manha_registro = 0

                self.tempo_estimado_por_peca_l2_1 = 0
                self.tempo_estimado_por_peca_l2_2 = 0

                self.temp_peca_1_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_1)} (s)')
                self.temp_peca_2_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_2)} (s)')



        def alerta_tempo_anormal_l3():

                print("Parametros de tempo anormal")

                msg.setText("Parâmetros de tempo inaceitáveis, verifique novamente. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()

                self.inicio_turno_l3 = None
                self.final_turno_l3 = None
                self.inicio_intervalo_l3 = None
                self.final_intervalo_l3 = None
                self.inicio_laboral_l3 = None
                self.final_laboral_l3 = None
                self.inicio_almoco_l3 = None
                self.final_laboral_l3 = None

                self.inicio_turno_l3_2 = None
                self.final_turno_l3_2 = None
                self.inicio_intervalo_l3_2 = None
                self.final_intervalo_l3_2 = None
                self.inicio_laboral_l3_2 = None
                self.final_laboral_l3_2 = None
                self.inicio_janta_l3 = None
                self.final_janta_l3 = None

                self.primeiro_turno_start_l3 = False
                self.segundo_turno_start_l3 = False

                self.estado_controle_sistema_linha_3 = False
                self.sistema_iniciado_linha_3 = False
                self.sistema_ativado_l3 = False

                self.meta_linha_3_tarde_registro = 0
                self.meta_linha_3_tarde = 0
                self.meta_linha_3 = 0
                self.meta_linha_3_manha_registro = 0

                self.tempo_estimado_por_peca_l3_1 = 0
                self.tempo_estimado_por_peca_l3_2 = 0

                self.temp_peca_1_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_1)} (s)')
                self.temp_peca_2_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_2)} (s)')


        def alerta_tempo_anormal_l4():

                print("Parametros de tempo anormal")

                msg.setText("Parâmetros de tempo inaceitáveis, verifique novamente. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()

                self.inicio_turno_l4 = None
                self.final_turno_l4 = None
                self.inicio_intervalo_l4 = None
                self.final_intervalo_l4 = None
                self.inicio_laboral_l4 = None
                self.final_laboral_l4 = None
                self.inicio_almoco_l4 = None
                self.final_laboral_l4 = None

                self.inicio_turno_l4_2 = None
                self.final_turno_l4_2 = None
                self.inicio_intervalo_l4_2 = None
                self.final_intervalo_l4_2 = None
                self.inicio_laboral_l4_2 = None
                self.final_laboral_l4_2 = None
                self.inicio_janta_l4 = None
                self.final_janta_l4 = None

                self.primeiro_turno_start_l4 = False
                self.segundo_turno_start_l4 = False

                self.estado_controle_sistema_linha_4 = False
                self.sistema_iniciado_linha_4 = False
                self.sistema_ativado_l4 = False

                self.meta_linha_4_tarde_registro = 0
                self.meta_linha_4_tarde = 0
                self.meta_linha_4 = 0
                self.meta_linha_4_manha_registro = 0

                self.tempo_estimado_por_peca_l4_1 = 0
                self.tempo_estimado_por_peca_l4_2 = 0

                self.temp_peca_1_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_1)} (s)')
                self.temp_peca_2_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_2)} (s)')







        def alerta_linha_1_rodando():





                msg.setText("O sistema da linha 1 está ativado, para alterar os parâmetros de tempo é preciso resetar o sistema de forma. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()



        def alerta_linha_2_rodando():



                msg.setText("O sistema da LINHA 2 está ativado, para alterar os parâmetros de tempo é preciso resetar o sistema de forma. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()


        def alerta_linha_3_rodando():



                msg.setText("O sistema da LINHA 3 está ativado, para alterar os parâmetros de tempo é preciso resetar o sistema de forma. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()



        def alerta_linha_4_rodando():



                msg.setText("O sistema da LINHA 4 está ativado, para alterar os parâmetros de tempo é preciso resetar o sistema de forma. ")

                # setting Message box window title
                msg.setWindowTitle("Aviso")

                # declaring buttons on Message Box
                msg.setStandardButtons(QMessageBox.Ok)

                # start the app
                retval = msg.exec_()





        if (self.box_turno_1_l1.isChecked()):

                if (self.tempo_estimado_por_peca_l1_1 > 40 or self.tempo_estimado_por_peca_l1_1 < 1):
                        alerta_tempo_anormal()

        if (self.box_turno_2_l1.isChecked()):

                if (self.tempo_estimado_por_peca_l1_2 > 40 or self.tempo_estimado_por_peca_l1_2 < 1):
                        alerta_tempo_anormal()


        if (self.box_turno_1_l2.isChecked()):

                if (self.tempo_estimado_por_peca_l2_1 > 40 or self.tempo_estimado_por_peca_l2_1 < 1):
                        alerta_tempo_anormal_l2()

        if (self.box_turno_2_l2.isChecked()):

                if (self.tempo_estimado_por_peca_l2_2 > 40 or self.tempo_estimado_por_peca_l2_2 < 1):
                        alerta_tempo_anormal_l2()



        if (self.box_turno_1_l3.isChecked()):

                if (self.tempo_estimado_por_peca_l3_1 > 40 or self.tempo_estimado_por_peca_l3_1 < 1):
                        alerta_tempo_anormal_l3()

        if (self.box_turno_2_l3.isChecked()):

                if (self.tempo_estimado_por_peca_l3_2 > 40 or self.tempo_estimado_por_peca_l3_2 < 1):
                        alerta_tempo_anormal_l3()


        if (self.box_turno_1_l4.isChecked()):

                if (self.tempo_estimado_por_peca_l4_1 > 40 or self.tempo_estimado_por_peca_l4_1 < 1):
                        alerta_tempo_anormal_l4()

        if (self.box_turno_2_l4.isChecked()):

                if (self.tempo_estimado_por_peca_l4_2 > 40 or self.tempo_estimado_por_peca_l4_2 < 1):
                        alerta_tempo_anormal_l4()



        if (self.sistema_iniciado_linha_1 == True ):
                alerta_linha_1_rodando()


        if (self.sistema_iniciado_linha_2 == True ):
                alerta_linha_2_rodando()


        if (self.sistema_iniciado_linha_3 == True ):
                alerta_linha_3_rodando()


        if (self.sistema_iniciado_linha_4 == True ):
                alerta_linha_4_rodando()





    def press_botao_set_linha_1(self):



            if (self.sistema_iniciado_linha_1 == False):

                    print("Horarios Setados")

                    ###### 1 Turno ######



                    self.inicio_turno_l1 = None
                    self.final_turno_l1 = None
                    self.inicio_intervalo_l1 = None
                    self.final_intervalo_l1 = None
                    self.inicio_laboral_l1 = None
                    self.final_laboral_l1 = None
                    self.inicio_almoco_l1 = None
                    self.final_almoco_l1 = None
                    self.primeiro_turno_start = False
                    self.estado_controle_sistema_linha_1 = False





                    if self.box_turno_1_l1.isChecked():



                            self.inicio_turno_l1 = self.t_turno_inicio_1_l1.time().toString()
                            self.final_turno_l1 = self.t_turno_fim_1_l1.time().toString()

                            print(self.inicio_turno_l1)

                            inicio_turno_l1_conversao_min = int(self.inicio_turno_l1[:2]) * 60
                            inicio_turno_l1_total_min = inicio_turno_l1_conversao_min + int(self.inicio_turno_l1[3:5])

                            final_turno_l1_conversao_min = int(self.final_turno_l1[:2]) * 60
                            final_turno_l1_total_min = final_turno_l1_conversao_min + int(self.final_turno_l1[3:5])

                            horas_trabalhadas_turno_manha_l1 = final_turno_l1_total_min - inicio_turno_l1_total_min

                            if self.box_intervalo_1_l1.isChecked():

                                    self.inicio_intervalo_l1 = self.t_intervalo_inicio_1_l1.time().toString()
                                    self.final_intervalo_l1 = self.t_intervalo_fim_1_l1.time().toString()

                                    inicio_intervalo_l1_conversao_min = int(self.inicio_intervalo_l1[:2]) * 60
                                    inicio_intervalo_l1_total_min = inicio_intervalo_l1_conversao_min + int(
                                            self.inicio_intervalo_l1[3:5])

                                    final_intervalo_l1_conversao_min = int(self.final_intervalo_l1[:2]) * 60
                                    final_intervalo_l1_total_min = final_intervalo_l1_conversao_min + int(
                                            self.final_intervalo_l1[3:5])

                                    turno_manhã_intervalo_l1 = final_intervalo_l1_total_min - inicio_intervalo_l1_total_min

                                    horas_trabalhadas_turno_manha_l1 = horas_trabalhadas_turno_manha_l1 - turno_manhã_intervalo_l1

                            if self.box_laboral_1_l1.isChecked():

                                    self.inicio_laboral_l1 = self.t_laboral_inicio_1_l1.time().toString()
                                    self.final_laboral_l1 = self.t_laboral_fim_1_l1.time().toString()



                                    inicio_laboral_l1_conversao_min = int(self.inicio_laboral_l1[:2]) * 60
                                    inicio_laboral_l1_total_min = inicio_laboral_l1_conversao_min + int(
                                            self.inicio_laboral_l1[3:5])

                                    final_laboral_l1_conversao_min = int(self.final_laboral_l1[:2]) * 60
                                    final_laboral_l1_total_min = final_laboral_l1_conversao_min + int(self.final_laboral_l1[3:5])

                                    turno_manha_laboral_l1 = final_laboral_l1_total_min - inicio_laboral_l1_total_min



                                    horas_trabalhadas_turno_manha_l1 = horas_trabalhadas_turno_manha_l1 - turno_manha_laboral_l1

                            if self.box_almoco_1_l1.isChecked():
                                    self.inicio_almoco_l1 = self.t_almoco_inicio_1_L1.time().toString()
                                    self.final_almoco_l1 = self.t_almoco_fim_1_l1.time().toString()

                                    inicio_almoco_l1_conversao_min = int(self.inicio_almoco_l1[:2]) * 60
                                    inicio_almoco_l1_total_min = inicio_almoco_l1_conversao_min + int(self.inicio_almoco_l1[3:5])

                                    final_almoco_l1_conversao_min = int(self.final_almoco_l1[:2]) * 60
                                    final_almoco_l1_total_min = final_almoco_l1_conversao_min + int(
                                            self.final_almoco_l1[3:5])
                                    turno_manha_almoco_l1 = final_almoco_l1_total_min - inicio_almoco_l1_total_min

                                    print(turno_manha_almoco_l1)

                                    horas_trabalhadas_turno_manha_l1 = horas_trabalhadas_turno_manha_l1 - turno_manha_almoco_l1



                            self.meta_linha_1 = self.spin_meta_1_l1.value()
                            self.meta_linha_1 = int(self.meta_linha_1)
                            self.meta_linha_1_manha_registro = self.meta_linha_1

                            self.horas_trabalhadas_turno_manha_l1_segundos = horas_trabalhadas_turno_manha_l1 * 60

                            self.tempo_estimado_por_peca_l1_1 = round((self.horas_trabalhadas_turno_manha_l1_segundos / self.meta_linha_1_manha_registro),2)

                            self.temp_peca_1_l1.setText(f'{str(self.tempo_estimado_por_peca_l1_1)} (s)')

                            self.sistema_ativado_l1 = True
                            self.sistema_iniciado_linha_1 = False
                            self.contagem_projetada_linha_1 = 0














                    ###### 2 Turno #####


                    self.inicio_turno_l1_2 = None
                    self.final_turno_l1_2 = None
                    self.inicio_intervalo_l1_2 = None
                    self.final_intervalo_l1_2 = None
                    self.inicio_laboral_l1_2 = None
                    self.final_laboral_l1_2 = None
                    self.inicio_janta_l1 = None
                    self.final_janta_l1 = None
                    self.segundo_turno_start = False



                    if self.box_turno_2_l1.isChecked():



                            self.inicio_turno_l1_2 = self.t_turno_inicio_2_l1.time().toString()
                            self.final_turno_l1_2 = self.t_turno_fim_2_l1.time().toString()

                            print(self.inicio_turno_l1_2)

                            inicio_turno_l1_2_conversao_min = int(self.inicio_turno_l1_2[:2]) * 60
                            inicio_turno_l1_2_total_min = inicio_turno_l1_2_conversao_min + int(self.inicio_turno_l1_2[3:5])

                            final_turno_l1_2_conversao_min = int(self.final_turno_l1_2[:2]) * 60
                            final_turno_l1_2_total_min = final_turno_l1_2_conversao_min + int(self.final_turno_l1_2[3:5])

                            horas_trabalhadas_turno_tarde_l1 = final_turno_l1_2_total_min - inicio_turno_l1_2_total_min

                            if self.box_intervalo_2_l1.isChecked():

                                    self.inicio_intervalo_l1_2 = self.t_intervalo_inicio_2_l1.time().toString()
                                    self.final_intervalo_l1_2 = self.t_intervalo_fim_2_l1.time().toString()

                                    inicio_intervalo_l1_2_conversao_min = int(self.inicio_intervalo_l1_2[:2]) * 60
                                    inicio_intervalo_l1_2_total_min = inicio_intervalo_l1_2_conversao_min + int(
                                            self.inicio_intervalo_l1_2[3:5])

                                    final_intervalo_l1_2_conversao_min = int(self.final_intervalo_l1_2[:2]) * 60
                                    final_intervalo_l1_2_total_min = final_intervalo_l1_2_conversao_min + int(
                                            self.final_intervalo_l1_2[3:5])

                                    turno_tarde_intervalo_l1_2 = final_intervalo_l1_2_total_min - inicio_intervalo_l1_2_total_min

                                    horas_trabalhadas_turno_tarde_l1 = horas_trabalhadas_turno_tarde_l1 - turno_tarde_intervalo_l1_2

                            if self.box_laboral_2_l1.isChecked():

                                    self.inicio_laboral_l1_2 = self.t_laboral_inicio_2_l1.time().toString()
                                    self.final_laboral_l1_2 = self.t_laboral_fim_2_l1.time().toString()



                                    inicio_laboral_l1_2_conversao_min = int(self.inicio_laboral_l1_2[:2]) * 60
                                    inicio_laboral_l1_2_total_min = inicio_laboral_l1_2_conversao_min + int(
                                            self.inicio_laboral_l1_2[3:5])

                                    final_laboral_l1_2_conversao_min = int(self.final_laboral_l1_2[:2]) * 60
                                    final_laboral_l1_2_total_min = final_laboral_l1_2_conversao_min + int(self.final_laboral_l1_2[3:5])

                                    turno_tarde_laboral_l1_2 = final_laboral_l1_2_total_min - inicio_laboral_l1_2_total_min



                                    horas_trabalhadas_turno_tarde_l1 = horas_trabalhadas_turno_tarde_l1 - turno_tarde_laboral_l1_2

                            if self.box_janta_2_l1.isChecked():

                                    self.inicio_janta_l1 = self.t_janta_inicio_2_l1.time().toString()
                                    self.final_janta_l1 = self.t_janta_fim_2_l1.time().toString()

                                    inicio_janta_l1_conversao_min = int(self.inicio_janta_l1[:2]) * 60
                                    inicio_janta_l1_total_min = inicio_janta_l1_conversao_min + int(self.inicio_janta_l1[3:5])

                                    final_janta_l1_conversao_min = int(self.final_janta_l1[:2]) * 60
                                    final_janta_l1_total_min = final_janta_l1_conversao_min + int(
                                            self.final_janta_l1[3:5])
                                    turno_tarde_janta_l1 = final_janta_l1_total_min - inicio_janta_l1_total_min



                                    horas_trabalhadas_turno_tarde_l1 = horas_trabalhadas_turno_tarde_l1 - turno_tarde_janta_l1



                            self.meta_linha_1_tarde = self.spin_meta_2_l1.value()
                            self.meta_linha_1_tarde_registro = int(self.meta_linha_1_tarde)


                            self.horas_trabalhadas_turno_tarde_l1 = horas_trabalhadas_turno_tarde_l1 * 60

                            self.tempo_estimado_por_peca_l1_2 = round(
                                    (self.horas_trabalhadas_turno_tarde_l1 / self.meta_linha_1_tarde_registro), 2)

                            self.temp_peca_2_l1.setText(f'{ str(self.tempo_estimado_por_peca_l1_2)} (s)')






                    ##################################

                            self.contagem_projetada_linha_1 = 0
                            self.sistema_ativado_l1 = True
                            self.sistema_iniciado_linha_1 = False

            self.show_info_messagebox()



    def press_botao_set_linha_2(self):

           print("TESTE")

           if (self.sistema_iniciado_linha_2 == False):

                        print("Horarios Setados Linha 2")

                        ###### 1 Turno ######

                        self.inicio_turno_l2 = None
                        self.final_turno_l2 = None
                        self.inicio_intervalo_l2 = None
                        self.final_intervalo_l2 = None
                        self.inicio_laboral_l2 = None
                        self.final_laboral_l2 = None
                        self.inicio_almoco_l2 = None
                        self.final_almoco_l2 = None
                        self.primeiro_turno_start_l2 = False
                        self.estado_controle_sistema_linha_2 = False

                        if self.box_turno_1_l2.isChecked():



                                self.inicio_turno_l2 = self.t_turno_inicio_1_l2.time().toString()
                                self.final_turno_l2 = self.t_turno_fim_1_l2.time().toString()

                                print(self.inicio_turno_l2)

                                inicio_turno_l2_conversao_min = int(self.inicio_turno_l2[:2]) * 60
                                inicio_turno_l2_total_min = inicio_turno_l2_conversao_min + int(
                                        self.inicio_turno_l2[3:5])

                                final_turno_l2_conversao_min = int(self.final_turno_l2[:2]) * 60 #
                                final_turno_l2_total_min = final_turno_l2_conversao_min + int(self.final_turno_l2[3:5])

                                horas_trabalhadas_turno_manha_l2 = final_turno_l2_total_min - inicio_turno_l2_total_min

                                if self.box_intervalo_1_l2.isChecked():
                                        self.inicio_intervalo_l2 = self.t_intervalo_inicio_1_l2.time().toString()
                                        self.final_intervalo_l2 = self.t_intervalo_fim_1_l2.time().toString()

                                        inicio_intervalo_l2_conversao_min = int(self.inicio_intervalo_l2[:2]) * 60
                                        inicio_intervalo_l2_total_min = inicio_intervalo_l2_conversao_min + int(
                                                self.inicio_intervalo_l2[3:5])

                                        final_intervalo_l2_conversao_min = int(self.final_intervalo_l2[:2]) * 60
                                        final_intervalo_l2_total_min = final_intervalo_l2_conversao_min + int(
                                                self.final_intervalo_l2[3:5])

                                        turno_manhã_intervalo_l2 = final_intervalo_l2_total_min - inicio_intervalo_l2_total_min

                                        horas_trabalhadas_turno_manha_l2 = horas_trabalhadas_turno_manha_l2 - turno_manhã_intervalo_l2

                                if self.box_laboral_1_l2.isChecked():
                                        self.inicio_laboral_l2 = self.t_laboral_inicio_1_l2.time().toString()
                                        self.final_laboral_l2 = self.t_laboral_fim_1_l2.time().toString()

                                        inicio_laboral_l2_conversao_min = int(self.inicio_laboral_l2[:2]) * 60
                                        inicio_laboral_l2_total_min = inicio_laboral_l2_conversao_min + int(
                                                self.inicio_laboral_l2[3:5])

                                        final_laboral_l2_conversao_min = int(self.final_laboral_l2[:2]) * 60
                                        final_laboral_l2_total_min = final_laboral_l2_conversao_min + int(
                                                self.final_laboral_l2[3:5])

                                        turno_manha_laboral_l2 = final_laboral_l2_total_min - inicio_laboral_l2_total_min

                                        horas_trabalhadas_turno_manha_l2 = horas_trabalhadas_turno_manha_l2 - turno_manha_laboral_l2

                                if self.box_almoco_1_l2.isChecked():
                                        self.inicio_almoco_l2 = self.t_almoco_inicio_1_l2.time().toString()
                                        self.final_almoco_l2 = self.t_almoco_fim_1_l2.time().toString()

                                        inicio_almoco_l2_conversao_min = int(self.inicio_almoco_l2[:2]) * 60
                                        inicio_almoco_l2_total_min = inicio_almoco_l2_conversao_min + int(
                                                self.inicio_almoco_l2[3:5])

                                        final_almoco_l2_conversao_min = int(self.final_almoco_l2[:2]) * 60
                                        final_almoco_l2_total_min = final_almoco_l2_conversao_min + int(
                                                self.final_almoco_l2[3:5])
                                        turno_manha_almoco_l2 = final_almoco_l2_total_min - inicio_almoco_l2_total_min

                                        print(turno_manha_almoco_l2)

                                        horas_trabalhadas_turno_manha_l2 = horas_trabalhadas_turno_manha_l2 - turno_manha_almoco_l2

                                self.meta_linha_2 = self.spin_meta_1_l2.value()
                                self.meta_linha_2 = int(self.meta_linha_2)
                                self.meta_linha_2_manha_registro = self.meta_linha_2

                                self.horas_trabalhadas_turno_manha_l2_segundos = horas_trabalhadas_turno_manha_l2 * 60

                                self.tempo_estimado_por_peca_l2_1 = round((self.horas_trabalhadas_turno_manha_l2_segundos / self.meta_linha_2_manha_registro),2)

                                self.temp_peca_1_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_1)} (s)')
                                print("SETADO")

                                self.contagem_projetada_linha_2 = 0
                                self.sistema_ativado_l2 = True
                                self.sistema_iniciado_linha_2 = False
                                self.primeiro_turno_start_l2 = 0

                        ###### 2 Turno #####

                        self.inicio_turno_l2_2 = None
                        self.final_turno_l2_2 = None
                        self.inicio_intervalo_l2_2 = None
                        self.final_intervalo_l2_2 = None
                        self.inicio_laboral_l2_2 = None
                        self.final_laboral_l2_2 = None
                        self.inicio_janta_l2 = None
                        self.final_janta_l2 = None
                        self.segundo_turno_start_l2 = False

                        if self.box_turno_2_l2.isChecked():

                                self.inicio_turno_l2_2 = self.t_turno_inicio_2_l2.time().toString()
                                self.final_turno_l2_2 = self.t_turno_fim_2_l2.time().toString()

                                print(self.inicio_turno_l2_2)

                                inicio_turno_l2_2_conversao_min = int(self.inicio_turno_l2_2[:2]) * 60
                                inicio_turno_l2_2_total_min = inicio_turno_l2_2_conversao_min + int(
                                        self.inicio_turno_l2_2[3:5])

                                final_turno_l2_2_conversao_min = int(self.final_turno_l2_2[:2]) * 60
                                final_turno_l2_2_total_min = final_turno_l2_2_conversao_min + int(
                                        self.final_turno_l2_2[3:5])

                                horas_trabalhadas_turno_tarde_l2 = final_turno_l2_2_total_min - inicio_turno_l2_2_total_min

                                if self.box_intervalo_2_l2.isChecked():
                                        self.inicio_intervalo_l2_2 = self.t_intervalo_inicio_2_l2.time().toString()
                                        self.final_intervalo_l2_2 = self.t_intervalo_fim_2_l2.time().toString()

                                        inicio_intervalo_l2_2_conversao_min = int(self.inicio_intervalo_l2_2[:2]) * 60
                                        inicio_intervalo_l2_2_total_min = inicio_intervalo_l2_2_conversao_min + int(
                                                self.inicio_intervalo_l2_2[3:5])

                                        final_intervalo_l2_2_conversao_min = int(self.final_intervalo_l2_2[:2]) * 60
                                        final_intervalo_l2_2_total_min = final_intervalo_l2_2_conversao_min + int(
                                                self.final_intervalo_l2_2[3:5])

                                        turno_tarde_intervalo_l2_2 = final_intervalo_l2_2_total_min - inicio_intervalo_l2_2_total_min

                                        horas_trabalhadas_turno_tarde_l2 = horas_trabalhadas_turno_tarde_l2 - turno_tarde_intervalo_l2_2

                                if self.box_laboral_2_l2.isChecked():
                                        self.inicio_laboral_l2_2 = self.t_laboral_inicio_2_l2.time().toString()
                                        self.final_laboral_l2_2 = self.t_laboral_fim_2_l2.time().toString()

                                        inicio_laboral_l2_2_conversao_min = int(self.inicio_laboral_l2_2[:2]) * 60
                                        inicio_laboral_l2_2_total_min = inicio_laboral_l2_2_conversao_min + int(
                                                self.inicio_laboral_l2_2[3:5])

                                        final_laboral_l2_2_conversao_min = int(self.final_laboral_l2_2[:2]) * 60
                                        final_laboral_l2_2_total_min = final_laboral_l2_2_conversao_min + int(
                                                self.final_laboral_l2_2[3:5])

                                        turno_tarde_laboral_l2_2 = final_laboral_l2_2_total_min - inicio_laboral_l2_2_total_min

                                        horas_trabalhadas_turno_tarde_l2 = horas_trabalhadas_turno_tarde_l2 - turno_tarde_laboral_l2_2

                                if self.box_janta_2_l2.isChecked():
                                        self.inicio_janta_l2 = self.t_janta_inicio_2_l2.time().toString()
                                        self.final_janta_l2 = self.t_janta_fim_2_l2.time().toString()

                                        inicio_janta_l2_conversao_min = int(self.inicio_janta_l2[:2]) * 60
                                        inicio_janta_l2_total_min = inicio_janta_l2_conversao_min + int(
                                                self.inicio_janta_l2[3:5])

                                        final_janta_l2_conversao_min = int(self.final_janta_l2[:2]) * 60
                                        final_janta_l2_total_min = final_janta_l2_conversao_min + int(
                                                self.final_janta_l2[3:5])
                                        turno_tarde_janta_l2 = final_janta_l2_total_min - inicio_janta_l2_total_min

                                        horas_trabalhadas_turno_tarde_l2 = horas_trabalhadas_turno_tarde_l2 - turno_tarde_janta_l2

                                self.meta_linha_2_tarde = self.spin_meta_2_l2.value()
                                self.meta_linha_2_tarde_registro = int(self.meta_linha_2_tarde)

                                self.horas_trabalhadas_turno_tarde_l2 = horas_trabalhadas_turno_tarde_l2 * 60

                                self.tempo_estimado_por_peca_l2_2 = round(
                                        (self.horas_trabalhadas_turno_tarde_l2 / self.meta_linha_2_tarde_registro), 2)

                                self.temp_peca_2_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_2)} (s)')

                                ##################################

                                self.contagem_projetada_linha_2 = 0
                                self.sistema_ativado_l2 = True
                                self.sistema_iniciado_linha_2 = False
                                self.segundo_turno_start_l2 = False




           self.show_info_messagebox()




    def press_botao_set_linha_3(self):

                print("TESTE L3")

                if (self.sistema_iniciado_linha_3 == False):

                        print("Horarios Setados Linha 3")

                        ###### 1 Turno ######

                        self.inicio_turno_l3 = None
                        self.final_turno_l3 = None
                        self.inicio_intervalo_l3 = None
                        self.final_intervalo_l3 = None
                        self.inicio_laboral_l3 = None
                        self.final_laboral_l3 = None
                        self.inicio_almoco_l3 = None
                        self.final_almoco_l3 = None
                        self.primeiro_turno_start_l3 = False
                        self.estado_controle_sistema_linha_3 = False

                        if self.box_turno_1_l3.isChecked():

                                self.inicio_turno_l3 = self.t_turno_inicio_1_l3.time().toString()
                                self.final_turno_l3 = self.t_turno_fim_1_l3.time().toString()

                                print(self.inicio_turno_l3)

                                inicio_turno_l3_conversao_min = int(self.inicio_turno_l3[:2]) * 60
                                inicio_turno_l3_total_min = inicio_turno_l3_conversao_min + int(
                                        self.inicio_turno_l3[3:5])

                                final_turno_l3_conversao_min = int(self.final_turno_l3[:2]) * 60  #
                                final_turno_l3_total_min = final_turno_l3_conversao_min + int(self.final_turno_l3[3:5])

                                horas_trabalhadas_turno_manha_l3 = final_turno_l3_total_min - inicio_turno_l3_total_min

                                if self.box_intervalo_1_l3.isChecked():
                                        self.inicio_intervalo_l3 = self.t_intervalo_inicio_1_l3.time().toString()
                                        self.final_intervalo_l3 = self.t_intervalo_fim_1_l3.time().toString()

                                        inicio_intervalo_l3_conversao_min = int(self.inicio_intervalo_l3[:2]) * 60
                                        inicio_intervalo_l3_total_min = inicio_intervalo_l3_conversao_min + int(
                                                self.inicio_intervalo_l3[3:5])

                                        final_intervalo_l3_conversao_min = int(self.final_intervalo_l3[:2]) * 60
                                        final_intervalo_l3_total_min = final_intervalo_l3_conversao_min + int(
                                                self.final_intervalo_l3[3:5])

                                        turno_manhã_intervalo_l3 = final_intervalo_l3_total_min - inicio_intervalo_l3_total_min

                                        horas_trabalhadas_turno_manha_l3 = horas_trabalhadas_turno_manha_l3 - turno_manhã_intervalo_l3

                                if self.box_laboral_1_l3.isChecked():
                                        self.inicio_laboral_l3 = self.t_laboral_inicio_1_l3.time().toString()
                                        self.final_laboral_l3 = self.t_laboral_fim_1_l3.time().toString()

                                        inicio_laboral_l3_conversao_min = int(self.inicio_laboral_l3[:2]) * 60
                                        inicio_laboral_l3_total_min = inicio_laboral_l3_conversao_min + int(
                                                self.inicio_laboral_l3[3:5])

                                        final_laboral_l3_conversao_min = int(self.final_laboral_l3[:2]) * 60
                                        final_laboral_l3_total_min = final_laboral_l3_conversao_min + int(
                                                self.final_laboral_l3[3:5])

                                        turno_manha_laboral_l3 = final_laboral_l3_total_min - inicio_laboral_l3_total_min

                                        horas_trabalhadas_turno_manha_l3 = horas_trabalhadas_turno_manha_l3 - turno_manha_laboral_l3

                                if self.box_almoco_1_l3.isChecked():
                                        self.inicio_almoco_l3 = self.t_almoco_inicio_1_l3.time().toString()
                                        self.final_almoco_l3 = self.t_almoco_fim_1_l3.time().toString()

                                        inicio_almoco_l3_conversao_min = int(self.inicio_almoco_l3[:2]) * 60
                                        inicio_almoco_l3_total_min = inicio_almoco_l3_conversao_min + int(
                                                self.inicio_almoco_l3[3:5])

                                        final_almoco_l3_conversao_min = int(self.final_almoco_l3[:2]) * 60
                                        final_almoco_l3_total_min = final_almoco_l3_conversao_min + int(
                                                self.final_almoco_l3[3:5])
                                        turno_manha_almoco_l3 = final_almoco_l3_total_min - inicio_almoco_l3_total_min

                                        print(turno_manha_almoco_l3)

                                        horas_trabalhadas_turno_manha_l3 = horas_trabalhadas_turno_manha_l3 - turno_manha_almoco_l3

                                self.meta_linha_3 = self.spin_meta_1_l3.value()
                                self.meta_linha_3 = int(self.meta_linha_3)
                                self.meta_linha_3_manha_registro = self.meta_linha_3

                                self.horas_trabalhadas_turno_manha_l3_segundos = horas_trabalhadas_turno_manha_l3 * 60

                                self.tempo_estimado_por_peca_l3_1 = round((self.horas_trabalhadas_turno_manha_l3_segundos / self.meta_linha_3_manha_registro),2)

                                self.temp_peca_1_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_1)} (s)')
                                print("SETADO")

                                self.contagem_projetada_linha_3 = 0
                                self.sistema_ativado_l3 = True
                                self.sistema_iniciado_linha_3 = False
                                self.primeiro_turno_start_l3 = 0

                        ###### 2 Turno #####

                        self.inicio_turno_l3_2 = None
                        self.final_turno_l3_2 = None
                        self.inicio_intervalo_l3_2 = None
                        self.final_intervalo_l3_2 = None
                        self.inicio_laboral_l3_2 = None
                        self.final_laboral_l3_2 = None
                        self.inicio_janta_l3 = None
                        self.final_janta_l3 = None
                        self.segundo_turno_start_l3 = False

                        if self.box_turno_2_l3.isChecked():

                                self.inicio_turno_l3_2 = self.t_turno_inicio_2_l3.time().toString()
                                self.final_turno_l3_2 = self.t_turno_fim_2_l3.time().toString()

                                print(self.inicio_turno_l3_2)

                                inicio_turno_l3_2_conversao_min = int(self.inicio_turno_l3_2[:2]) * 60
                                inicio_turno_l3_2_total_min = inicio_turno_l3_2_conversao_min + int(
                                        self.inicio_turno_l3_2[3:5])

                                final_turno_l3_2_conversao_min = int(self.final_turno_l3_2[:2]) * 60
                                final_turno_l3_2_total_min = final_turno_l3_2_conversao_min + int(
                                        self.final_turno_l3_2[3:5])

                                horas_trabalhadas_turno_tarde_l3 = final_turno_l3_2_total_min - inicio_turno_l3_2_total_min

                                if self.box_intervalo_2_l3.isChecked():
                                        self.inicio_intervalo_l3_2 = self.t_intervalo_inicio_2_l3.time().toString()
                                        self.final_intervalo_l3_2 = self.t_intervalo_fim_2_l3.time().toString()

                                        inicio_intervalo_l3_2_conversao_min = int(self.inicio_intervalo_l3_2[:2]) * 60
                                        inicio_intervalo_l3_2_total_min = inicio_intervalo_l3_2_conversao_min + int(
                                                self.inicio_intervalo_l3_2[3:5])

                                        final_intervalo_l3_2_conversao_min = int(self.final_intervalo_l3_2[:2]) * 60
                                        final_intervalo_l3_2_total_min = final_intervalo_l3_2_conversao_min + int(
                                                self.final_intervalo_l3_2[3:5])

                                        turno_tarde_intervalo_l3_2 = final_intervalo_l3_2_total_min - inicio_intervalo_l3_2_total_min

                                        horas_trabalhadas_turno_tarde_l3 = horas_trabalhadas_turno_tarde_l3 - turno_tarde_intervalo_l3_2

                                if self.box_laboral_2_l3.isChecked():
                                        self.inicio_laboral_l3_2 = self.t_laboral_inicio_2_l3.time().toString()
                                        self.final_laboral_l3_2 = self.t_laboral_fim_2_l3.time().toString()

                                        inicio_laboral_l3_2_conversao_min = int(self.inicio_laboral_l3_2[:2]) * 60
                                        inicio_laboral_l3_2_total_min = inicio_laboral_l3_2_conversao_min + int(
                                                self.inicio_laboral_l3_2[3:5])

                                        final_laboral_l3_2_conversao_min = int(self.final_laboral_l3_2[:2]) * 60
                                        final_laboral_l3_2_total_min = final_laboral_l3_2_conversao_min + int(
                                                self.final_laboral_l3_2[3:5])

                                        turno_tarde_laboral_l3_2 = final_laboral_l3_2_total_min - inicio_laboral_l3_2_total_min

                                        horas_trabalhadas_turno_tarde_l3 = horas_trabalhadas_turno_tarde_l3 - turno_tarde_laboral_l3_2

                                if self.box_janta_2_l3.isChecked():
                                        self.inicio_janta_l3 = self.t_janta_inicio_2_l3.time().toString()
                                        self.final_janta_l3 = self.t_janta_fim_2_l3.time().toString()

                                        inicio_janta_l3_conversao_min = int(self.inicio_janta_l3[:2]) * 60
                                        inicio_janta_l3_total_min = inicio_janta_l3_conversao_min + int(
                                                self.inicio_janta_l3[3:5])

                                        final_janta_l3_conversao_min = int(self.final_janta_l3[:2]) * 60
                                        final_janta_l3_total_min = final_janta_l3_conversao_min + int(
                                                self.final_janta_l3[3:5])
                                        turno_tarde_janta_l3 = final_janta_l3_total_min - inicio_janta_l3_total_min

                                        horas_trabalhadas_turno_tarde_l3 = horas_trabalhadas_turno_tarde_l3 - turno_tarde_janta_l3

                                self.meta_linha_3_tarde = self.spin_meta_2_l3.value()
                                self.meta_linha_3_tarde_registro = int(self.meta_linha_3_tarde)

                                self.horas_trabalhadas_turno_tarde_l3 = horas_trabalhadas_turno_tarde_l3 * 60

                                self.tempo_estimado_por_peca_l3_2 = round(
                                        (self.horas_trabalhadas_turno_tarde_l3 / self.meta_linha_3_tarde_registro), 2)

                                self.temp_peca_2_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_2)} (s)')

                                ##################################

                                self.contagem_projetada_linha_3 = 0
                                self.sistema_ativado_l3 = True
                                self.sistema_iniciado_linha_3 = False
                                self.segundo_turno_start_l3 = False

                self.show_info_messagebox()









    def press_botao_set_linha_4(self):

                print("TESTE")

                if (self.sistema_iniciado_linha_4 == False):

                        print("Horarios Setados Linha 4")

                        ###### 1 Turno ######

                        self.inicio_turno_l4 = None
                        self.final_turno_l4 = None
                        self.inicio_intervalo_l4 = None
                        self.final_intervalo_l4 = None
                        self.inicio_laboral_l4 = None
                        self.final_laboral_l4 = None
                        self.inicio_almoco_l4 = None
                        self.final_almoco_l4 = None
                        self.primeiro_turno_start_l4 = False
                        self.estado_controle_sistema_linha_4 = False

                        if self.box_turno_1_l4.isChecked():

                                self.inicio_turno_l4 = self.t_turno_inicio_1_l4.time().toString()
                                self.final_turno_l4 = self.t_turno_fim_1_l4.time().toString()

                                print(self.inicio_turno_l4)

                                inicio_turno_l4_conversao_min = int(self.inicio_turno_l4[:2]) * 60
                                inicio_turno_l4_total_min = inicio_turno_l4_conversao_min + int(
                                        self.inicio_turno_l4[3:5])

                                final_turno_l4_conversao_min = int(self.final_turno_l4[:2]) * 60  #
                                final_turno_l4_total_min = final_turno_l4_conversao_min + int(self.final_turno_l4[3:5])

                                horas_trabalhadas_turno_manha_l4 = final_turno_l4_total_min - inicio_turno_l4_total_min

                                if self.box_intervalo_1_l4.isChecked():
                                        self.inicio_intervalo_l4 = self.t_intervalo_inicio_1_l4.time().toString()
                                        self.final_intervalo_l4 = self.t_intervalo_fim_1_l4.time().toString()

                                        inicio_intervalo_l4_conversao_min = int(self.inicio_intervalo_l4[:2]) * 60
                                        inicio_intervalo_l4_total_min = inicio_intervalo_l4_conversao_min + int(
                                                self.inicio_intervalo_l4[3:5])

                                        final_intervalo_l4_conversao_min = int(self.final_intervalo_l4[:2]) * 60
                                        final_intervalo_l4_total_min = final_intervalo_l4_conversao_min + int(
                                                self.final_intervalo_l4[3:5])

                                        turno_manhã_intervalo_l4 = final_intervalo_l4_total_min - inicio_intervalo_l4_total_min

                                        horas_trabalhadas_turno_manha_l4 = horas_trabalhadas_turno_manha_l4 - turno_manhã_intervalo_l4

                                if self.box_laboral_1_l4.isChecked():
                                        self.inicio_laboral_l4 = self.t_laboral_inicio_1_L4.time().toString()
                                        self.final_laboral_l4 = self.t_laboral_fim_1_l4.time().toString()

                                        inicio_laboral_l4_conversao_min = int(self.inicio_laboral_l4[:2]) * 60
                                        inicio_laboral_l4_total_min = inicio_laboral_l4_conversao_min + int(
                                                self.inicio_laboral_l4[3:5])

                                        final_laboral_l4_conversao_min = int(self.final_laboral_l4[:2]) * 60
                                        final_laboral_l4_total_min = final_laboral_l4_conversao_min + int(
                                                self.final_laboral_l4[3:5])

                                        turno_manha_laboral_l4 = final_laboral_l4_total_min - inicio_laboral_l4_total_min

                                        horas_trabalhadas_turno_manha_l4 = horas_trabalhadas_turno_manha_l4 - turno_manha_laboral_l4

                                if self.box_almoco_1_l4.isChecked():
                                        self.inicio_almoco_l4 = self.t_almoco_inicio_1_l4.time().toString()
                                        self.final_almoco_l4 = self.t_almoco_fim_1_l4.time().toString()

                                        inicio_almoco_l4_conversao_min = int(self.inicio_almoco_l4[:2]) * 60
                                        inicio_almoco_l4_total_min = inicio_almoco_l4_conversao_min + int(
                                                self.inicio_almoco_l4[3:5])

                                        final_almoco_l4_conversao_min = int(self.final_almoco_l4[:2]) * 60
                                        final_almoco_l4_total_min = final_almoco_l4_conversao_min + int(
                                                self.final_almoco_l4[3:5])
                                        turno_manha_almoco_l4 = final_almoco_l4_total_min - inicio_almoco_l4_total_min

                                        print(turno_manha_almoco_l4)

                                        horas_trabalhadas_turno_manha_l4 = horas_trabalhadas_turno_manha_l4 - turno_manha_almoco_l4

                                self.meta_linha_4 = self.spin_meta_1_L4.value()
                                self.meta_linha_4 = int(self.meta_linha_4)
                                self.meta_linha_4_manha_registro = self.meta_linha_4

                                self.horas_trabalhadas_turno_manha_l4_segundos = horas_trabalhadas_turno_manha_l4 * 60

                                self.tempo_estimado_por_peca_l4_1 = round((
                                        self.horas_trabalhadas_turno_manha_l4_segundos / self.meta_linha_4_manha_registro),
                                        2)

                                self.temp_peca_1_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_1)} (s)')
                                print("SETADO")

                                self.contagem_projetada_linha_4 = 0
                                self.sistema_ativado_l4 = True
                                self.sistema_iniciado_linha_4 = False
                                self.primeiro_turno_start_l4 = 0

                        ###### 2 Turno #####

                        self.inicio_turno_l4_2 = None
                        self.final_turno_l4_2 = None
                        self.inicio_intervalo_l4_2 = None
                        self.final_intervalo_l4_2 = None
                        self.inicio_laboral_l4_2 = None
                        self.final_laboral_l4_2 = None
                        self.inicio_janta_l4 = None
                        self.final_janta_l4 = None
                        self.segundo_turno_start_l4 = False

                        if self.box_turno_2_l4.isChecked():

                                self.inicio_turno_l4_2 = self.t_turno_inicio_2_l4.time().toString()
                                self.final_turno_l4_2 = self.t_turno_fim_2_l4.time().toString()

                                print(self.inicio_turno_l4_2)

                                inicio_turno_l4_2_conversao_min = int(self.inicio_turno_l4_2[:2]) * 60
                                inicio_turno_l4_2_total_min = inicio_turno_l4_2_conversao_min + int(
                                        self.inicio_turno_l4_2[3:5])

                                final_turno_l4_2_conversao_min = int(self.final_turno_l4_2[:2]) * 60
                                final_turno_l4_2_total_min = final_turno_l4_2_conversao_min + int(
                                        self.final_turno_l4_2[3:5])

                                horas_trabalhadas_turno_tarde_l4 = final_turno_l4_2_total_min - inicio_turno_l4_2_total_min

                                if self.box_intervalo_2_l4.isChecked():
                                        self.inicio_intervalo_l4_2 = self.t_intervalo_inicio_2_l4.time().toString()
                                        self.final_intervalo_l4_2 = self.t_intervalo_fim_2_l4.time().toString()

                                        inicio_intervalo_l4_2_conversao_min = int(self.inicio_intervalo_l4_2[:2]) * 60
                                        inicio_intervalo_l4_2_total_min = inicio_intervalo_l4_2_conversao_min + int(
                                                self.inicio_intervalo_l4_2[3:5])

                                        final_intervalo_l4_2_conversao_min = int(self.final_intervalo_l4_2[:2]) * 60
                                        final_intervalo_l4_2_total_min = final_intervalo_l4_2_conversao_min + int(
                                                self.final_intervalo_l4_2[3:5])

                                        turno_tarde_intervalo_l4_2 = final_intervalo_l4_2_total_min - inicio_intervalo_l4_2_total_min

                                        horas_trabalhadas_turno_tarde_l4 = horas_trabalhadas_turno_tarde_l4 - turno_tarde_intervalo_l4_2

                                if self.box_laboral_2_l4.isChecked():
                                        self.inicio_laboral_l4_2 = self.t_laboral_inicio_2_l4.time().toString()
                                        self.final_laboral_l4_2 = self.t_laboral_fim_2_l4.time().toString()

                                        inicio_laboral_l4_2_conversao_min = int(self.inicio_laboral_l4_2[:2]) * 60
                                        inicio_laboral_l4_2_total_min = inicio_laboral_l4_2_conversao_min + int(
                                                self.inicio_laboral_l4_2[3:5])

                                        final_laboral_l4_2_conversao_min = int(self.final_laboral_l4_2[:2]) * 60
                                        final_laboral_l4_2_total_min = final_laboral_l4_2_conversao_min + int(
                                                self.final_laboral_l4_2[3:5])

                                        turno_tarde_laboral_l4_2 = final_laboral_l4_2_total_min - inicio_laboral_l4_2_total_min

                                        horas_trabalhadas_turno_tarde_l4 = horas_trabalhadas_turno_tarde_l4 - turno_tarde_laboral_l4_2

                                if self.box_janta_2_l4.isChecked():
                                        self.inicio_janta_l4 = self.t_janta_inicio_2_l4.time().toString()
                                        self.final_janta_l4 = self.t_janta_fim_2_l4.time().toString()

                                        inicio_janta_l4_conversao_min = int(self.inicio_janta_l4[:2]) * 60
                                        inicio_janta_l4_total_min = inicio_janta_l4_conversao_min + int(
                                                self.inicio_janta_l4[3:5])

                                        final_janta_l4_conversao_min = int(self.final_janta_l4[:2]) * 60
                                        final_janta_l4_total_min = final_janta_l4_conversao_min + int(
                                                self.final_janta_l4[3:5])
                                        turno_tarde_janta_l4 = final_janta_l4_total_min - inicio_janta_l4_total_min

                                        horas_trabalhadas_turno_tarde_l4 = horas_trabalhadas_turno_tarde_l4 - turno_tarde_janta_l4

                                self.meta_linha_4_tarde = self.spin_meta_2_l4.value()
                                self.meta_linha_4_tarde_registro = int(self.meta_linha_4_tarde)

                                self.horas_trabalhadas_turno_tarde_l4 = horas_trabalhadas_turno_tarde_l4 * 60

                                self.tempo_estimado_por_peca_l4_2 = round(
                                        (self.horas_trabalhadas_turno_tarde_l4 / self.meta_linha_4_tarde_registro), 2)

                                self.temp_peca_2_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_2)} (s)')

                                ##################################

                                self.contagem_projetada_linha_4 = 0
                                self.sistema_ativado_l4 = True
                                self.sistema_iniciado_linha_4 = False
                                self.segundo_turno_start_l4 = False

                self.show_info_messagebox()






    def press_botao_reset_linha_1(self):

            self.inicio_turno_l1 = None
            self.final_turno_l1 = None
            self.inicio_intervalo_l1 = None
            self.final_intervalo_l1 = None
            self.inicio_laboral_l1 = None
            self.final_laboral_l1 = None
            self.inicio_almoco_l1 = None
            self.final_laboral_l1 = None

            self.inicio_turno_l1_2 = None
            self.final_turno_l1_2 = None
            self.inicio_intervalo_l1_2 = None
            self.final_intervalo_l1_2 = None
            self.inicio_laboral_l1_2 = None
            self.final_laboral_l1_2 = None
            self.inicio_almoco_l1_2 = None
            self.final_laboral_l1_2 = None

            self.estado_controle_sistema_linha_1 = False
            self.sistema_iniciado_linha_1 = False
            self.sistema_ativado_l1 = False

            self.primeiro_turno_start = False
            self.segundo_turno_start = False




            self.tempo_estimado_por_peca_l1_1 = 0
            self.tempo_estimado_por_peca_l1_2 = 0

            self.temp_peca_1_l1.setText(f'{str(self.tempo_estimado_por_peca_l1_1)} (s)')
            self.temp_peca_2_l1.setText(f'{str(self.tempo_estimado_por_peca_l1_2)} (s)')

            self.lcd_cont_p_l1.setProperty("value", int(0))

            self.status_l1.setText(
                    QCoreApplication.translate("MainWindow", u"Parada", None))
            self.status_l1.setStyleSheet(
                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

    def press_botao_reset_linha_2(self):

            self.inicio_turno_l2 = None
            self.final_turno_l2 = None
            self.inicio_intervalo_l2 = None
            self.final_intervalo_l2 = None
            self.inicio_laboral_l2 = None
            self.final_laboral_l2 = None
            self.inicio_almoco_l2 = None
            self.final_laboral_l2 = None

            self.inicio_turno_l2_2 = None
            self.final_turno_l2_2 = None
            self.inicio_intervalo_l2_2 = None
            self.final_intervalo_l2_2 = None
            self.inicio_laboral_l2_2 = None
            self.final_laboral_l2_2 = None
            self.inicio_almoco_l2_2 = None
            self.final_laboral_l2_2 = None

            self.estado_controle_sistema_linha_2 = False
            self.sistema_iniciado_linha_2 = False
            self.sistema_ativado_l2 = False

            self.primeiro_turno_start_l2 = False
            self.segundo_turno_start_l2 = False

            self.tempo_estimado_por_peca_l2_1 = 0
            self.tempo_estimado_por_peca_l2_2 = 0

            self.temp_peca_1_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_1)} (s)')
            self.temp_peca_2_l2.setText(f'{str(self.tempo_estimado_por_peca_l2_2)} (s)')

            self.lcd_cont_p_l2.setProperty("value", int(0))


            self.status_l2.setText(
                            QCoreApplication.translate("MainWindow", u"Parada", None))
            self.status_l2.setStyleSheet(
                            u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")



            print("RESET LINHA 2")

    def press_botao_reset_linha_3(self):

                self.inicio_turno_l3 = None
                self.final_turno_l3 = None
                self.inicio_intervalo_l3 = None
                self.final_intervalo_l3 = None
                self.inicio_laboral_l3 = None
                self.final_laboral_l3 = None
                self.inicio_almoco_l3 = None
                self.final_laboral_l3 = None

                self.inicio_turno_l3_2 = None
                self.final_turno_l3_2 = None
                self.inicio_intervalo_l3_2 = None
                self.final_intervalo_l3_2 = None
                self.inicio_laboral_l3_2 = None
                self.final_laboral_l3_2 = None
                self.inicio_almoco_l3_2 = None
                self.final_laboral_l3_2 = None

                self.estado_controle_sistema_linha_3 = False
                self.sistema_iniciado_linha_3 = False
                self.sistema_ativado_l3 = False

                self.primeiro_turno_start_l3 = False
                self.segundo_turno_start_l3 = False

                self.tempo_estimado_por_peca_l3_1 = 0
                self.tempo_estimado_por_peca_l3_2 = 0

                self.temp_peca_1_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_1)} (s)')
                self.temp_peca_2_l3.setText(f'{str(self.tempo_estimado_por_peca_l3_2)} (s)')

                self.lcd_cont_prog_l3.setProperty("value", int(0))

                self.status_l3.setText(
                        QCoreApplication.translate("MainWindow", u"Parada", None))
                self.status_l3.setStyleSheet(
                        u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                print("RESET LINHA 2")

    def press_botao_reset_linha_4(self):

                self.inicio_turno_l4 = None
                self.final_turno_l4 = None
                self.inicio_intervalo_l4 = None
                self.final_intervalo_l4 = None
                self.inicio_laboral_l4 = None
                self.final_laboral_l4 = None
                self.inicio_almoco_l4 = None
                self.final_laboral_l4 = None

                self.inicio_turno_l4_2 = None
                self.final_turno_l4_2 = None
                self.inicio_intervalo_l4_2 = None
                self.final_intervalo_l4_2 = None
                self.inicio_laboral_l4_2 = None
                self.final_laboral_l4_2 = None
                self.inicio_almoco_l4_2 = None
                self.final_laboral_l4_2 = None

                self.estado_controle_sistema_linha_4 = False
                self.sistema_iniciado_linha_4 = False
                self.sistema_ativado_l4 = False

                self.primeiro_turno_start_l4 = False
                self.segundo_turno_start_l4 = False

                self.tempo_estimado_por_peca_l4_1 = 0
                self.tempo_estimado_por_peca_l4_2 = 0

                self.temp_peca_1_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_1)} (s)')
                self.temp_peca_2_l4.setText(f'{str(self.tempo_estimado_por_peca_l4_2)} (s)')

                self.lcd_cont_p_l4.setProperty("value", int(0))

                self.status_l4.setText(
                        QCoreApplication.translate("MainWindow", u"Parada", None))
                self.status_l4.setStyleSheet(
                        u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                print("RESET LINHA 2")











    def atualizar_interface(self):



        if (self.counter1 == 1):
                self.atualiza_linha_1()


        if (self.counter1 == 2 ):

                self.atualiza_linha_2()


        if (self.counter1 == 3):

                self.atualiza_linha_3()



        if (self.counter1 == 4):

                self.atualiza_linha_4()



        if (self.counter1 == 5):





                self.compara_contagem_programada_real()
                












        if(self.counter1 > 5):



                self.counter1 = 0



        if (self.counter2 > 150):

                start_gravar_db = threading.Thread(target=self.gravar_banco_de_dados())

                # Inicie o thread
                start_gravar_db.start()

                self.counter2 = 0



        self.counter2 = self.counter2 + 1
        self.counter1 = self.counter1 + 1





    def atualiza_linha_1(self):








        def start_subscriber_l1():





                try:

                        self.subscriber_mesa_1.start()
                        self.subscriber_est_1_ap.start()
                        self.subscriber_est_1_rep.start()
                        self.subscriber_pre_1_ap.start()
                        self.subscriber_pre_1_rep.start()
                        self.subscriber_hy_1_ap.start()
                        self.subscriber_hy_1_rep.start()



                        local_Mesa_de_Montagem_L1 = self.subscriber_mesa_1.get_value()
                        local_Estanquiedade_Aprovadas_L1 = self.subscriber_est_1_ap.get_value()
                        local_Estanquiedade_Reprovadas_L1 = self.subscriber_est_1_rep.get_value()
                        local_Pressurizacao_Aprovadas_L1 = self.subscriber_pre_1_ap.get_value()
                        local_Pressurizacao_Reprovadas_L1 = self.subscriber_pre_1_rep.get_value()
                        local_Hypot_Aprovadas_L1 = self.subscriber_hy_1_ap.get_value()
                        local_Hypot_Reprovadas_L1 = self.subscriber_hy_1_rep.get_value()

                        if (int(local_Mesa_de_Montagem_L1) >= 1000):
                                self.Mesa_de_Montagem_L1 = int(local_Mesa_de_Montagem_L1) - 1000
                                self.lcd_mesa_l1.setProperty("value", int(self.Mesa_de_Montagem_L1))

                        if (int(local_Estanquiedade_Aprovadas_L1) >= 2000):
                                self.Estanquiedade_Aprovadas_L1 = int(local_Estanquiedade_Aprovadas_L1) - 2000
                                self.lcd_est_ap_l1.setProperty("value", int(self.Estanquiedade_Aprovadas_L1))

                        if (int(local_Estanquiedade_Reprovadas_L1) >= 4000):
                                self.Estanquiedade_Reprovadas_L1 = int(local_Estanquiedade_Reprovadas_L1) - 4000
                                self.lcd_est_rep_l1.setProperty("value", int(self.Estanquiedade_Reprovadas_L1))

                        if (int(local_Pressurizacao_Aprovadas_L1) >= 6000):
                                self.Pressurizacao_Aprovadas_L1 = int(local_Pressurizacao_Aprovadas_L1) - 6000
                                self.lcd_pre_ap_l1.setProperty("value", int(self.Pressurizacao_Aprovadas_L1))

                        if (int(local_Pressurizacao_Reprovadas_L1) >= 8000):
                                self.Pressurizacao_Reprovadas_L1 = int(local_Pressurizacao_Reprovadas_L1) - 8000
                                self.lcd_pre_rep_l1.setProperty("value", int(self.Pressurizacao_Reprovadas_L1))

                        if (int(local_Hypot_Aprovadas_L1) >= 10000):
                                self.Hypot_Aprovadas_L1 = int(local_Hypot_Aprovadas_L1) - 10000
                                self.lcd_hy_ap_l1.setProperty("value", int(self.Hypot_Aprovadas_L1))

                        if (int(local_Hypot_Reprovadas_L1) >= 12000):
                                self.Hypot_Reprovadas_L1 = int(local_Hypot_Reprovadas_L1) - 12000
                                self.lcd_hy_rep_l1.setProperty("value", int(self.Hypot_Reprovadas_L1))




                        self.subscriber_mesa_1.stop()
                        self.subscriber_est_1_ap.stop()
                        self.subscriber_est_1_rep.stop()
                        self.subscriber_pre_1_ap.stop()
                        self.subscriber_pre_1_rep.stop()
                        self.subscriber_hy_1_ap.stop()
                        self.subscriber_hy_1_rep.stop()










                except Exception as e:

                        self.tempo_servidor_offiline = self.tempo_servidor_offiline + 1



                        print("Error Linha 1")




















        start_thread_l1 = threading.Thread(target=start_subscriber_l1)

        # Inicie o thread
        start_thread_l1.start()













    def atualiza_linha_2(self):

        def start_subscriber_l2():

                try:

                        self.subscriber_mesa_2.start()
                        self.subscriber_est_2_ap.start()
                        self.subscriber_est_2_rep.start()
                        self.subscriber_pre_2_ap.start()
                        self.subscriber_pre_2_rep.start()
                        self.subscriber_hy_2_ap.start()
                        self.subscriber_hy_2_rep.start()


                        local_Mesa_de_Montagem_L2 = self.subscriber_mesa_2.get_value()
                        local_Estanquiedade_Aprovadas_L2 = self.subscriber_est_2_ap.get_value()
                        local_Estanquiedade_Reprovadas_L2 = self.subscriber_est_2_rep.get_value()
                        local_Pressurizacao_Aprovadas_L2 = self.subscriber_pre_2_ap.get_value()
                        local_Pressurizacao_Reprovadas_L2 = self.subscriber_pre_2_rep.get_value()
                        local_Hypot_Aprovadas_L2 = self.subscriber_hy_2_ap.get_value()
                        local_Hypot_Reprovadas_L2 = self.subscriber_hy_2_rep.get_value()




                        if (int(local_Mesa_de_Montagem_L2) >= 1000):
                                self.Mesa_de_Montagem_L2 = int(local_Mesa_de_Montagem_L2) - 1000
                                self.lcd_mesa_l2.setProperty("value", int(self.Mesa_de_Montagem_L2))

                        if (int(local_Estanquiedade_Aprovadas_L2) >= 2000):
                                self.Estanquiedade_Aprovadas_L2 = int(local_Estanquiedade_Aprovadas_L2) - 2000
                                self.lcd_est_ap_l2.setProperty("value", int(self.Estanquiedade_Aprovadas_L2))

                        if (int(local_Estanquiedade_Reprovadas_L2) >= 4000):
                                self.Estanquiedade_Reprovadas_L2 = int(local_Estanquiedade_Reprovadas_L2) - 4000
                                self.lcd_est_rep_l2.setProperty("value", int(self.Estanquiedade_Reprovadas_L2))

                        if (int(local_Pressurizacao_Aprovadas_L2) >= 6000):
                                self.Pressurizacao_Aprovadas_L2 = int(local_Pressurizacao_Aprovadas_L2) - 6000
                                self.lcd_pre_ap_l2.setProperty("value", int(self.Pressurizacao_Aprovadas_L2))

                        if (int(local_Pressurizacao_Reprovadas_L2) >= 8000):
                                self.Pressurizacao_Reprovadas_L2 = int(local_Pressurizacao_Reprovadas_L2) - 8000
                                self.lcd_pre_rep_l2.setProperty("value", int(self.Pressurizacao_Reprovadas_L2))

                        if (int(local_Hypot_Aprovadas_L2) >= 10000):
                                self.Hypot_Aprovadas_L2 = int(local_Hypot_Aprovadas_L2) - 10000
                                self.lcd_hy_ap_l2.setProperty("value", int(self.Hypot_Aprovadas_L2))

                        if (int(local_Hypot_Reprovadas_L2) >= 12000):
                                self.Hypot_Reprovadas_L2 = int(local_Hypot_Reprovadas_L2) - 12000
                                self.lcd_hy_rep_l2.setProperty("value", int(self.Hypot_Reprovadas_L2))


                        self.subscriber_mesa_2.stop()
                        self.subscriber_est_2_ap.stop()
                        self.subscriber_est_2_rep.stop()
                        self.subscriber_pre_2_ap.stop()
                        self.subscriber_pre_2_rep.stop()
                        self.subscriber_hy_2_ap.stop()
                        self.subscriber_hy_2_rep.stop()

                except Exception as e:

                        print("Error Linha 2")

                        self.tempo_servidor_offiline = self.tempo_servidor_offiline + 1














        start_thread_l2 = threading.Thread(target=start_subscriber_l2)

        # Inicie o thread
        start_thread_l2.start()









    def atualiza_linha_3(self):

        def start_subscriber_l3():


                try:

                        self.subscriber_mesa_3.start()
                        self.subscriber_est_3_ap.start()
                        self.subscriber_est_3_rep.start()
                        self.subscriber_hy_3_ap.start()
                        self.subscriber_hy_3_rep.start()

                        local_Mesa_de_Montagem_L3 = self.subscriber_mesa_3.get_value()
                        local_Estanquiedade_Aprovadas_L3 = self.subscriber_est_3_ap.get_value()
                        local_Estanquiedade_Reprovadas_L3 = self.subscriber_est_3_rep.get_value()
                        local_Hypot_Aprovadas_L3 = self.subscriber_hy_3_ap.get_value()
                        local_Hypot_Reprovadas_L3 = self.subscriber_hy_3_rep.get_value()

                        if (int(local_Mesa_de_Montagem_L3) >= 1000):
                            self.Mesa_de_Montagem_L3 = int(local_Mesa_de_Montagem_L3) - 1000
                            self.lcd_mesa_l3.setProperty("value", int(self.Mesa_de_Montagem_L3))

                        if (int(local_Estanquiedade_Aprovadas_L3) >= 2000):
                            self.Estanquiedade_Aprovadas_L3 = int(local_Estanquiedade_Aprovadas_L3) - 2000
                            self.lcd_est_ap_l3.setProperty("value", int(self.Estanquiedade_Aprovadas_L3))

                        if (int(local_Estanquiedade_Reprovadas_L3) >= 4000):
                            self.Estanquiedade_Reprovadas_L3 = int(local_Estanquiedade_Reprovadas_L3) - 4000
                            self.lcd_est_rep_l3.setProperty("value", int(self.Estanquiedade_Reprovadas_L3))



                        if (int(local_Hypot_Aprovadas_L3) >= 10000):
                            self.Hypot_Aprovadas_L3 = int(local_Hypot_Aprovadas_L3) - 10000
                            self.lcd_hy_ap_l3.setProperty("value", int(self.Hypot_Aprovadas_L3))

                        if (int(local_Hypot_Reprovadas_L3) >= 12000):
                            self.Hypot_Reprovadas_L3 = int(local_Hypot_Reprovadas_L3) - 12000
                            self.lcd_hy_rep_l3.setProperty("value", int(self.Hypot_Reprovadas_L3))

                        self.subscriber_mesa_3.stop()
                        self.subscriber_est_3_ap.stop()
                        self.subscriber_est_3_rep.stop()
                        self.subscriber_hy_3_ap.stop()
                        self.subscriber_hy_3_rep.stop()

                except Exception as e:

                        print("Error Linha 3")

                        self.tempo_servidor_offiline = self.tempo_servidor_offiline + 1












        start_thread_l3 = threading.Thread(target=start_subscriber_l3)

        # Inicie o thread
        start_thread_l3.start()







    def atualiza_linha_4(self):

        def start_subscriber_l4():


            try:


                    self.subscriber_mesa_4.start()
                    self.subscriber_est_4_ap.start()
                    self.subscriber_est_4_rep.start()
                    self.subscriber_hy_4_ap.start()
                    self.subscriber_hy_4_rep.start()

                    local_Mesa_de_Montagem_L4 = self.subscriber_mesa_4.get_value()
                    local_Estanquiedade_Aprovadas_L4 = self.subscriber_est_4_ap.get_value()
                    local_Estanquiedade_Reprovadas_L4 = self.subscriber_est_4_rep.get_value()
                    local_Hypot_Aprovadas_L4 = self.subscriber_hy_4_ap.get_value()
                    local_Hypot_Reprovadas_L4 = self.subscriber_hy_4_rep.get_value()

                    if (int(local_Mesa_de_Montagem_L4) >= 1000):
                        self.Mesa_de_Montagem_L4 = int(local_Mesa_de_Montagem_L4) - 1000
                        self.lcd_mesa_l4.setProperty("value", int(self.Mesa_de_Montagem_L4))

                    if (int(local_Estanquiedade_Aprovadas_L4) >= 2000):
                        self.Estanquiedade_Aprovadas_L4 = int(local_Estanquiedade_Aprovadas_L4) - 2000
                        self.lcd_est_ap_l4.setProperty("value", int(self.Estanquiedade_Aprovadas_L4))

                    if (int(local_Estanquiedade_Reprovadas_L4) >= 4000):
                        self.Estanquiedade_Reprovadas_L4 = int(local_Estanquiedade_Reprovadas_L4) - 4000
                        self.lcd_est_rep_l4.setProperty("value", int(self.Estanquiedade_Reprovadas_L4))

                    if (int(local_Hypot_Aprovadas_L4) >= 10000):
                        self.Hypot_Aprovadas_L4 = int(local_Hypot_Aprovadas_L4) - 10000
                        self.lcd_hy_ap_l4.setProperty("value", int(self.Hypot_Aprovadas_L4))

                    if (int(local_Hypot_Reprovadas_L4) >= 12000):
                        self.Hypot_Reprovadas_L4 = int(local_Hypot_Reprovadas_L4) - 12000
                        self.lcd_hy_rep_l4.setProperty("value", int(self.Hypot_Reprovadas_L4))

                    self.subscriber_mesa_4.stop()
                    self.subscriber_est_4_ap.stop()
                    self.subscriber_est_4_rep.stop()
                    self.subscriber_hy_4_ap.stop()
                    self.subscriber_hy_4_rep.stop()


                    if(self.tempo_servidor_offiline > 0):
                        self.tempo_servidor_offiline = self.tempo_servidor_offiline - 1

            except Exception as e:

                    print("Error linha 4")

                    self.tempo_servidor_offiline = self.tempo_servidor_offiline + 1






        start_thread_l4 = threading.Thread(target=start_subscriber_l4)

        # Inicie o thread
        start_thread_l4.start()
















    def compara_contagem_programada_real(self):



            def verifica_servidor():
                print(f'Contagem Erro servidor {self.tempo_servidor_offiline}')


                if (self.tempo_servidor_offiline > 4):

                        print("Desativa Tudo")

                        self.subscriber_mesa_1.stop()
                        self.subscriber_est_1_ap.stop()
                        self.subscriber_est_1_rep.stop()
                        self.subscriber_pre_1_ap.stop()
                        self.subscriber_pre_1_rep.stop()
                        self.subscriber_hy_1_ap.stop()
                        self.subscriber_hy_1_rep.stop()


                        self.subscriber_mesa_2.stop()
                        self.subscriber_est_2_ap.stop()
                        self.subscriber_est_2_rep.stop()
                        self.subscriber_pre_2_ap.stop()
                        self.subscriber_pre_2_rep.stop()
                        self.subscriber_hy_2_ap.stop()
                        self.subscriber_hy_2_rep.stop()

                        self.subscriber_mesa_3.stop()
                        self.subscriber_est_3_ap.stop()
                        self.subscriber_est_3_rep.stop()
                        self.subscriber_hy_3_ap.stop()
                        self.subscriber_hy_3_rep.stop()

                        self.subscriber_mesa_4.stop()
                        self.subscriber_est_4_ap.stop()
                        self.subscriber_est_4_rep.stop()
                        self.subscriber_hy_4_ap.stop()
                        self.subscriber_hy_4_rep.stop()


                        self.subscriber_op_L1.stop()
                        self.subscriber_op_L1.stop()
                        self.subscriber_op_L1.stop()
                        self.subscriber_op_L1.stop()


                        self.tempo_servidor_offiline = 0





                if (self.tempo_servidor_offiline < 1):

                        self.status_servidor.setText(QCoreApplication.translate("MainWindow", u"Conectado", None))
                        self.status_servidor.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n""color: rgb(0, 128, 0);\n"u"background-color: rgb(0, 1, 1);")

                else:
                        self.status_servidor.setText(QCoreApplication.translate("MainWindow", u"Error", None))
                        self.status_servidor.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 0, 0);\n"u"background-color: rgb(0, 1, 1);")






            def publicacao_linha_1():

                    if (self.sistema_iniciado_linha_1 == True):

                            if (self.estado_controle_sistema_linha_1 == True):

                                    self.subscriber_op_L1.start()

                                    if (int(self.contagem_projetada_linha_1) > self.Mesa_de_Montagem_L1):
                                            self.subscriber_op_L1.publish_message("3")
                                            print("Atrasado")

                                    if (int(self.contagem_projetada_linha_1) == self.Mesa_de_Montagem_L1):
                                            self.subscriber_op_L1.publish_message("2")
                                            print("Na Meta")

                                    if (int(self.contagem_projetada_linha_1) < self.Mesa_de_Montagem_L1):
                                            self.subscriber_op_L1.publish_message("1")
                                            print("Adiantado")



                                    self.subscriber_op_L1.stop()

                            if (self.estado_controle_sistema_linha_1 == False):

                                    self.subscriber_op_L1.start()
                                    self.subscriber_op_L1.publish_message("4")
                                    self.subscriber_op_L1.stop()

                    if (self.sistema_iniciado_linha_1 == False):

                            self.subscriber_op_L1.start()
                            self.subscriber_op_L1.publish_message("4")
                            self.subscriber_op_L1.stop()




            def publicacao_linha_2():

                    if (self.sistema_iniciado_linha_2 == True):

                            if (self.estado_controle_sistema_linha_2 == True):

                                    self.subscriber_op_L2.start()

                                    if (int(self.contagem_projetada_linha_2) > self.Mesa_de_Montagem_L2):
                                            self.subscriber_op_L2.publish_message("3")
                                            print("Atrasado")

                                    if (int(self.contagem_projetada_linha_2) == self.Mesa_de_Montagem_L2):
                                            self.subscriber_op_L2.publish_message("2")
                                            print("Na Meta")

                                    if (int(self.contagem_projetada_linha_2) < self.Mesa_de_Montagem_L2):
                                            self.subscriber_op_L2.publish_message("1")
                                            print("Adiantado")

                                    self.subscriber_op_L2.stop()

                            if (self.estado_controle_sistema_linha_2 == False):
                                    self.subscriber_op_L2.start()
                                    self.subscriber_op_L2.publish_message("4")
                                    self.subscriber_op_L2.stop()

                    if (self.sistema_iniciado_linha_2 == False):
                            self.subscriber_op_L2.start()
                            self.subscriber_op_L2.publish_message("4")
                            self.subscriber_op_L2.stop()





            def publicacao_linha_3():

                    if (self.sistema_iniciado_linha_3 == True):

                            if (self.estado_controle_sistema_linha_3 == True):

                                    self.subscriber_op_L3.start()

                                    if (int(self.contagem_projetada_linha_3) > self.Mesa_de_Montagem_L3):
                                            self.subscriber_op_L3.publish_message("3")
                                            print("Atrasado")

                                    if (int(self.contagem_projetada_linha_3) == self.Mesa_de_Montagem_L3):
                                            self.subscriber_op_L3.publish_message("2")
                                            print("Na Meta")

                                    if (int(self.contagem_projetada_linha_3) < self.Mesa_de_Montagem_L3):
                                            self.subscriber_op_L3.publish_message("1")
                                            print("Adiantado")

                                    self.subscriber_op_L3.stop()

                            if (self.estado_controle_sistema_linha_3 == False):
                                    self.subscriber_op_L3.start()
                                    self.subscriber_op_L3.publish_message("4")
                                    self.subscriber_op_L3.stop()

                    if (self.sistema_iniciado_linha_3 == False):
                            self.subscriber_op_L3.start()
                            self.subscriber_op_L3.publish_message("4")
                            self.subscriber_op_L3.stop()


            def publicacao_linha_4():

                    if (self.sistema_iniciado_linha_4 == True):

                            if (self.estado_controle_sistema_linha_4 == True):

                                    self.subscriber_op_L4.start()

                                    if (int(self.contagem_projetada_linha_4) > self.Mesa_de_Montagem_L4):
                                            self.subscriber_op_L4.publish_message("3")
                                            print("Atrasado")

                                    if (int(self.contagem_projetada_linha_4) == self.Mesa_de_Montagem_L4):
                                            self.subscriber_op_L4.publish_message("2")
                                            print("Na Meta")

                                    if (int(self.contagem_projetada_linha_4) < self.Mesa_de_Montagem_L4):
                                            self.subscriber_op_L4.publish_message("1")
                                            print("Adiantado")

                                    self.subscriber_op_L4.stop()

                            if (self.estado_controle_sistema_linha_4 == False):
                                    self.subscriber_op_L4.start()
                                    self.subscriber_op_L4.publish_message("4")
                                    self.subscriber_op_L4.stop()

                    if (self.sistema_iniciado_linha_4 == False):
                            self.subscriber_op_L4.start()
                            self.subscriber_op_L4.publish_message("4")
                            self.subscriber_op_L4.stop()



            def varredura_linha_1():



                    if ((self.inicio_turno_l1 == hora_minuto_atual) and (self.sistema_ativado_l1 == True) and (self.sistema_iniciado_linha_1 == False) and (self.segundo_turno_start == False)):

                            self.primeiro_turno_start = True
                            self.sistema_iniciado_linha_1 = True
                            self.estado_controle_sistema_linha_1 = True
                            self.contagem_projetada_linha_1 = 0
                            self.tempo_acumulado_l1 = 0
                            self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_1}")

                            print("INICIO PRIMEIRO TURNO")

                    if(self.sistema_iniciado_linha_1 == True):


                            if ((self.inicio_intervalo_l1 == hora_minuto_atual) and (self.estado_controle_sistema_linha_1 == True)):

                                    if (self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = (hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l1}")

                            if (self.final_intervalo_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.inicio_laboral_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l1}")


                            if (self.final_laboral_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.inicio_almoco_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l1}")


                            if (self.final_almoco_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.final_turno_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.contagem_projetada_linha_1 = self.meta_linha_1_manha_registro
                                    self.estado_controle_sistema_linha_1 = False

                                    self.sistema_iniciado_linha_1 = False
                                    self.primeiro_turno_start = False
                                    print("Final  1 Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l1}")






                    if ((self.inicio_turno_l1_2 == hora_minuto_atual) and (self.sistema_ativado_l1 == True) and (self.sistema_iniciado_linha_1 == False) and (self.primeiro_turno_start == False)):

                            self.segundo_turno_start = True
                            self.sistema_iniciado_linha_1 = True
                            self.estado_controle_sistema_linha_1 = True
                            self.contagem_projetada_linha_1 = 0
                            self.tempo_acumulado_l1 = 0
                            self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()

                            print("INICIO SEGUNDO TURNO")

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_1}")

                    if(self.sistema_iniciado_linha_1 == True):


                            if ((self.inicio_intervalo_l1_2 == hora_minuto_atual) and (self.estado_controle_sistema_linha_1 == True)):

                                    if (self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = (hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l1}")

                            if (self.final_intervalo_l1_2 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.inicio_laboral_l1_2 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l1}")


                            if (self.final_laboral_l1_2 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.inicio_janta_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.estado_controle_sistema_linha_1 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l1}")


                            if (self.final_janta_l1 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == False):

                                    self.estado_controle_sistema_linha_1 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_1 = datetime.datetime.now()


                            if (self.final_turno_l1_2 == hora_minuto_atual and self.estado_controle_sistema_linha_1 == True):

                                    if(self.estado_controle_sistema_linha_1 == True):
                                            self.tempo_acumulado_l1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1

                                    self.contagem_projetada_linha_1 = self.meta_linha_1_tarde_registro
                                    self.estado_controle_sistema_linha_1 = False

                                    self.sistema_iniciado_linha_1 = False
                                    self.segundo_turno_start = False
                                    print("Final Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l1}")


                    self.lcd_cont_p_l1.setProperty("value", int(self.contagem_projetada_linha_1))


                    if (self.estado_controle_sistema_linha_1 == True):
                            self.status_l1.setText(
                                    QCoreApplication.translate("MainWindow", u"Rodando", None))
                            self.status_l1.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(0, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                    if (self.estado_controle_sistema_linha_1 == False):
                            self.status_l1.setText(
                                    QCoreApplication.translate("MainWindow", u"Parado", None))
                            self.status_l1.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")





                    if(self.sistema_iniciado_linha_1 == True and self.estado_controle_sistema_linha_1 == True):


                            self.contagem_projetada_linha_1 = ((hora_atual - self.hora_de_inicio_sistema_linha_1).total_seconds()) + self.tempo_acumulado_l1
                            print(self.contagem_projetada_linha_1)


                            if (self.primeiro_turno_start == True):

                                self.contagem_projetada_linha_1 = self.contagem_projetada_linha_1 / self.tempo_estimado_por_peca_l1_1



                            if (self.segundo_turno_start == True):

                                self.contagem_projetada_linha_1 = self.contagem_projetada_linha_1 / self.tempo_estimado_por_peca_l1_2









            def varredura_linha_2():



                    if ((self.inicio_turno_l2 == hora_minuto_atual) and (self.sistema_ativado_l2 == True) and (self.sistema_iniciado_linha_2 == False) and (self.segundo_turno_start_l2 == False)):

                            self.primeiro_turno_start_l2 = True
                            self.sistema_iniciado_linha_2 = True
                            self.estado_controle_sistema_linha_2 = True
                            self.contagem_projetada_linha_2 = 0
                            self.tempo_acumulado_l2 = 0
                            self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_2}")

                            print("INICIO PRIMEIRO TURNO")

                    if(self.sistema_iniciado_linha_2 == True):


                            if ((self.inicio_intervalo_l2 == hora_minuto_atual) and (self.estado_controle_sistema_linha_2 == True)):

                                    if (self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = (hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l2}")

                            if (self.final_intervalo_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.inicio_laboral_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l2}")


                            if (self.final_laboral_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.inicio_almoco_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l1}")


                            if (self.final_almoco_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.final_turno_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.contagem_projetada_linha_2 = self.meta_linha_2_manha_registro
                                    self.estado_controle_sistema_linha_2 = False

                                    self.sistema_iniciado_linha_2 = False
                                    self.primeiro_turno_start_l2 = False
                                    print("Final  1 Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l2}")






                    if ((self.inicio_turno_l2_2 == hora_minuto_atual) and (self.sistema_ativado_l2 == True) and (self.sistema_iniciado_linha_2 == False) and (self.primeiro_turno_start_l2 == False)):

                            self.segundo_turno_start_l2 = True
                            self.sistema_iniciado_linha_2 = True
                            self.estado_controle_sistema_linha_2 = True
                            self.contagem_projetada_linha_2 = 0
                            self.tempo_acumulado_l2 = 0
                            self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()

                            print("INICIO SEGUNDO TURNO")

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_2}")

                    if(self.sistema_iniciado_linha_2 == True):


                            if ((self.inicio_intervalo_l2_2 == hora_minuto_atual) and (self.estado_controle_sistema_linha_2 == True)):

                                    if (self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = (hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l2}")

                            if (self.final_intervalo_l2_2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.inicio_laboral_l2_2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l2}")


                            if (self.final_laboral_l2_2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.inicio_janta_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.estado_controle_sistema_linha_2 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l2}")


                            if (self.final_janta_l2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == False):

                                    self.estado_controle_sistema_linha_2 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_2 = datetime.datetime.now()


                            if (self.final_turno_l2_2 == hora_minuto_atual and self.estado_controle_sistema_linha_2 == True):

                                    if(self.estado_controle_sistema_linha_2 == True):
                                            self.tempo_acumulado_l2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2

                                    self.contagem_projetada_linha_2 = self.meta_linha_2_tarde_registro
                                    self.estado_controle_sistema_linha_2 = False

                                    self.sistema_iniciado_linha_2 = False
                                    self.segundo_turno_start_l2 = False
                                    print("Final Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l2}")


                    self.lcd_cont_p_l2.setProperty("value", int(self.contagem_projetada_linha_2))

                    if (self.estado_controle_sistema_linha_2 == True):
                            self.status_l2.setText(
                                    QCoreApplication.translate("MainWindow", u"Rodando", None))
                            self.status_l2.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(0, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                    if (self.estado_controle_sistema_linha_2 == False):
                            self.status_l2.setText(
                                    QCoreApplication.translate("MainWindow", u"Parado", None))
                            self.status_l2.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")


                    if(self.sistema_iniciado_linha_2 == True and self.estado_controle_sistema_linha_2 == True):


                            self.contagem_projetada_linha_2 = ((hora_atual - self.hora_de_inicio_sistema_linha_2).total_seconds()) + self.tempo_acumulado_l2
                            print(self.contagem_projetada_linha_2)


                            if (self.primeiro_turno_start_l2 == True):

                                self.contagem_projetada_linha_2 = self.contagem_projetada_linha_2 / self.tempo_estimado_por_peca_l2_1




                            if (self.segundo_turno_start_l2 == True):

                                self.contagem_projetada_linha_2 = self.contagem_projetada_linha_2 / self.tempo_estimado_por_peca_l2_2





            def varredura_linha_3():



                    if ((self.inicio_turno_l3 == hora_minuto_atual) and (self.sistema_ativado_l3 == True) and (self.sistema_iniciado_linha_3 == False) and (self.segundo_turno_start_l3 == False)):

                            self.primeiro_turno_start_l3 = True
                            self.sistema_iniciado_linha_3 = True
                            self.estado_controle_sistema_linha_3 = True
                            self.contagem_projetada_linha_3 = 0
                            self.tempo_acumulado_l3 = 0
                            self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_3}")

                            print("INICIO PRIMEIRO TURNO")

                    if(self.sistema_iniciado_linha_3 == True):


                            if ((self.inicio_intervalo_l3 == hora_minuto_atual) and (self.estado_controle_sistema_linha_3 == True)):

                                    if (self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = (hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l3}")

                            if (self.final_intervalo_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.inicio_laboral_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l3}")


                            if (self.final_laboral_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.inicio_almoco_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l3}")


                            if (self.final_almoco_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.final_turno_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.contagem_projetada_linha_3 = self.meta_linha_3_manha_registro
                                    self.estado_controle_sistema_linha_3 = False

                                    self.sistema_iniciado_linha_3 = False
                                    self.primeiro_turno_start_l3 = False
                                    print("Final  1 Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l3}")






                    if ((self.inicio_turno_l3_2 == hora_minuto_atual) and (self.sistema_ativado_l3 == True) and (self.sistema_iniciado_linha_3 == False) and (self.primeiro_turno_start_l3 == False)):

                            self.segundo_turno_start_l3 = True
                            self.sistema_iniciado_linha_3 = True
                            self.estado_controle_sistema_linha_3 = True
                            self.contagem_projetada_linha_3 = 0
                            self.tempo_acumulado_l3 = 0
                            self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()

                            print("INICIO SEGUNDO TURNO")

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_3}")

                    if(self.sistema_iniciado_linha_3 == True):


                            if ((self.inicio_intervalo_l3_2 == hora_minuto_atual) and (self.estado_controle_sistema_linha_3 == True)):

                                    if (self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = (hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l3}")

                            if (self.final_intervalo_l3_2 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.inicio_laboral_l3_2 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l3}")


                            if (self.final_laboral_l3_2 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.inicio_janta_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.estado_controle_sistema_linha_3 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l3}")


                            if (self.final_janta_l3 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == False):

                                    self.estado_controle_sistema_linha_3 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_3 = datetime.datetime.now()


                            if (self.final_turno_l3_2 == hora_minuto_atual and self.estado_controle_sistema_linha_3 == True):

                                    if(self.estado_controle_sistema_linha_3 == True):
                                            self.tempo_acumulado_l3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3

                                    self.contagem_projetada_linha_3 = self.meta_linha_3_tarde_registro
                                    self.estado_controle_sistema_linha_3 = False

                                    self.sistema_iniciado_linha_3 = False
                                    self.segundo_turno_start_l3 = False
                                    print("Final Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l3}")


                    self.lcd_cont_prog_l3.setProperty("value", int(self.contagem_projetada_linha_3))

                    if (self.estado_controle_sistema_linha_3 == True):
                            self.status_l3.setText(
                                    QCoreApplication.translate("MainWindow", u"Rodando", None))
                            self.status_l3.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(0, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                    if (self.estado_controle_sistema_linha_3 == False):
                            self.status_l3.setText(
                                    QCoreApplication.translate("MainWindow", u"Parado", None))
                            self.status_l3.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")


                    if(self.sistema_iniciado_linha_3 == True and self.estado_controle_sistema_linha_3 == True):


                            self.contagem_projetada_linha_3 = ((hora_atual - self.hora_de_inicio_sistema_linha_3).total_seconds()) + self.tempo_acumulado_l3
                            print(self.contagem_projetada_linha_3)


                            if (self.primeiro_turno_start_l3 == True):

                                self.contagem_projetada_linha_3 = self.contagem_projetada_linha_3 / self.tempo_estimado_por_peca_l3_1




                            if (self.segundo_turno_start_l3 == True):

                                self.contagem_projetada_linha_3 = self.contagem_projetada_linha_3 / self.tempo_estimado_por_peca_l3_2



            def varredura_linha_4():



                    if ((self.inicio_turno_l4 == hora_minuto_atual) and (self.sistema_ativado_l4 == True) and (self.sistema_iniciado_linha_4 == False) and (self.segundo_turno_start_l4 == False)):

                            self.primeiro_turno_start_l4 = True
                            self.sistema_iniciado_linha_4 = True
                            self.estado_controle_sistema_linha_4 = True
                            self.contagem_projetada_linha_4 = 0
                            self.tempo_acumulado_l4 = 0
                            self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_4}")

                            print("INICIO PRIMEIRO TURNO")

                    if(self.sistema_iniciado_linha_4 == True):


                            if ((self.inicio_intervalo_l4 == hora_minuto_atual) and (self.estado_controle_sistema_linha_4 == True)):

                                    if (self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = (hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l4}")

                            if (self.final_intervalo_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.inicio_laboral_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l4}")


                            if (self.final_laboral_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.inicio_almoco_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l4}")


                            if (self.final_almoco_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.final_turno_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.contagem_projetada_linha_4 = self.meta_linha_4_manha_registro
                                    self.estado_controle_sistema_linha_4 = False

                                    self.sistema_iniciado_linha_4 = False
                                    self.primeiro_turno_start_l4 = False
                                    print("Final  1 Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l4}")






                    if ((self.inicio_turno_l4_2 == hora_minuto_atual) and (self.sistema_ativado_l4 == True) and (self.sistema_iniciado_linha_4 == False) and (self.primeiro_turno_start_l4 == False)):

                            self.segundo_turno_start_l4 = True
                            self.sistema_iniciado_linha_4 = True
                            self.estado_controle_sistema_linha_4 = True
                            self.contagem_projetada_linha_4 = 0
                            self.tempo_acumulado_l4 = 0
                            self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()

                            print("INICIO SEGUNDO TURNO")

                            print(f"hora de incicio:  {self.hora_de_inicio_sistema_linha_4}")

                    if(self.sistema_iniciado_linha_4 == True):


                            if ((self.inicio_intervalo_l4_2 == hora_minuto_atual) and (self.estado_controle_sistema_linha_4 == True)):

                                    if (self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = (hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Pausa para intervalo ")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l4}")

                            if (self.final_intervalo_l4_2 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do intevalo")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.inicio_laboral_l4_2 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Pausa para Inicio Laboral")
                                    print(f"Tempo acumulado até agora: {self.tempo_acumulado_l4}")


                            if (self.final_laboral_l4_2 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do Laboral")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.inicio_janta_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.estado_controle_sistema_linha_4 = False
                                    print("Inicio Almoço")
                                    print(f"Tempo acumuladora até agora: {self.tempo_acumulado_l4}")


                            if (self.final_janta_l4 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == False):

                                    self.estado_controle_sistema_linha_4 = True
                                    print("Volta do almoço")
                                    self.hora_de_inicio_sistema_linha_4 = datetime.datetime.now()


                            if (self.final_turno_l4_2 == hora_minuto_atual and self.estado_controle_sistema_linha_4 == True):

                                    if(self.estado_controle_sistema_linha_4 == True):
                                            self.tempo_acumulado_l4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4

                                    self.contagem_projetada_linha_4 = self.meta_linha_4_tarde_registro
                                    self.estado_controle_sistema_linha_4 = False

                                    self.sistema_iniciado_linha_4 = False
                                    self.segundo_turno_start_l4 = False
                                    print("Final Turno")
                                    print(f"Tempo acumuladora total : {self.tempo_acumulado_l4}")


                    self.lcd_cont_p_l4.setProperty("value", int(self.contagem_projetada_linha_4))

                    if (self.estado_controle_sistema_linha_4 == True):
                            self.status_l4.setText(
                                    QCoreApplication.translate("MainWindow", u"Rodando", None))
                            self.status_l4.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(0, 200, 0);\n"u"background-color: rgb(61, 61, 61);")

                    if (self.estado_controle_sistema_linha_4 == False):
                            self.status_l4.setText(
                                    QCoreApplication.translate("MainWindow", u"Parado", None))
                            self.status_l4.setStyleSheet(
                                    u"font: 700 12pt \"Segoe UI\";\n""color: rgb(200, 200, 0);\n"u"background-color: rgb(61, 61, 61);")


                    if(self.sistema_iniciado_linha_4 == True and self.estado_controle_sistema_linha_4 == True):


                            self.contagem_projetada_linha_4 = ((hora_atual - self.hora_de_inicio_sistema_linha_4).total_seconds()) + self.tempo_acumulado_l4
                            print(self.contagem_projetada_linha_4)


                            if (self.primeiro_turno_start_l4 == True):

                                self.contagem_projetada_linha_4 = self.contagem_projetada_linha_4 / self.tempo_estimado_por_peca_l4_1




                            if (self.segundo_turno_start_l4 == True):

                                self.contagem_projetada_linha_4 = self.contagem_projetada_linha_4 / self.tempo_estimado_por_peca_l4_2








            hora_atual = datetime.datetime.now()
            hora_minuto_atual = hora_atual.strftime("%H:%M:00")

            verifica_servidor()



            if (self.sistema_ativado_l1 == True):



                varredura_linha_1()

                start_sistema_mesa_l1 = threading.Thread(target=publicacao_linha_1())

                    # Inicie o thread
                start_sistema_mesa_l1.start()




            if (self.sistema_ativado_l2 == True):


                varredura_linha_2()

                start_sistema_mesa_l2 = threading.Thread(target=publicacao_linha_2())

                    # Inicie o thread
                start_sistema_mesa_l2.start()



            if (self.sistema_ativado_l3 == True):


                varredura_linha_3()

                start_sistema_mesa_l3 = threading.Thread(target=publicacao_linha_3())

                    # Inicie o thread
                start_sistema_mesa_l3.start()



            if (self.sistema_ativado_l4 == True):



                varredura_linha_4()

                start_sistema_mesa_l4 = threading.Thread(target=publicacao_linha_4())

                    # Inicie o thread
                start_sistema_mesa_l4.start()















































































