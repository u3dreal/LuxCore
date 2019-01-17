# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './luxcorerender/LuxCore/src/pyluxcoretools/pyluxcoretools/pyluxcorenetconsole/mainwindow.ui',
# licensing of './luxcorerender/LuxCore/src/pyluxcoretools/pyluxcoretools/pyluxcorenetconsole/mainwindow.ui' applies.
#
# Created: Sat Jan 12 17:36:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidgetMain = QtWidgets.QTabWidget(self.splitter)
        self.tabWidgetMain.setObjectName("tabWidgetMain")
        self.currentJob = QtWidgets.QWidget()
        self.currentJob.setObjectName("currentJob")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.currentJob)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.currentJob)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -134, 742, 595))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.labelRenderCfgFileName = QtWidgets.QLabel(self.groupBox)
        self.labelRenderCfgFileName.setText("")
        self.labelRenderCfgFileName.setObjectName("labelRenderCfgFileName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.labelRenderCfgFileName)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.labelFilmFileName = QtWidgets.QLabel(self.groupBox)
        self.labelFilmFileName.setText("")
        self.labelFilmFileName.setObjectName("labelFilmFileName")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.labelFilmFileName)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.labelImageFileName = QtWidgets.QLabel(self.groupBox)
        self.labelImageFileName.setText("")
        self.labelImageFileName.setObjectName("labelImageFileName")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.labelImageFileName)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.labelWorkDirectory = QtWidgets.QLabel(self.groupBox)
        self.labelWorkDirectory.setText("")
        self.labelWorkDirectory.setObjectName("labelWorkDirectory")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.labelWorkDirectory)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.labelStartTime = QtWidgets.QLabel(self.groupBox)
        self.labelStartTime.setText("")
        self.labelStartTime.setObjectName("labelStartTime")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.labelStartTime)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.labelRenderingTime = QtWidgets.QLabel(self.groupBox)
        self.labelRenderingTime.setText("")
        self.labelRenderingTime.setObjectName("labelRenderingTime")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.labelRenderingTime)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.labelSamplesPixel = QtWidgets.QLabel(self.groupBox)
        self.labelSamplesPixel.setText("")
        self.labelSamplesPixel.setObjectName("labelSamplesPixel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.labelSamplesPixel)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.labelSamplesSec = QtWidgets.QLabel(self.groupBox)
        self.labelSamplesSec.setText("")
        self.labelSamplesSec.setObjectName("labelSamplesSec")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.labelSamplesSec)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditHaltSPP = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltSPP.sizePolicy().hasHeightForWidth())
        self.lineEditHaltSPP.setSizePolicy(sizePolicy)
        self.lineEditHaltSPP.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltSPP.setObjectName("lineEditHaltSPP")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditHaltSPP)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditHaltTime = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditHaltTime.sizePolicy().hasHeightForWidth())
        self.lineEditHaltTime.setSizePolicy(sizePolicy)
        self.lineEditHaltTime.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditHaltTime.setObjectName("lineEditHaltTime")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditHaltTime)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditFilmUpdatePeriod = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilmUpdatePeriod.sizePolicy().hasHeightForWidth())
        self.lineEditFilmUpdatePeriod.setSizePolicy(sizePolicy)
        self.lineEditFilmUpdatePeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditFilmUpdatePeriod.setObjectName("lineEditFilmUpdatePeriod")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditFilmUpdatePeriod)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditStatsPeriod = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditStatsPeriod.sizePolicy().hasHeightForWidth())
        self.lineEditStatsPeriod.setSizePolicy(sizePolicy)
        self.lineEditStatsPeriod.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditStatsPeriod.setObjectName("lineEditStatsPeriod")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditStatsPeriod)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonForceFilmMerge = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonForceFilmMerge.setObjectName("pushButtonForceFilmMerge")
        self.gridLayout_2.addWidget(self.pushButtonForceFilmMerge, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 4, 1, 1)
        self.pushButtonForceFilmDownload = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonForceFilmDownload.setObjectName("pushButtonForceFilmDownload")
        self.gridLayout_2.addWidget(self.pushButtonForceFilmDownload, 0, 1, 1, 1)
        self.pushButtonFinishJob = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonFinishJob.setObjectName("pushButtonFinishJob")
        self.gridLayout_2.addWidget(self.pushButtonFinishJob, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_4)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 696, 76))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelRenderingImage = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.labelRenderingImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelRenderingImage.setObjectName("labelRenderingImage")
        self.gridLayout_5.addWidget(self.labelRenderingImage, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.tabWidgetMain.addTab(self.currentJob, "")
        self.queuedJobs = QtWidgets.QWidget()
        self.queuedJobs.setObjectName("queuedJobs")
        self.gridLayout = QtWidgets.QGridLayout(self.queuedJobs)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.pushButtonAddJob = QtWidgets.QPushButton(self.queuedJobs)
        self.pushButtonAddJob.setObjectName("pushButtonAddJob")
        self.gridLayout.addWidget(self.pushButtonAddJob, 1, 1, 1, 1)
        self.scrollAreaQueuedJobs = QtWidgets.QScrollArea(self.queuedJobs)
        self.scrollAreaQueuedJobs.setWidgetResizable(True)
        self.scrollAreaQueuedJobs.setObjectName("scrollAreaQueuedJobs")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 758, 374))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaQueuedJobs.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollAreaQueuedJobs, 0, 0, 1, 4)
        self.pushButtonRemovePendingJobs = QtWidgets.QPushButton(self.queuedJobs)
        self.pushButtonRemovePendingJobs.setObjectName("pushButtonRemovePendingJobs")
        self.gridLayout.addWidget(self.pushButtonRemovePendingJobs, 1, 2, 1, 1)
        self.tabWidgetMain.addTab(self.queuedJobs, "")
        self.nodes = QtWidgets.QWidget()
        self.nodes.setObjectName("nodes")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.nodes)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 1, 3, 1, 1)
        self.pushButtonAddNode = QtWidgets.QPushButton(self.nodes)
        self.pushButtonAddNode.setObjectName("pushButtonAddNode")
        self.gridLayout_3.addWidget(self.pushButtonAddNode, 1, 1, 1, 1)
        self.scrollAreaNodes = QtWidgets.QScrollArea(self.nodes)
        self.scrollAreaNodes.setWidgetResizable(True)
        self.scrollAreaNodes.setObjectName("scrollAreaNodes")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 758, 374))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaNodes.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.addWidget(self.scrollAreaNodes, 0, 0, 1, 4)
        self.pushButtonRefreshNodesList = QtWidgets.QPushButton(self.nodes)
        self.pushButtonRefreshNodesList.setObjectName("pushButtonRefreshNodesList")
        self.gridLayout_3.addWidget(self.pushButtonRefreshNodesList, 1, 2, 1, 1)
        self.tabWidgetMain.addTab(self.nodes, "")
        self.textEditLog = QtWidgets.QTextEdit(self.splitter)
        self.textEditLog.setUndoRedoEnabled(False)
        self.textEditLog.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEditLog.setReadOnly(True)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidgetMain.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("activated()"), MainWindow.clickedQuit)
        QtCore.QObject.connect(self.pushButtonAddJob, QtCore.SIGNAL("clicked()"), MainWindow.clickedAddJob)
        QtCore.QObject.connect(self.lineEditHaltSPP, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltSPP)
        QtCore.QObject.connect(self.lineEditHaltTime, QtCore.SIGNAL("editingFinished()"), MainWindow.editedHaltTime)
        QtCore.QObject.connect(self.lineEditFilmUpdatePeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedFilmUpdatePeriod)
        QtCore.QObject.connect(self.lineEditStatsPeriod, QtCore.SIGNAL("editingFinished()"), MainWindow.editedStatsPeriod)
        QtCore.QObject.connect(self.pushButtonForceFilmMerge, QtCore.SIGNAL("clicked()"), MainWindow.clickedForceFilmMerge)
        QtCore.QObject.connect(self.pushButtonForceFilmDownload, QtCore.SIGNAL("clicked()"), MainWindow.clickedForceFilmDownload)
        QtCore.QObject.connect(self.pushButtonFinishJob, QtCore.SIGNAL("clicked()"), MainWindow.clickedFinishJob)
        QtCore.QObject.connect(self.pushButtonRemovePendingJobs, QtCore.SIGNAL("clicked()"), MainWindow.clickedRemovePendingJobs)
        QtCore.QObject.connect(self.pushButtonAddNode, QtCore.SIGNAL("clicked()"), MainWindow.clickedAddNode)
        QtCore.QObject.connect(self.pushButtonRefreshNodesList, QtCore.SIGNAL("clicked()"), MainWindow.clickedRefreshNodesList)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditHaltSPP, self.lineEditHaltTime)
        MainWindow.setTabOrder(self.lineEditHaltTime, self.lineEditFilmUpdatePeriod)
        MainWindow.setTabOrder(self.lineEditFilmUpdatePeriod, self.lineEditStatsPeriod)
        MainWindow.setTabOrder(self.lineEditStatsPeriod, self.pushButtonForceFilmDownload)
        MainWindow.setTabOrder(self.pushButtonForceFilmDownload, self.pushButtonForceFilmMerge)
        MainWindow.setTabOrder(self.pushButtonForceFilmMerge, self.pushButtonFinishJob)
        MainWindow.setTabOrder(self.pushButtonFinishJob, self.pushButtonAddJob)
        MainWindow.setTabOrder(self.pushButtonAddJob, self.pushButtonRemovePendingJobs)
        MainWindow.setTabOrder(self.pushButtonRemovePendingJobs, self.pushButtonAddNode)
        MainWindow.setTabOrder(self.pushButtonAddNode, self.tabWidgetMain)
        MainWindow.setTabOrder(self.tabWidgetMain, self.scrollAreaQueuedJobs)
        MainWindow.setTabOrder(self.scrollAreaQueuedJobs, self.scrollArea_2)
        MainWindow.setTabOrder(self.scrollArea_2, self.scrollAreaNodes)
        MainWindow.setTabOrder(self.scrollAreaNodes, self.textEditLog)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "PyLuxCore Tool NetConsole", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Information", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Render configuration file name:", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Film file name:", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Image file name:", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Work directory:", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Start time:", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("MainWindow", "Rendering time:", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate("MainWindow", "Samples/pixel:", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("MainWindow", "Samples/sec:", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Configuration", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Halt at samples/pixel (0 disabled):", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Halt at time (in secs, 0 disabled):", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "Film update period (in secs):", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Statistics print period (in secs):", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("MainWindow", "Commands", None, -1))
        self.pushButtonForceFilmMerge.setText(QtWidgets.QApplication.translate("MainWindow", "Force film merge", None, -1))
        self.pushButtonForceFilmDownload.setText(QtWidgets.QApplication.translate("MainWindow", "Force film download", None, -1))
        self.pushButtonFinishJob.setText(QtWidgets.QApplication.translate("MainWindow", "Finish job", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("MainWindow", "Rendering", None, -1))
        self.labelRenderingImage.setText(QtWidgets.QApplication.translate("MainWindow", "Waiting for film download and merge", None, -1))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.currentJob), QtWidgets.QApplication.translate("MainWindow", "Current job", None, -1))
        self.pushButtonAddJob.setText(QtWidgets.QApplication.translate("MainWindow", "Add job", None, -1))
        self.pushButtonRemovePendingJobs.setText(QtWidgets.QApplication.translate("MainWindow", "Remove pending jobs", None, -1))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.queuedJobs), QtWidgets.QApplication.translate("MainWindow", "Queued jobs", None, -1))
        self.pushButtonAddNode.setText(QtWidgets.QApplication.translate("MainWindow", "Add node", None, -1))
        self.pushButtonRefreshNodesList.setText(QtWidgets.QApplication.translate("MainWindow", "Refresh nodes list", None, -1))
        self.tabWidgetMain.setTabText(self.tabWidgetMain.indexOf(self.nodes), QtWidgets.QApplication.translate("MainWindow", "Nodes", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.actionQuit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))

