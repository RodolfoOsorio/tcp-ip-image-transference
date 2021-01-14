from decoding import *
import socket
import json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

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
bstream = socket_client.recv(1502808)
print("Received!")

try:
    # Decodificacion del mensaje
    print("Decoding...")
    mensaje = bstream.decode()
    #print(mensaje)
    lista = json.loads(mensaje) # convierte a lista
    matrix = numpy.array(lista) # convierte a matriz de numpy
    rndrImage = decode(matrix)

    '''
    signalPower=(BWimage.astype(numpy.int16)**2).mean(axis=None)
    noisePower=( ( BWimage.astype(numpy.int16)-rndrImage.astype(numpy.int16) )**2).mean(axis=None)
    SNR=10*math.log10(signalPower/noisePower)
    print ("SNR: ",SNR)
    '''
    # Visualiza mensaje recibido
    print("Showing received image...")
    cv2.imshow('render', rndrImage) # dtype=uint8
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Success!")
finally:
    socket_client.close()
    socket_server.close()
