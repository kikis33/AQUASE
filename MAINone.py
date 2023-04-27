import sys
from PySide2.QtCore import  QTimer
from PyQt5 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QTableWidgetItem
from PySide2.QtGui import QIcon, QImage, QPixmap, QImage
from PySide2.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
from ui_historial import Ui_Dialog
import time
import imutils
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'es-MX')
import ctypes
import cv2
import pandas as pd
from tensorflow import keras
import tensorflow as tf
import numpy as np
import shutil

myappid = 'Nissan.PDM-QA.AQUASE.V1' 
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

conteo = 0
estado = True

class Historial(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("imagenes/logo.png"))
    def showEvent(self, event):
        df=0
        df = pd.read_excel("dataresults.xlsx")
        columnas = list(df.columns)
        df_fila = df.to_numpy().tolist()
        x = len(columnas)
        y = len(df_fila)
        self.ui.tableWidget.setRowCount(y)
        self.ui.tableWidget.setColumnCount(x)
        for j in range(x):
            encabezado = QTableWidgetItem(columnas[j])
            self.ui.tableWidget.setHorizontalHeaderItem(j,encabezado)
            for i in range(y):
                dato = str(df_fila[i][j])
                if dato == 'nan':
                    dato = ''
                self.ui.tableWidget.setItem(i,j,QTableWidgetItem(dato))
        del df

