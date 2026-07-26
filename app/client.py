import asyncio
import websockets
from app.config import HOST, PORT

async def send_messages(websockets):
      while True:
            message = await asyncio.to_thread(input, "You: ")
            await websockets.send(message)

async def receive_messages(websockets):
      async for message in websockets:
            print(f"\nReceived: {message}")

async def client():
      uri = f"ws://{HOST}:{PORT}"
      username = input("Username:")

      async with websockets.connect(uri) as websocket:
            await websocket.send(username)
            print("Connected to server!")

            await asyncio.gather(send_messages(websocket), receive_messages(websocket))

def connect_client():
      asyncio.run(client())