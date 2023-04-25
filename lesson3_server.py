import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',50000))
sock.listen()
print('Server is running')

while True:
    conn, add = sock.accept()
    print('Conn', conn, '\n', 'Add', add)
    data = conn.recv(1024)
    print(str(data))
    conn.send(data.upper())
    conn.close()