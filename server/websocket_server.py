#!/usr/bin/env python3.5

import asyncio
import base64
import io
from websockets.server import serve
from pynput.mouse import Button, Controller
import webview
import threading
import qrcode
import json

SERVER_IP = ""
SERVER_PORT = 2023
SERVER_QRCODE = b""
SENSITIVITY = 1

TOUCHSTART = "00"
TOUCHMOVE = "01"
TOUCHEND = "02"
LEFT_BTN_PRESS = "03"
LEFT_BTN_RELEASE = "04"
RIGHT_BTN_PRESS = "05"
RIGHT_BTN_RELEASE = "06"
SCROLL = "07"
LEFT_CLICK = "08"
RIGHT_CLICK = "09"
DBL_CLICK = "10"

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
        cmd = msg[0]
        
        if cmd == TOUCHSTART:
            mouse.press(Button.left)
        elif cmd == TOUCHEND:
            mouse.release(Button.left)
            #pass
        elif cmd == TOUCHMOVE:
            #x =  twos_complement( str(msg[1]), 8 )
            #y = twos_complement( str(msg[2]), 8 )
            x = float(msg[1]) * SENSITIVITY
            y = float(msg[2]) * SENSITIVITY
            print(x, y)
            mouse.move(x,y)
        elif cmd == LEFT_CLICK:
            print("left click")
            mouse.click(Button.left)
        elif cmd == RIGHT_CLICK:
            print("right click")
            mouse.click(Button.right)
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
        elif cmd == DBL_CLICK:
            print("dbl click")
            mouse.click(Button.left, 2)
        elif cmd == SCROLL:
            print("scroll")
            sc = int(msg[1])
            mouse.scroll(0,sc)

def get_local_ip():
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        global SERVER_IP
        SERVER_IP = s.getsockname()[0]
        print(SERVER_IP)
        s.close()
    except Exception as e:
        print("Exception while getting IP: {}".format(e))

async def _start_server():
    global SERVER_IP, SERVER_PORT
    print('starting webserver at {}:{}'.format(SERVER_IP, SERVER_PORT))
    async with serve(echo, "0.0.0.0", SERVER_PORT):
        await asyncio.Future()  # run forever


def start_server():
    asyncio.run(_start_server())


def open_confirmation_dialog(window):
    #get_local_ip()
    print("SERVER IP: {}".format(SERVER_IP))
    if SERVER_IP == "":
        result = window.create_confirmation_dialog('No Connection Detected\nCheck Your Connection Settings and Try Again')
        if result:
            print('User clicked OK')
        else:
            print('User clicked Cancel')
        window.destroy()
    
def get_server_port():
    global SERVER_PORT, SENSITIVITY
    try:
        '''with open('config.json', 'r') as f:
            fn = f.read()
            if( len(fn) < 1):
                SERVER_PORT = "2023"
            SERVER_PORT = fn'''
        
        with open('config.json', 'r') as f:
            fn = json.load(f)
            SERVER_PORT = fn["port"]
            SENSITIVITY = float(fn["sensitivity"])

    except Exception as e:
        print("file open error: {}".format(e))
        SERVER_PORT = "2023"
        with open('config.json', 'w') as f:
            fw = {}
            fw["port"] = SERVER_PORT
            fw["sensitivity"] = SENSITIVITY
            json.dump(fw, f)
            
    print(SERVER_PORT)
    print(SENSITIVITY)

def get_qrcode_image():
    global SERVER_IP, SERVER_PORT, SERVER_QRCODE
    val = SERVER_IP + ":" + str(SERVER_PORT)
    print(val)
    #SERVER_QRCODE =  pyqrcode.create(val, mode='binary')
    #print(SERVER_QRCODE.text())
    qr = qrcode.QRCode()
    qr.add_data(val)
    img = qr.make_image()

    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    SERVER_QRCODE = base64.b64encode(buffered.getvalue()).decode("utf-8")
    #return img_str

    #img.save('qrcode.png')
    #print(SERVER_QRCODE)

class Api:
    def __init__(self):
        pass

    def get_server_ip(self):
        global SERVER_IP, SERVER_PORT, SENSITIVITY
        return [SERVER_IP, SERVER_PORT, SENSITIVITY]
    

    def save_server_settings(self, port, sensitivity):
        global SERVER_PORT, SENSITIVITY
        print("PORT: {}".format(port))
        try:
            fr = open('config.json', 'r')
            fr = json.load(fr)
        except FileNotFoundError:
            fr = {}
        
        fr["port"] = port
        fr["sensitivity"] = sensitivity
        with open('config.json', 'w') as fw:
            try:
                #f.write(port)
                #f.close()
                json.dump(fr, fw)
                SENSITIVITY = float(sensitivity)
                SERVER_PORT = port
                return True
            except Exception as e:
                print(e)
                return False
        #return False
    
    def get_server_qrcode(self):
        global SERVER_QRCODE
        return SERVER_QRCODE
        '''try:
            with open('qrcode.png', 'rb') as f:
                fs =  base64.b64encode( f.read() )
                #print(fs.decode('utf-8'))
                return fs.decode('utf-8')
        except Exception as e:
            print("open img err: {}".format(e))
            return ""
        '''

def main():
    get_local_ip()
    get_server_port()
    print( get_qrcode_image() )

    th = threading.Thread(target=start_server)
    th.start()

    api = Api()
    window = webview.create_window('Touchpad Server', 'index.html', confirm_close=False, js_api=api)
    webview.start(open_confirmation_dialog, window, debug=False)
    #webview.start(debug=True)

main()