class MainWindow(QMainWindow):

    def __init__(self):
        global estado
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        self.setWindowIcon(QIcon("imagenes/logo.png"))

        self.webcam = cv2.VideoCapture(0)

        self.ventana = Historial()

        pixmap = QPixmap('imagenes/nulo.png') 
        self.ui.label_11.setPixmap(pixmap)

        #red_electrodes = keras.models.load_model("C:/Users/kikis/OneDrive/Escritorio/converted_keras/keras_model.h5")     #H5 TM
        self.red_electrodes = keras.models.load_model("C:/Users/kikis/OneDrive/Escritorio/model.savedmodel")                   #SVM TM
        #red_electrodes = keras.models.load_model("C:/Users/kikis/OneDrive/Escritorio/kerasinc/modelo_electrodos.h5")      #H5 INCV3
        #red_electrodes = keras.models.load_model("C:/Users/kikis/OneDrive/Escritorio/modelo_electrodos")                  #SVM INCV3M
        print("Modelo cargado")
        self.red_electrodes.trainable = False
        self.red_electrodes.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy','FalseNegatives','FalsePositives','TrueNegatives','TruePositives','MeanAbsolutePercentageError'])
        self.red_electrodes.summary()

        self.ui.pushButton_2.clicked.connect(self.history)
        self.ui.pushButton.clicked.connect(self.proceso)
        #self.ui.pushButton.clicked.connect(MainWindow.close)
        self.ui.checkBox.toggled.connect(self.onClicked)
        
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start(1)
        timer2 = QTimer(self)
        timer2.timeout.connect(self.displayVideo)
        timer2.start(1000/30)

    def onClicked(self):
        global estado
        self.ui.checkBox = self.sender()
        estado = self.ui.checkBox.isChecked()

    def history(self):
        self.ventana.exec_()

    def displayTime(self):
        date=datetime.strftime(datetime.now(),'%A, %d de %B del %Y -- %H:%M:%S')
        self.ui.label_5.setText(date)

    def displayVideo(self):
        ok, img = self.webcam.read()
        if not ok:
            return
        img = cv2.resize(img, (300,300),interpolation = cv2.INTER_AREA)
        image = QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QImage.Format_RGB888)
        pixmap = QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
        self.ui.label_10.setPixmap(pixmap)

    def proceso(self):
        global conteo
        global estado
        img2, img3 = self.foto()
        resultado = self.clasificar(img2)
        print(resultado)
        date=datetime.strftime(datetime.now(),'Imagen capturada el %d de %B del %Y a las %H:%M:%S hrs')
        self.ui.label_3.setText(date)
        self.registrar(resultado, conteo, img3)  

        if resultado == "OK":
            accion = "NoLimar" 
            conteo = 0
            self.ui.label_7.setText("No se limó el electrodo por condición OK")
        elif conteo >= 3:
            accion = "NoLimar" 
            conteo = 0
            self.ui.label_7.setText("No se limó porque el límite de limado se alcanzó")
        elif not(estado):
            accion = "NoLimar" 
            conteo = 0
            self.ui.label_7.setText("No se limó el electrodo porque asi se ha indicado")
        else:
            accion = "Limar"  
            conteo = conteo + 1
            self.ui.label_7.setText("Se limó el electrodo por condición NG")              

        if resultado == "OK":
            pixmap = QPixmap('imagenes/ok.png')
        else:
            pixmap = QPixmap('imagenes/ng.png')

        self.setPin(accion)
        self.ui.label_11.setPixmap(pixmap)  

    def registrar(self, resultado, veces, img2):      
        fecha = datetime.strftime(datetime.now(),'%d-%B-%y')
        hora = datetime.strftime(datetime.now(),'%H:%M:%S')
        f1 = datetime.strftime(datetime.now(),'%Y_%M_%d--%H_%M_%S')
        ubicacion = "D:/Nissan/AQUASE/clasificacion/" + resultado + "/" + f1 + ".jpg"
        print("Guardado en " + ubicacion)
        cv2.imwrite(ubicacion, img2)
        df5 = 0
        df6 = 0
        if veces > 2 : veces2 = "No Limado"
        else : veces2 = str(veces+1)
        df6 = pd.DataFrame({'col1': fecha, 'col2': hora, 'col3': resultado, 'col4': [veces2], 'col5': ubicacion}, columns=None) 
        df5 = pd.read_excel("dataresults.xlsx", header=None)
        df_fila = df5.to_numpy().tolist()
        y = len(df_fila)
        print(y)
        if y==0: y=1
        print(y)
        with pd.ExcelWriter("dataresults.xlsx", mode="a", if_sheet_exists='overlay') as writer:
            df6.to_excel(writer, header=False, index=False, na_rep='', startrow=y) 
        del df5
        del df6 

    def setPin(self, accion):
        if accion == "NoLimar":
            print("No se limará el electrodo")
        else:
            print("Se limará el electrodo")


    def foto(self):
        ok, img = self.webcam.read()
        if not ok:
            return
        img3 = img
        img2= cv2.resize(img, (224,224),interpolation = cv2.INTER_AREA)
        img = cv2.resize(img, (300,300),interpolation = cv2.INTER_AREA)
        image = QImage(img, img.shape[1], img.shape[0], img.shape[1] * img.shape[2], QImage.Format_RGB888)
        pixmap = QPixmap()
        pixmap.convertFromImage(image.rgbSwapped())
        self.ui.label_9.setPixmap(pixmap)
        return img2, img3

    def clasificar(self, img):
        prediccion = self.red_electrodes.predict(img.reshape(-1, 224, 224, 3),verbose=1, steps=None, workers=2, use_multiprocessing=True)
        print(prediccion)
        if prediccion[0][0] > 0.4 and prediccion[0][1] < 0.55 :
            return "OK"
        else: 
            return "NG"

    

    def closeEvent(self, event):
        event.accept()
        pregunta = QMessageBox.question(self, "Saliendo", "¿Estas seguro/a de que quieres cerrar el programa?", QMessageBox.Yes | QMessageBox.No)
        if pregunta == QMessageBox.Yes:
            pregunta2 = QMessageBox.question(self, "Saliendo...", "¿Estas TOTALMENTE seguro/a de que quieres cerrar el programa? \n (El programa se cerrara definitivamente y tendrá que volver a iniciarse manualmente)", QMessageBox.Yes | QMessageBox.No)
            if pregunta2 == QMessageBox.Yes:
                pregunta3 = QMessageBox.question(self, "Ultima oportunidad", "Ultima confirmacion, cerraras el programa y tendras que iniciarlo manualmente", QMessageBox.Ok | QMessageBox.Cancel)
        if pregunta == QMessageBox.Yes and pregunta2 == QMessageBox.Yes and pregunta3 == QMessageBox.Ok: event.accept()
        if pregunta == QMessageBox.Yes and pregunta2 == QMessageBox.Yes and pregunta3 == QMessageBox.Ok: self.webcam.release()
        else: event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())	