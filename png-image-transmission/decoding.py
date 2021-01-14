import numpy
import cv2
from scipy.fftpack import dct
from scipy.fftpack import idct
from time import time
import math


#Decodificacion
def decode(jpegimage):
	rows,cols=jpegimage.shape
	rndrImage=numpy.zeros([rows,cols],dtype=numpy.uint8)
	for r in range(0,rows,8):
		for c in range(0,cols,8):
			dctblock=jpegimage[r:r+8,c:c+8]
			block=(idct(idct(dctblock,axis=0),axis=1)+128).astype(numpy.uint8)
			rndrImage[r:r+8,c:c+8]=block
	return rndrImage