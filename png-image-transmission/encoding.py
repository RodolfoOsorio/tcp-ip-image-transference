import numpy
import cv2
from scipy.fftpack import dct
from scipy.fftpack import idct
from time import time
import math


#Codificacion
def encode(BWimage):
	rows,cols=BWimage.shape # Gets size
	jpgImage=numpy.zeros([rows,cols],dtype=numpy.int8) #Debieran ser 16 bits
	factor=(0.22/64)
	for r in range(0,rows,8):
		for c in range(0,cols,8):
			block=BWimage [r:r+8,c:c+8].astype( numpy.int16 )-128	# Recupera bloque de 8x8, convierte a int16 y elimina componente DC
			dctblock= (factor * dct(dct(block,axis=0),axis=1)).astype(numpy.int8) # Cálculo de serie coseno discreto
			jpgImage[r:r+8,c:c+8]=dctblock # Forma matriz de espectros
	return jpgImage







