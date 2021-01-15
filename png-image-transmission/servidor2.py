from decoding import *
import socket
import json
import struct
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE, SIG_DFL)

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

# Recibir un ACK
bstream = socket_client.recv(3)
print("Received!")

if bstream == b"new":
    matriz = numpy.empty((600,800), dtype = numpy.int16)
    k = 0
    #print(matriz)
    strRow = socket_client.recv(800)
    while strRow[:600] == b"row":
        #print("Hola si entro al WHILE PUTO")
        matriz[k] = numpy.array(struct.unpack(800*'h', strRow[600:], dtype = numpy.int16))
        strRow = socket_client.recv(800)
        #1502808
        k+=1
        socket_client(b"ack")
        print("Matriz recibida")
        #print(matriz)


else:
    print("Comando no reconocido")
    

    
rndrImage = decode(matriz)
print("Showing received image...")
cv2.imshow('Imagen', rndrImage) # dtype=uint8
      
cv2.waitKey(0)
cv2.destroyAllWindows()



print("Success!")
socket_client.close()
socket_server.close()
