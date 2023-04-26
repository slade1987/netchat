import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

def chat_client(ip:str, port: int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, int(port)))
    sock.send(bytes("hello", encoding = 'UTF-8'))
    data = sock.recv(1024)
    sock.close()
    print(data)

if __name__ == "__main__":
    chat_client(args.ip_addr, args.port)
