from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,QTableView,
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,QAbstractScrollArea,QAbstractItemView,
    QVBoxLayout, QWidget)
import pandas as pd



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 450)
        Dialog.setMinimumSize(QSize(800, 450))
        Dialog.setMaximumSize(QSize(800, 450))
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 800, 450))
        self.frame.setMinimumSize(QSize(800, 450))
        self.frame.setMaximumSize(QSize(800, 450))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(205, 21, 49);\n"
"border: 3px solid #4b4b4b;\n"
"border-radius: 12px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 15, 751, 21))
        QFontDatabase.addApplicationFont("NissanOpti.otf")
        font = QFont("NissanOpti")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(205, 21, 49);\n"
"border: 0px solid #4b4b4b;\n"
"border-radius: 12px;\n"
"color: #fffff8;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_2)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(776, 370))
        self.tableWidget.setMaximumSize(QSize(776, 370))
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet(u"QWidget{	\n"
"	background-color:  rgb(50, 50, 50); \n"
"	alternate-background-color:#4b4b4b;\n"
"	color: #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	padding: 4px;\n"
"	background-color:  #4b4b4b; \n"
"	font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	font-size: 12pt;\n"
"	border: 3px solid rgb(205, 21, 49);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal{\n"
"    border-bottom: 1px solid #000000;\n"
"	border-top: none;\n"
"}\n"
"\n"
"")
        self.tableWidget.setFrameShape(QFrame.VLine)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(130)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setMinimumSectionSize(35)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 15)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Historial", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Historial de clasificacion de resultados", None))
    # retranslateUi

