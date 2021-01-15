import socket, cv2
import json, sys, struct
from encoding import *
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

DNS = "4.tcp.ngrok.io"
PORT = 17955

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( (DNS, PORT) )	# FOLLOW README INSTRUCTIONS AND REPLACE WITH REAL PARAMETERS
#socket_client.connect( ("0.tcp.ngrok.io", 13547))

# Mensaje imagen
print("Preparing message...") # Imprime mensaje
BWimage = cv2.imread('../photo.jpg',cv2.IMREAD_GRAYSCALE)
# Muestra imagen
#cv2.imshow('imagenBW', BWimage) # dtype=uint8
# Obteniendo imagen sin compresión
print("Coding...")
jpegImage=encode2(BWimage)

[rows, cols] = jpegImage.shape
print(sys.getsizeof(jpegImage))

#SENDING MATRIZ

for k in range(rows):
    #print(jpegImage.shape)
    socket_client.send(b"new")
    #CODING
    strRow = b"row" + struct.pack(cols*'h', *jpegImage[k][:])
    #SENDING
    print("Sending...")
    socket_client.send(strRow)
    ack=socket_client.recv(3)
    

socket_client.send(b"eol")

print("Image sent!")
socket_client.close()
