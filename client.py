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
server = socket.socket()
host = 'localhost'
port = 12345
server.connect((host,port))

print(f"Connected to {host}:{port})")
msg_send = threading.Thread(target=send, args=(server,))
msg_recv = threading.Thread(target=recv, args=(server,))

msg_send.start()
msg_recv.start()

msg_send.join()
msg_recv.join()