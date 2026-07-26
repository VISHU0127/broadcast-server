import asyncio
from typing import Set, Dict
from websockets.asyncio.server import ServerConnection
from app.logger import logger

class WebSocketManager:
    def __init__(self):
        self.connected_clients: Set[ServerConnection] = set()
        self.usernames: Dict[ServerConnection, str] = {}

    def register(self, websocket: ServerConnection, username: str):
        self.connected_clients.add(websocket)
        self.usernames[websocket] = username
        logger.info(f"{username} connected.")

    def unregister(self, websocket: ServerConnection):
        self.connected_clients.discard(websocket)
        username = self.usernames.pop(websocket, "Unknown")
        logger.info(f"{username} disconnected.")

    async def broadcast(self, message: str):
        if not self.connected_clients:
            return 
        await asyncio.gather(
    *(client.send(message) for client in self.connected_clients),
        return_exceptions=True
        )