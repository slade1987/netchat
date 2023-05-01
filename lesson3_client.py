import socket
import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

RESPONSE = {
"response": 'None',
"From": 'client',
"time": str(datetime.now())
}

def resp_ans(ans):
    pass

def chat_client(ip:str, port: int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, int(port)))
    data = json.loads(sock.recv(1024))
    sock.send(json.dumps(RESPONSE).encode('utf-8'))
    sock.close()
    print(data)

if __name__ == "__main__":
    chat_client(args.ip_addr, args.port)
