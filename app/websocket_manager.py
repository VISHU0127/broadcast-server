import asyncio
from typing import Set
from websockets.asyncio.server import ServerConnection


class WebSocketManager:
    def __init__(self):
        self.connected_clients: Set[ServerConnection] = set()

    def register(self, websocket: ServerConnection):
        self.connected_clients.add(websocket)
        print(f"Client connected. Total clients: {len(self.connected_clients)}")

    def unregister(self, websocket: ServerConnection):
        self.connected_clients.discard(websocket)
        print(f"Client disconnected. Total clients: {len(self.connected_clients)}")

    async def broadcast(self, message: str):
        if not self.connected_clients:
            return 
        await asyncio.gather(*(client.send(message) for client in self.connected_clients))