
import socket
import encoding

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( (<"SERVER DNS"> , <CLIENT PORT>) )	# FOLLOW README INSTRUCTIONS AND REPLACE WITH REAL PARAMETERS
#socket_client.connect( ("0.tcp.ngrok.io", 13547))

# Mensaje imagen
print("Preparing message:\n", matrix) #Imprime mensaje
BWimage=cv2.imread('../image800x600.jpg',cv2.IMREAD_GRAYSCALE)
# Muestra imagen
cv2.imshow('imagenBW', BWimage) # dtype=uint8
# Obteniendo imagen sin compresión
print("Coding...")
jpegImage=encode(BWimage)

# Codifica mensaje
print("Coding...")
lista = jpegImage.tolist() # Transforma a lista
listastr = json.dumps(lista) # Transforma a str
blistastr = listastr.encode() # Codifica a 8 bits

# Envia mensaje
print("Sending...")
socket_client.send(blistastr)

# Cierre
print("Image sent!")
socket_client.close()
