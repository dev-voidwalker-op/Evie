from app.websocket.manager import manager

async def send_emotion_event(emotion: str):

    await manager.broadcast({
        "type": "emotion",
        "emotion": emotion
    })


async def send_subtitle_event(text: str):

    await manager.broadcast({
        "type": "subtitle",
        "text": text
    })
