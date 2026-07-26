import asyncio
import websockets
from app.logger import logger
from app.config import HOST, PORT
from app.websocket_manager import WebSocketManager
manager = WebSocketManager()

async def handle_client(websocket):
      username = await websocket.recv()
      manager.register(websocket, username)
      await manager.broadcast(f"📢 {username} joined the chat.")

      try:
           async for message in websocket:
                logger.info(f"Broadcasting: {message}")
                await manager.broadcast(f"{username}: {message}")

      except websockets.exceptions.ConnectionClosed:
            logger.info(f"{username} disconnected unexpectedly.")

      finally:
            manager.unregister(websocket)
            await manager.broadcast(f"📢 {username} left the chat.")

async def server():
      async with websockets.serve(handle_client, HOST, PORT):
            logger.info(f"Broadcast Server started running on ws://{HOST}:{PORT}")
            await asyncio.Future()

def start_server():
      try:
            asyncio.run(server())
      except KeyboardInterrupt:
            logger.info("Server stopped manually.")