import socket
import argparse
from datetime import datetime
import json
import log.server_log_config as logg

parser = argparse.ArgumentParser()
parser.add_argument('ip_addr',  nargs='?', default='localhost')
parser.add_argument("port", nargs='?', default='7777')
args = parser.parse_args()

RESPONSE = {
"response": 'None',
"From": 'Server',
"time": str(datetime.now())
}

SERV_RESP = (
    ('200', 'OK'),
    ('400', 'неправильный запрос/JSON-объект')
)


def chat_server(ip:str, port:int):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        sock.bind((ip,int(port)))
        logg.logger.info("Все пошло хорошо. Соединения установленно")
    except Exception:
        logg.logger.warning("Соединения установленно на не стандартном потру 7771. Проверьте порт 7777")
        sock.bind((ip,7771))

    sock.listen()
    print('Server is running')
    RESPONSE['response'] = SERV_RESP[0]
    print('Отладочная информация', RESPONSE)


    while True:
        conn, addr = sock.accept()
        print('Conn', conn, '\n', 'Add', addr  )
        conn.send(json.dumps(RESPONSE).encode('utf-8'))

        try:
            data = json.loads(conn.recv(1024))
            print(data)
            logg.logger.info("Данные получены")
        except ValueError:
            logg.logger.error('С данными что то случилось')
            print('Corrupted data')

        conn.close()

if __name__ == '__main__':
    chat_server(args.ip_addr, args.port)