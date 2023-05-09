import inspect
import socket
import argparse
import json
from datetime import datetime
import log.client_log_config as logg
from functools import wraps

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

PRESENCE = {
"From": 'client',
"time": str(datetime.now())
}

def log(func):
    @wraps(func)
    def call(*args, **kwargs):
        logg.logger.debug(f"Funct {func.__name__} call {inspect.stack()[1][3]}")
        return func(*args, **kwargs)
    return call

@log
def parse_data(data:dict):
    if data['response'][0] == '200':
        return print("Все прошло хорошо")
    else:
        return print('Что то пошло не так')

@log
def chat_client(ip:str, port: int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
       sock.connect((ip,int(port)))
       logg.logger.info("Соеденение прошло успешно")
       data = json.loads(sock.recv(1024))
       sock.send(json.dumps(PRESENCE).encode('utf-8'))
       parse_data(data)
       sock.close()
       print(data)
       logg.logger.info("Данные получены и отправленые")
    except:
        logg.logger.error("Не удалось установить соединение")


if __name__ == "__main__":
    chat_client(args.ip_addr, args.port)