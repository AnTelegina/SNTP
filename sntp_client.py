
import socket
import time

from ntplib import NTPStats

stats = NTPStats()

sock = socket.socket()
sock.connect(('localhost', 123))
sock.send(str('aaa').encode())

data = sock.recv(1024)
sock.close()

print(f'Полученные данные: {data}')
stats.from_data(data)
print(f'Время полученное пользователем: {time.ctime(stats.tx_time)}')