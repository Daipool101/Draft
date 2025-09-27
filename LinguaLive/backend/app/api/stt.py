from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def stt(audio_file: bytes, lang: str):
    # Dummy STT: return fixed string
    return {"transcript": "Hello World"}