from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def tts(text: str, lang: str):
    # Dummy TTS: return text for now
    return {"audio_url": f"/static/{lang}_audio.mp3"}