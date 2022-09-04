import asyncio
import websockets
import random
import time

n=0

async def echo(websocket, path):
    print('echo')
    async for msg in websocket:
        global n
        n+=1
        
        if msg.split(',')[3]=='-10' :
            print(n,msg.split(','))

        a=random.random()
        if a>0.95 :
            action='o'
        else :
            action='x'
        await asyncio.sleep(.02)
        await websocket.send(action)
        # print(f"> {greeting}")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 9999))
asyncio.get_event_loop().run_forever()