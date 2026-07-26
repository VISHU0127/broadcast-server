import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket):
      connected_clients.add(websocket)
      print("Client connected!")

      try:
            async for message in websocket:
                  print(f"Broadcasting:  {message}")
                  await broadcast(message)
      except websockets.exceptions.ConnectionClosed:
            print("Client disconnected!")
      finally:
            connected_clients.discard(websocket)
            print("Client removed.")

async def broadcast(message):
      if connected_clients:
            await asyncio.gather(*[client.send(message) for client in connected_clients])

async def server():
      async with websockets.serve(handle_client, "localhost", 8765):
            print("Broadcast Server started...")

            await asyncio.Future()

def start_server():
      asyncio.run(server())