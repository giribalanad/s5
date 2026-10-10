
# ========== TCP SERVER (tcp_server.py) ==========
import socket

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)
c, _ = s.accept()
print("Client:", c.recv(1024).decode())
c.send(b"Message received")
c.close()
s.close()

# OUTPUT:
# Client: Hello


# ========== TCP CLIENT (tcp_client.py) ==========
import socket

s = socket.socket()
s.connect(("localhost", 5000))
s.send(input("Message: ").encode())
print("Server:", s.recv(1024).decode())
s.close()

# INPUT:
# Message: Hello
# OUTPUT:
# Server: Message received


# ========== UDP RECEIVER (udp_receiver.py) ==========
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 6000))
data, addr = s.recvfrom(1024)
print("Received:", data.decode())
s.close()

# OUTPUT:
# Received: Hello


# ========== UDP SENDER (udp_sender.py) ==========
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(input("Message: ").encode(), ("localhost", 6000))
s.close()

# INPUT:
# Message: Hello
# OUTPUT:
# (No output)
