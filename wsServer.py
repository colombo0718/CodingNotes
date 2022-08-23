import asyncio
import websockets

async def echo(websocket, path):
    print('echo')
    async for msg in websocket:
        print(msg ,'received from client')
        greeting = f"Hello {msg}!"
        await websocket.send(greeting)
        print(f"> {greeting}")

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 9998))
asyncio.get_event_loop().run_forever()