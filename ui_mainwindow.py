from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QCheckBox, QFrame, QGraphicsView,
    QLCDNumber, QLabel, QMainWindow, QPushButton,QTableWidgetItem, QDialog,
    QSizePolicy, QVBoxLayout, QWidget)
from ui_historial import Ui_Dialog
import pandas as pd
    
        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 830)
        MainWindow.setMinimumSize(QSize(1100, 830))
        MainWindow.setMaximumSize(QSize(1100, 830))
        QFontDatabase.addApplicationFont("NissanOpti.otf")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1100, 830))
        self.centralwidget.setMaximumSize(QSize(1100, 830))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(1100, 830))
        self.frame.setMaximumSize(QSize(1100, 830))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(40, 10, 192, 192))
        self.graphicsView.setStyleSheet(u"background-image: url(imagenes/192.png);\n"
"border-radius: 10px;")
        self.graphicsView_4 = QGraphicsView(self.frame)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setEnabled(True)
        self.graphicsView_4.setGeometry(QRect(869, 10, 192, 192))
        self.graphicsView_4.setStyleSheet(u"background-image: url(imagenes/mantto.png);\n"
"border-radius: 10px;")
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(760, 610, 121, 25))
        font = QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setTabletTracking(False)
        self.checkBox.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"color: rgb(255, 255, 255);\n"
"border: 4px solid rgb(75, 75, 75);\n"
"border-radius: 10px;") 
        self.checkBox.setChecked(True)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 231, 301, 28))
        font2 = QFont()
        font2.setPointSize(14)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(620, 660, 441, 31))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(775, 720, 93, 28))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButton.setFont(font3)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #383838;\n"
"border-radius: 5px;\n"
"color: rgb(255,255, 255);\n"
"background-color: rgb(255, 55, 58);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #383838;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(180, 10, 10);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 3.5px solid #383838;\n"
"border-radius: 5px;\n"
"color: rgb(150, 150, 150);\n"
"background-color: rgb(180, 10, 10);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 630, 501, 22))
        font4 = QFont()
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(669, 231, 301, 28))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(299, 60, 492, 111))
        font5 = QFont("NissanOpti")
        font5.setPointSize(15)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 0, 0);\n"
"gridline-color: rgb(255, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(775, 760, 93, 28))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: 2px solid #ff0000;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(75, 75, 75);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #ff0000;\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(25, 25, 25);\n"
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: 3.5px solid #ff0000;\n"
"border-radius: 5px;\n"
"color: rgb(100, 100, 100);\n"
"background-color: rgb(25, 25, 25);\n"
"font: 75 9.2pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(55, 575, 471, 22))
        self.label_3.setStyleSheet(u"border: 2px solid #ff0000;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(299, 30, 491, 22))
        self.label_5.setStyleSheet(u"border: 2px solid #ff0000;\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(570, 210, 10, 601))
        self.line.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(25, 25, 25);\n"
"border-radius: 5px;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 270, 300, 300))
        self.label_9.setStyleSheet(u"border: 4px solid #ff0000;\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 10px;\n"
"background-image: url(imagenes/Nissan300.png);")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(670, 270, 300, 300))
        self.label_10.setStyleSheet(u"border: 4px solid #ff0000;\n"
"background-color: rgb(75, 75, 75);\n"
"border-radius: 10px;\n"
"background-image: url(imagenes/Nissan300.png);")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(160, 660, 260, 130))
        #self.label_11.setStyleSheet(u"background-image: url(imagenes/nulo.png);")
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.graphicsView.raise_()
        self.graphicsView_4.raise_()
        self.checkBox.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.label_4.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.line.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nissan PdM Department (AQUASE)", None))
#if QT_CONFIG(whatsthis)
        self.graphicsView_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\"imagenes/mantto.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Discriminar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ultima imagen evaluada", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Kill Process", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resultado de la evaluaci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Camara en tiempo real", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PdM Sistema de aseguramiento de calidad del proceso de limado de electrodos", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Historial", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"A\u00fan no se ha evaluado ninguna imagen", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cargando Datos...", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
    # retranslateUi

