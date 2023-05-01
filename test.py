import socket
import unittest
from lesson3_client import chat_client
from lesson3_server import chat_server

class TestChat(unittest.TestCase):
    def setUp(self):
        self.serv = chat_server('localhost', 7777)
        self.client = chat_client('localhost', 7777)

    def connClose(self):
        self.serv.close()
        self.client.close()

    def test_pasrse(self):
        self.client.parse_data(self.sender)

    def test_serv_sock_is_inst(self):
        self.assertIsInstance(self.serv,socket.socket)

    def testServer(self):
        self.assertEqual(self.serv.getsockname(), ('127.0.0.1', 7777))

    def testClient(self):
        self.assertEqual(self.client.getsockname(),('127.0.0.1',7777))




if __name__ == '__main__':
    unittest.main()