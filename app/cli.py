import argparse

from app.server import start_server
from app.client import connect_client

def run():
      parser = argparse.ArgumentParser(description="Broadcast Server CLI")

      parser.add_argument("command", choices=["start", "connect"], help="Command to execute")

      args = parser.parse_args()

      if args.command == "start":
            start_server()
      else:
            connect_client()