 #!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import csv
import matplotlib.pyplot as plt
import datetime

"""
archivo_entrada = 'datos_meteorologicos.csv'
archivo_salida = 'salida.csv'
fila_fecha = 5
fila_radiacion = 14
"""
def area_bajo_curva(archivo_entrada,archivo_salida,fila_fecha,fila_radiacion):
	col_fecha=[]
	col_rad=[]
	cont_rad = 0    # (a)
	with open(archivo_entrada, 'rb') as archivo_csv:
	    archivo = csv.reader(archivo_csv, delimiter=';')
	    for fila in archivo:
	        col_fecha.append(fila[fila_fecha])
	        col_rad.append(fila[fila_radiacion])
	        

	col_rad1 =[float(i) for i in col_rad[1:]]
	col_fecha1 =[float(i) for i in col_fecha[1:]]
	#========================
	col_rad1.append(1)
	col_fecha1.append(1)
	#=========================
	data = zip(col_fecha1,col_rad1)
	radiacion=[]
	day = []
	cont_rad = 0

	minutos_radiacion = []
	for i in range(0,len(data)):
		
		try:

			if data[i][0] == data[i+1][0]:
				cont_rad = data[i][1] + cont_rad
			else:
				
				cont_rad = data[i][1] + cont_rad
				radiacion.append(((cont_rad/144)/10))
				day.append(data[i][0])
				cont_rad = 0
				contador = 0 
		except:
			pass

		

	fecha_inicio = datetime.datetime(1900,1,1)
	array_fecha = []
	for i in day:
		fecha = fecha_inicio + datetime.timedelta(days=int(i)-3) 
		array_fecha.append("%s/%s/%s" % (fecha.day, fecha.month, fecha.year))



	#array_fecha = np.char.asarray(array_fecha)
	array_dias = np.asarray(day)
	array_radiacion = np.around(np.asarray(radiacion, dtype=float),decimals=1)

	plt.plot(array_dias,array_radiacion,'-k')
	#plt.xticks(len(array_dias),array_fecha)
	plt.ylim(0,40)
	plt.show()	

	header = ['fecha','radiacion (Mj/m2)']
	with open(archivo_salida, "wb") as fichero:
	    writer = csv.writer(fichero)
	    writer.writerow([g for g in header])
	    writer.writerows(zip(array_fecha,array_radiacion))

def graficar(archivo_entrada,archivo_salida,fila_fecha,fila_radiacion):
	col_fecha=[]
	col_rad=[]
	cont_rad = 0    # (a)
	with open(archivo_entrada, 'rb') as archivo_csv:
	    archivo = csv.reader(archivo_csv, delimiter=';')
	    for fila in archivo:
	        col_fecha.append(fila[fila_fecha])
	        col_rad.append(fila[fila_radiacion])
	        

	col_rad1 =[float(i) for i in col_rad[1:]]
	col_fecha1 =[float(i) for i in col_fecha[1:]]
	#========================
	col_rad1.append(1)
	col_fecha1.append(1)
	#=========================
	data = zip(col_fecha1,col_rad1)
	radiacion=[]
	day = []
	cont_rad = 0

	minutos_radiacion = []
	for i in range(0,len(data)):
		
		try:

			if data[i][0] == data[i+1][0]:
				cont_rad = data[i][1] + cont_rad
			else:
				
				cont_rad = data[i][1] + cont_rad
				radiacion.append(((cont_rad/144)/10))
				day.append(data[i][0])
				cont_rad = 0
				contador = 0 
		except:
			pass

		

	fecha_inicio = datetime.datetime(1900,1,1)
	array_fecha = []
	for i in day:
		fecha = fecha_inicio + datetime.timedelta(days=int(i)-3) 
		array_fecha.append("%s/%s/%s" % (fecha.day, fecha.month, fecha.year))



	#array_fecha = np.char.asarray(array_fecha)
	array_dias = np.asarray(day)
	array_radiacion = np.around(np.asarray(radiacion, dtype=float),decimals=1)

	plt.plot(array_dias,array_radiacion,'-k')
	#plt.xticks(len(array_dias),array_fecha)
	plt.ylim(0,40)
	plt.show()	


#area_bajo_curva(archivo_entrada,archivo_salida,fila_fecha,fila_radiacion)