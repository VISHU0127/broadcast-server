import asyncio
import websockets
from app.websocket_manager import WebSocketManager
manager = WebSocketManager()

async def handle_client(websocket):
      manager.register(websocket)

      try:
            async for message in websocket:
                  print(f"Broadcasting:  {message}")
                  await manager.broadcast(message)
      except websockets.exceptions.ConnectionClosed:
            print("Client disconnected!")
      finally:
            manager.unregister(websocket)
            print("Client removed.")

async def server():
      async with websockets.serve(handle_client, "localhost", 8765):
            print("Broadcast Server started running on ws://localhost:8765")

            await asyncio.Future()

def start_server():
      asyncio.run(server())