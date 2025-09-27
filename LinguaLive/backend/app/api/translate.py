from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def translate(text: str, src_lang: str, tgt_lang: str):
    # Dummy translation for MVP
    return {"translated_text": f"[{tgt_lang}] {text}"}