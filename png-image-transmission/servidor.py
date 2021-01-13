
import socket

# Creando el socket: protocolos
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definiendo puertos
socket_server.bind( ("0.0.0.0",9999) )

# Cuantos host se van a comunicar con el servidor
# Esta funcion pone al servidor en modo escuchar: espera peticion
socket_server.listen(1)

# Aceptando la peticion
# Se crea el cliente
socket_client, (remote_client_ip, remote_client_tcp) = socket_server.accept()
print("ip client", remote_client_ip)
print("tcp client", remote_client_tcp)

# Recibir un mensaje
while True:
	mensaje = socket_client.recv(1024)
	socket_client.send(mensaje)		# envia echo
	if mensaje == b"quit":
		break
	print("> ", mensaje)

print("bye")
socket_client.close()
socket_server.close()





