import socket

# Crear el socket del servidor
Mi_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar el puerto 3490 al socket
Mi_Socket.bind(('localhost', 3490))

# Escuchar conexiones entrantes (máximo 5 en cola)
Mi_Socket.listen(5)
print("Servidor escuchando en el puerto 3490...")

while True:
    # Aceptar una nueva conexión
    Cliente_Socket, Cliente_Address = Mi_Socket.accept()
    print(f"Conexión desde {Cliente_Address}")

    # Enviar un mensaje al cliente
    Mensaje_Servidor = "Hola desde el socket servidor".encode('utf-8')
    Cliente_Socket.send(Mensaje_Servidor)

    # Recibir mensaje del cliente
    # Mensaje_Cliente = Cliente_Socket.recv(1024).decode('utf-8')
    # print(f"Mensaje del cliente: {Mensaje_Cliente}")

    # Cerrar la conexión
    Cliente_Socket.close()