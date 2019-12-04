import logging
import socket
from util import *

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

sock_A = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Configuração para Internet, UDP

sock_A.sendto(b'Message from A to server', (HOST, PORT))  # Envia mensagem para o servidor

while True:  # Loop do cliente
    data, addr = sock_A.recvfrom(1024)  # Leitura do buffer de recebimento
    print('client A received from {} : {}'.format(addr, data))  # Imprime o endereço do remetente (o servidor)
                                                                 # e a mensagem, que contém o endereço do outro cliente

    addr = msg_to_addr(data)  # Resgata o endereço do outro cliente a partir da mensagem do servidor


    sock_A.sendto(b'Message from A to B', addr)
    # Manda uma mensagem para o outro cliente com o endereço que recebeu do servidor. O NAT adiciona
     # uma tradução à sua tabela somente quando o sentido da comunicação é de dentro pra fora da rede.
     #
     # Sendo assim, sem o hole punching ou alguma outra técnica, não haveria como um dos clientes se
     # comportar como servidor, já que seu conjunto endereço/porta privado não estaria mapeado na tabela
     # de tradução


    data, addr = sock_A.recvfrom(1024)  # Leitura do buffer de recebimento
    print('client A received from {} : {}'.format(addr, data))  # Imprime o endereço do remetente (o outro cliente)
                                                                 # e a mensagem
