import socket
import argparse
from datetime import datetime
import json

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

RESPONSE = {
"response": 'None',
"From": 'Server',
"time": str(datetime.now())
}



def chat_server(ip:str, port:int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((ip,int(port)))
    sock.listen()
    print('Server is running')

    while True:
        conn, addr = sock.accept()
        print('Conn', conn, '\n', 'Add', addr  )
        conn.send(json.dumps(RESPONSE).encode('utf-8'))
        data = json.loads(conn.recv(1024))
        conn.close()
        print(data)

if __name__ == '__main__':
    chat_server(args.ip_addr, args.port)