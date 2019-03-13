def send(client):
	while True:
		msg = input("server--> {msg}")
		client.send(msg.encode())
		if msg.lower().strip() == 'bye':
			client.close()
			print("Connection closed by server")
			break
def recv(client):
	while True:
		msg = client.recv(1024).decode()
		s = "client--> {msg}"
		print(msg.rjust(50))
		if msg.lower().strip() == 'bye':
			client.close()
			print("Connection closed by client")
			break


import socket
import threading
server  = socket.socket()
host = 'localhost'
port = 12345
server.bind((host,port))
server.listen()
print(f"Sever is waiting for clients on {host}:{port}")
client_socket, client_address = server.accept()
print(f"Received a connection from {client_address[0]}:client_address[1]")

msg_send=threading.Thread(target=send, args=(client_socket,))
msg_recv=threading.Thread(target=recv, args=(client_socket,))

msg_send.start()
msg_recv.start()

msg_send.join()
msg_recv.join()

		