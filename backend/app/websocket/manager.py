from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):

        # Stores all connected frontend clients
        self.active_connections = []


    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)


    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


    async def broadcast(self, message: dict):
        # Send event to all connected frontend clients
        for connection in self.active_connections:
            await connection.send_json(message)

# Global manager instance
manager = ConnectionManager()
