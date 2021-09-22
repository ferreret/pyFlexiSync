# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 259)
        MainWindow.setMinimumSize(QSize(800, 259))
        MainWindow.setMaximumSize(QSize(800, 259))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gbSourceFolders = QGroupBox(self.centralwidget)
        self.gbSourceFolders.setObjectName(u"gbSourceFolders")
        sizePolicy.setHeightForWidth(self.gbSourceFolders.sizePolicy().hasHeightForWidth())
        self.gbSourceFolders.setSizePolicy(sizePolicy)
        self.formLayout_2 = QFormLayout(self.gbSourceFolders)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formSourceFolders = QFormLayout()
        self.formSourceFolders.setObjectName(u"formSourceFolders")
        self.formSourceFolders.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.txtProgramFilesSourceFolder = QLineEdit(self.gbSourceFolders)
        self.txtProgramFilesSourceFolder.setObjectName(u"txtProgramFilesSourceFolder")

        self.formSourceFolders.setWidget(0, QFormLayout.FieldRole, self.txtProgramFilesSourceFolder)

        self.lblProgramDataSourceFolder = QLabel(self.gbSourceFolders)
        self.lblProgramDataSourceFolder.setObjectName(u"lblProgramDataSourceFolder")

        self.formSourceFolders.setWidget(1, QFormLayout.LabelRole, self.lblProgramDataSourceFolder)

        self.txtProgramDataSourceFolder = QLineEdit(self.gbSourceFolders)
        self.txtProgramDataSourceFolder.setObjectName(u"txtProgramDataSourceFolder")

        self.formSourceFolders.setWidget(1, QFormLayout.FieldRole, self.txtProgramDataSourceFolder)

        self.lblProgramFilesSourceFolder = QLabel(self.gbSourceFolders)
        self.lblProgramFilesSourceFolder.setObjectName(u"lblProgramFilesSourceFolder")

        self.formSourceFolders.setWidget(0, QFormLayout.LabelRole, self.lblProgramFilesSourceFolder)


        self.formLayout_2.setLayout(0, QFormLayout.SpanningRole, self.formSourceFolders)


        self.verticalLayout.addWidget(self.gbSourceFolders)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_4 = QFormLayout(self.groupBox_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lblProgramFilesTargetFolder = QLabel(self.groupBox_2)
        self.lblProgramFilesTargetFolder.setObjectName(u"lblProgramFilesTargetFolder")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lblProgramFilesTargetFolder)

        self.txtProgramFilesTargetFolder = QLineEdit(self.groupBox_2)
        self.txtProgramFilesTargetFolder.setObjectName(u"txtProgramFilesTargetFolder")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.txtProgramFilesTargetFolder)

        self.txtProgramDataTargetFolder = QLineEdit(self.groupBox_2)
        self.txtProgramDataTargetFolder.setObjectName(u"txtProgramDataTargetFolder")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.txtProgramDataTargetFolder)

        self.lblProgramDataTargetFolder = QLabel(self.groupBox_2)
        self.lblProgramDataTargetFolder.setObjectName(u"lblProgramDataTargetFolder")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.lblProgramDataTargetFolder)


        self.formLayout_4.setLayout(0, QFormLayout.SpanningRole, self.formLayout_3)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnStart = QPushButton(self.centralwidget)
        self.btnStart.setObjectName(u"btnStart")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnQuit = QPushButton(self.centralwidget)
        self.btnQuit.setObjectName(u"btnQuit")
        sizePolicy1.setHeightForWidth(self.btnQuit.sizePolicy().hasHeightForWidth())
        self.btnQuit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.btnQuit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sincronizador de carpetas de FlexibarNET", None))
        self.gbSourceFolders.setTitle(QCoreApplication.translate("MainWindow", u"Source Folders", None))
        self.lblProgramDataSourceFolder.setText(QCoreApplication.translate("MainWindow", u"Program Data:", None))
        self.lblProgramFilesSourceFolder.setText(QCoreApplication.translate("MainWindow", u"Program Files:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Target Folders", None))
        self.lblProgramFilesTargetFolder.setText(QCoreApplication.translate("MainWindow", u"Program Files:", None))
        self.lblProgramDataTargetFolder.setText(QCoreApplication.translate("MainWindow", u"Program Data:", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
    # retranslateUi

