import socket
import ntplib
from time import ctime
import struct
import time

time_difference = 0
TIME1970 = 2208988800

with open('config.txt', 'r') as config_file:
    time_difference = int(config_file.readline())

#NTP_SERVER = ntplib.NTPClient()
NTP_SERVER = "0.uk.pool.ntp.org"

def print_time():
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request('pool.ntp.org')

    print(ctime(response.tx_time))

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode('utf-8'), (NTP_SERVER, 123))
    data, address = client.recvfrom(1024)

    if data:
        print('Response received from:', address)

    t = struct.unpack('!12I', data ) [10]
    t -= TIME1970
    print('\tTime=%s' % time.ctime(t))

if __name__ == "__main__":
    #print_time()
    sntp_client()