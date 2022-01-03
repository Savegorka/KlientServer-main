import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, IP_ADDRESS, PORT
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):
    output = {
        ACTION: 'presence',
        USER: {
            ACCOUNT_NAME: account_name
        },
        TIME: time.time(),
    }
    return output


def answer(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:  # ???
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError

print(sys.argv)

def main():
    try:
        address = sys.argv[2]
        port = int(sys.argv[3])
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        address = IP_ADDRESS
        port = PORT
    except ValueError:
        print('НЗНД')
        return ''

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((address, port))
    server_message = create_presence()
    send_message(transport, server_message)
    try:
        printed = answer(get_message(transport))
        print(printed)
    except (ValueError, json.JSONDecodeError):
        print('ERROR')
