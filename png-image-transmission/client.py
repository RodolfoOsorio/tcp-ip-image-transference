import socket
import json
from encoding import *
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( ("4.tcp.ngrok.io", 13900) )	# FOLLOW README INSTRUCTIONS AND REPLACE WITH REAL PARAMETERS
#socket_client.connect( ("0.tcp.ngrok.io", 13547))

# Mensaje imagen
print("Preparing message...") # Imprime mensaje
BWimage=cv2.imread('../image800x600.jpg',cv2.IMREAD_GRAYSCALE)
# Muestra imagen
cv2.imshow('imagenBW', BWimage) # dtype=uint8
# Obteniendo imagen sin compresión
print("Coding...")
jpegImage=encode(BWimage)

lista = jpegImage.tolist() # Transforma a lista
listastr = json.dumps(lista) # Transforma a str
blistastr = listastr.encode() # Codifica a 8 bits

try:
    # Envia mensaje
    print("Sending...")
    socket_client.send(blistastr)
finally:
    # Cierre
    print("Image sent!")
    socket_client.close()
