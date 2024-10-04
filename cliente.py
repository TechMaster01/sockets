import socket

# Pedir la IP del servidor al usuario
Server_Ip = input("Introduce la dirección IP del servidor: ")

# Crear el socket del cliente
Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor en el puerto 3490
Mi_Socket.connect((Server_Ip, 3490))

# Enviar mensaje al servidor
# Mensaje_Cliente = "Hola desde el cliente".encode('utf-8')
# Mi_Socket.send(Mensaje_Cliente)

# Recibir el mensaje del servidor
Mensaje_Servidor = Mi_Socket.recv(1024).decode('utf-8')

# Mostrar el mensaje recibido
print(f"Mensaje del servidor: {Mensaje_Servidor}")

# Cerrar el socket
Mi_Socket.close()
