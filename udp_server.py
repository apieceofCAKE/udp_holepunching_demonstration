import logging
import socket
from util import *

logger = logging.getLogger()
addresses = []

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')  # Formação das mensagens de log

sock_S = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Configuração para Internet, UDP

sock_S.bind((HOST, PORT))  #Associa o socket ao endereço
print('\nServer: ' + HOST + ':' + str(PORT) + '\n')


while True:  #Loop do servidor
    data, addr = sock_S.recvfrom(1024)  # Leitura do buffer de recebimento

    logger.info("connection from %s. Message: %s", addr, data)  # Se há algo no buffer, imprime o endereço do
                                                                 # remetente e a mensagem

    addresses.append(addr)  # Adiciona o endereço do remetente ao vetor de endereços

    if len(addresses) >= 2:  # Se há mais de 1 endereço salvo no vetor de endereços, então temos dois clientes
                              # e podemos prosseguir com o hole punching

        logger.info("server - send client info to %s from %s", addresses[0], addresses[1])
        sock_S.sendto(addr_to_msg(addresses[1]), addresses[0])  # Manda o endereço do primeiro cliente que fez conexão
                                                                 # com o servidor para o segundo cliente

        logger.info("server - send client info to %s from %s", addresses[1], addresses[0])
        sock_S.sendto(addr_to_msg(addresses[0]), addresses[1])  # Vice versa

        addresses.pop(1)
        addresses.pop(0)  # Limpa o vetor de endereços
