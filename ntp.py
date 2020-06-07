import socket
import ntplib
from time import ctime



def print_time():
    ntpClient = ntplib.NTPClient()
    response = ntpClient.request('pool.ntp.org')

    print(ctime(response.tx_time))
    
if __name__ == "__main__":
    print_time()