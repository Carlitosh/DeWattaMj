#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, uic
import csv
import matplotlib.pyplot as plt
import numpy as np
from metodos import area_bajo_curva,graficar

# Cargar nuestro archivo .ui
form_class = uic.loadUiType("interfaz.ui")[0]

class convertidor_watt_mj(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
		self.button_abrir.clicked.connect(self.abrir)
		self.button_guardar.clicked.connect(self.guardar)
		self.button_procesar.clicked.connect(self.procesar)
		self.button_graficar.clicked.connect(self.graficar)
		

		
	def abrir(self):
		#self.comboBox1.clear()
		#self.comboBox2.clear()
		
		path_entrada = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Capa csv', 
		'','(*.csv)')
		self.lineEdit_entrada.setText(str(path_entrada))

	
	def guardar(self):
		path_salida = QtGui.QFileDialog.getSaveFileName(self, 'Guardar csv ',
		 'Archivos/', selectedFilter='*.csv')
		self.lineEdit_salida.setText(str(path_salida))
		

	def procesar(self):
		print ""
		archivo_entrada = str(self.lineEdit_entrada.text())
		archivo_salida = str(self.lineEdit_salida.text()) 
		fila_fecha = int(self.spinBox_fecha.value())
		fila_radiacion = int(self.spinBox_radiacion.value())

		area_bajo_curva(archivo_entrada,archivo_salida,fila_fecha,fila_radiacion)
		
	def graficar(self):
		archivo_entrada = str(self.lineEdit_entrada.text())
		archivo_salida = str(self.lineEdit_salida.text()) 
		fila_fecha = int(self.spinBox_fecha.value())
		fila_radiacion = int(self.spinBox_radiacion.value())
		graficar(archivo_entrada,archivo_salida,fila_fecha,fila_radiacion)

app = QtGui.QApplication(sys.argv)
ventana = convertidor_watt_mj(None)
ventana.show()
app.exec_()			
	


