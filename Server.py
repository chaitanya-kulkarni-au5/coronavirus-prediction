# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(('0.0.0.0', 0))
# LISTEN_ADDRESS = ('0.0.0.0', sock.getsockname()[1])
# print(LISTEN_ADDRESS)
import json
LISTEN_ADDRESS = ('127.0.0.1', 9999)
import websockets
from Data_Handler import *
start_server = websockets.serve(Data, *LISTEN_ADDRESS)
import asyncio
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
