import subprocess
import sys

#task 1
word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'

print(type(word1))
print(type(word2))
print(type(word3))

print('Unicode')
uword1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
uword2 = '\u0441\u043e\u043a\u0435\u0442'
uword3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(uword1), uword1)
print(type(uword2), uword2)
print(type(uword3), uword3)


#task 2

word1 = bytes('class','utf-8')
print(word1, type(word1), sys.getsizeof(word1))
word2 = bytes('function','utf-8')
print(word2, type(word2), sys.getsizeof(word2))
word3 = bytes('method', 'utf-8')
print(word3, type(word3), sys.getsizeof(word3))

#task 3

word1 = b'attribute'
#Выдает ошибки
#word2 = b'класс'
#word3 = b'функция'
word4 = b'type'

# task 4
word1 = 'разработка'
word1 = word1.encode()
print(word1, '\n', word1.decode())

word2 = 'администрирование'
word2 = word2.encode()
print(word2, '\n', word2.decode())

word3 = 'protocol'
word3 = word3.encode()
print(word3, '\n', word3.decode())

word4 = 'standard'
word4 = word4.encode()
print(word4, '\n', word4.decode())


ping_results = ''
args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    ping_results += line.decode('cp866')

print(ping_results.encode('utf-8'))

