from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.config import APP_NAME, APP_VERSION
from app.websocket.manager import manager
from app.routes.debug_routes import router as debug_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)


# Communication pathway for frontend and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


# Register debug API routes
app.include_router(debug_router)

@app.get('/')
def root():
    return {
        'message': 'Evie backend running'
    }


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
