import json
from variables import MAX_PACKAGE_LENGTH

def get_message(user):
    encoded_response = user.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        raise ValueError
    raise ValueError


def send_message(socket, message):
    js_message = json.dumps(message)
    message_encode = js_message.encode('utf-8')
    socket.send(message_encode)
