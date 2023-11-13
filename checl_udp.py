import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(("127.0.0.1",50007))
if result == 0:
    print("Port 50007 is open")
    sock.close()
else:
    print("Port 50007 is not open")

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result2 = sock.connect_ex(("127.0.0.1",50008))

if result == 0:
    print("Port 50008 is open")
    sock2.close()
else:
    print("Port 50008 is not open")