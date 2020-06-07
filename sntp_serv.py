
import struct

import ntplib
import socket
import time

TIME1970 = 2208988800

time_difference = 0

with open('config.txt', 'r') as config_file:
    time_difference = int(config_file.readline())

print(f"Время сдвига: {time_difference}")

NTP_SERVER = ntplib.NTPClient()

sock = socket.socket()
sock.bind(('localhost', 123))
sock.listen(1)

conn, addr = sock.accept()

while True:
    data = conn.recv(1024)

    if not data:
        break
    request = NTP_SERVER.request('pool.ntp.org')

    real_time = request.tx_time
    data = request.to_data()
    data_bytes = bytearray(data)

    new_time = struct.pack('!1I', TIME1970 + int(real_time) + time_difference)
    new_time_bytes = bytearray(new_time)
    data_bytes[40:43] = new_time_bytes
    request.from_data(data_bytes)

    conn.send(data_bytes)

conn.close()
