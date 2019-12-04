import logging
import socket
from util import *

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

sock_B = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock_B.sendto(b'Message from B to server', (HOST, PORT))

while True:
    data, addr = sock_B.recvfrom(1024)
    print('client B received from {} : {}'.format(addr, data))

    addr = msg_to_addr(data)

    sock_B.sendto(b'Message from B to A', addr)

    data, addr = sock_B.recvfrom(1024)
    print('client B received from {} : {}'.format(addr, data))
