# Endereço do servidor
HOST = 'localhost'
PORT = 6001


def msg_to_addr(data):  # Pega o endereço recebido como DATA e transforma na dupla IP e PORT
    ip, port = data.decode('utf-8').strip().split(':')
    return ip, int(port)


def addr_to_msg(addr):  # Faz o inverso
    return '{}:{}'.format(addr[0], str(addr[1])).encode('utf-8')
