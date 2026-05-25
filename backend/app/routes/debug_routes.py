from fastapi import APIRouter
from app.websocket.events import (
    send_emotion_event,
    send_subtitle_event
)
from app.emotions.emotion_engine import emotion_engine

router = APIRouter()

@router.get('/test-emotion')
async def test_emotion():
    emotion = emotion_engine.get_random_emotion()
    await send_emotion_event(emotion)
    return {
        "emotion": emotion
    }


@router.get('/test-subtitle')
async def test_subtitle():
    text = 'Hello! How is your day going?'
    await send_subtitle_event(text)
    return {
        "subtitle": text
    }
