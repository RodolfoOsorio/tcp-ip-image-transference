
import json
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

def decode(jpegimage):
	rows,cols=jpegimage.shape
	rndrImage=numpy.zeros([rows,cols],dtype=numpy.uint8)
	for r in range(0,rows,8):
		for c in range(0,cols,8):
			dctblock=jpegimage[r:r+8,c:c+8]
			block=(idct(idct(dctblock,axis=0),axis=1)+128).astype(numpy.uint8)
			rndrImage[r:r+8,c:c+8]=block
	return rndrImage

# Mensaje imagen
print("Preparing message...") 
BWimage=cv2.imread('../image800x600.jpg',cv2.IMREAD_GRAYSCALE)
# Muestra imagen
cv2.imshow('imagenBW', BWimage) # dtype=uint8
#cv2.waitKey(0)

# Obteniendo imagen sin compresión
print("Coding...")
print("Decoding...")
jpegImage=encode(BWimage)

rows, cols = jpegImage.shape
matrix = []
for i in range(rows):
    lista = jpegImage[i].tolist() # Transforma a lista
    listastr = json.dumps(lista) # Transforma a str
    blistastr = listastr.encode() # Codifica a 8 bits

    lista = json.loads(blistastr) # convierte a lista
    vector = numpy.array(lista) # convierte a matriz de numpy
    numpy.concatenate([matrix, vector], axis = 0)

matrix.shape
rndrImage = decode(matrix)


# Visualiza mensaje recibido
print("Showing received image...")
cv2.imshow('render', rndrImage) # dtype=uint8
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Success!")
