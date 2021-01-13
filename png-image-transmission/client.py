
import socket

# Protocolos
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Que puertos
socket_client.connect( (<"SERVER DNS"> , <CLIENT PORT>) )	# FOLLOW README INSTRUCTIONS AND REPLACE WITH REAL PARAMETERS
#socket_client.connect( ("0.tcp.ngrok.io", 13547))
#socket_client.connect( ("localhost", 9999) )

# Mensaje

while True:
	mensaje = input("> ").encode() 	# codifica a 8 bits
	socket_client.send(mensaje)		# envia mensaje
	data = socket_client.recv(1024)	# Recibe el eco
	print("echo:>", data)			# Imprime el eco
	if mensaje == b"quit":
		break

# Cierre
print("Bye")
socket_client.close()
