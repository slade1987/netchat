import socket
import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

PRESENCE = {
"From": 'client',
"time": str(datetime.now())
}

def parse_data(data:dict):
    if data['response'][0] == '200':
        return print("Все прошло хорошо")
    else:
        return print('Что то пошло не так')


def chat_client(ip:str, port: int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, int(port)))
    data = json.loads(sock.recv(1024))
    sock.send(json.dumps(PRESENCE).encode('utf-8'))
    parse_data(data)
    sock.close()
    print(data)

if __name__ == "__main__":
    chat_client(args.ip_addr, args.port)
