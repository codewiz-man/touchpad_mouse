#!/usr/bin/env python

import asyncio
from websockets.server import serve
from pynput.mouse import Button, Controller

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


async def main():
    async with serve(echo, "0.0.0.0", 2023):
        await asyncio.Future()  # run forever

asyncio.run(main())
