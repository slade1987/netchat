import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

def chat_server(ip:str, port:int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((ip,int(port)))
    sock.listen()
    print('Server is running')

    while True:
        conn, addr = sock.accept()
        print('Conn', conn, '\n', 'Add', addr  )
        data = conn.recv(1024)
        print(str(data))
        conn.send(data.upper())
        conn.close()

if __name__ == '__main__':
    chat_server(args.ip_addr, args.port)