# Broadcast Server

A CLI-based real-time broadcast server built with Python and WebSockets. Clients can connect to the server and send messages that are broadcast to all connected clients.

## Features

- CLI interface
- WebSocket server
- Multiple client support
- Real-time message broadcasting
- Username support
- Join/Leave notifications
- Graceful client disconnections

## Technologies Used

- Python 3.12
- asyncio
- websockets 16.x

## Project Structure

```
Broadcast-Server/
│
├── app/
│   ├── cli.py
│   ├── client.py
│   ├── config.py
│   ├── logger.py
│   ├── server.py
│   ├── websocket_manager.py
│   └── __init__.py
│
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/VISHU0127/Broadcast-Server.git
cd Broadcast-Server
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
python main.py start
```

## Running a Client

Open another terminal:

```bash
python main.py connect
```

Open multiple terminals and run the same command to connect multiple clients.

## Example

Server:

```text
Broadcast Server started on ws://localhost:8765
```

Client 1:

```text
Username: Alice
You: Hello everyone!
```

Client 2:

```text
Username: Bob

Received:
Alice: Hello everyone!
```

## Project Page

Roadmap.sh Project:
https://roadmap.sh/projects/broadcast-server

## GitHub Repository

https://github.com/VISHU0127/Broadcast-Server

## Future Improvements

- Private messaging
- Chat rooms
- Authentication
- Message history
- Docker support
- Unit tests
