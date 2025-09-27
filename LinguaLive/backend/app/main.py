from fastapi import FastAPI
from app.api import auth, translate, tts, stt

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(translate.router, prefix="/translate")
app.include_router(tts.router, prefix="/tts")
app.include_router(stt.router, prefix="/stt")

@app.get("/")
def root():
    return {"message": "LinguaLive API is up"}