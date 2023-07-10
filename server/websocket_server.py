#!/usr/bin/env python

import asyncio
from websockets.server import serve
from pynput.mouse import Button, Controller
import webview
import threading


SERVER_IP = ""
SERVER_PORT = 2023
TOUCHSTART = 0x00
TOUCHMOVE = 0x01
TOUCHEND = 0x02
LEFT_BTN_PRESS = 0x03
LEFT_BTN_RELEASE = 0x04
RIGHT_BTN_PRESS = 0x05
RIGHT_BTN_RELEASE = 0x06
SCROLL = 0x07
LEFT_CLICK = 0x08
RIGHT_CLICK = 0x09

DELIMITER = "_"

mouse = Controller()

def twos_complement(hexstr, bits):
    value = int(hexstr, 16)
    if value & (1 << (bits - 1)):
        value -= 1 << bits
    return value

async def echo(websocket):
    async for message in websocket:
        #await websocket.send(message)
        print(message)
        msg = message.split(DELIMITER)
        cmd = int(msg[0])
        
        if cmd == TOUCHSTART:
            mouse.press(Button.left)
        elif cmd == TOUCHEND:
            mouse.release(Button.left)
            #pass
        elif cmd == TOUCHMOVE:
            #x =  twos_complement( str(msg[1]), 8 )
            #y = twos_complement( str(msg[2]), 8 )
            x = int(msg[1])
            y = int(msg[2])
            print(x, y)
            mouse.move(x,y)
        elif cmd == LEFT_CLICK:
            print("left click")
            mouse.click(Button.left)
        elif cmd == LEFT_BTN_PRESS:
            print("left press")
            mouse.press(Button.left)
        elif cmd == LEFT_BTN_RELEASE:
            print("left release")
            mouse.release(Button.left)
        elif cmd == RIGHT_BTN_PRESS:
            print("right press")
            mouse.press(Button.right)
        elif cmd == RIGHT_BTN_RELEASE:
            print("right release")
            mouse.release(Button.right)
        elif cmd == SCROLL:
            print("scroll")
            sc = int(msg[1])
            mouse.scroll(0,sc)

def get_local_ip():
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        SERVER_IP = s.getsockname()[0]
        print(SERVER_IP)
        s.close()
    except Exception as e:
        print("Exception while getting IP: {}".format(e))

async def _start_server():
    print('starting webserver at {}:{}'.format(SERVER_IP, SERVER_PORT))
    async with serve(echo, "0.0.0.0", SERVER_PORT):
        await asyncio.Future()  # run forever


def start_server():
    asyncio.run(_start_server())


def open_confirmation_dialog(window):
    result = window.create_confirmation_dialog('Question', 'Are you ok with this?')
    if result:
        print('User clicked OK')
    else:
        print('User clicked Cancel')

class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def get_server_ip(self):
        response = {
            'IP': 'Hello from Python {0}'.format(SERVER_IP)
        }
        return response


def main():
    get_local_ip()

    th = threading.Thread(target=start_server)

    api = Api()
    window = webview.create_window('Touchpad Server', 'assets/index.html', confirm_close=False, js_api=api)
    #webview.start(open_confirmation_dialog, window, debug=False)
    webview.start()

main()

