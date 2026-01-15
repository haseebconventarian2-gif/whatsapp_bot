from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse, Response

from .azure import (
  audio_content_type,
  generate_text,
  synthesize_speech,
  transcribe_audio,
)
from .ui import UI_HTML


def create_app() -> FastAPI:
  app = FastAPI(title="Azure AI Bot")

  @app.get("/")
  def ui() -> Response:
    return Response(content=UI_HTML, media_type="text/html")

  @app.get("/health")
  def health() -> JSONResponse:
    return JSONResponse({"ok": True})

  @app.post("/text")
  async def text_reply(payload: dict) -> JSONResponse:
    user_text = str(payload.get("text") or "").strip()
    if not user_text:
      raise HTTPException(status_code=400, detail="Missing text")
    answer = await generate_text(user_text)
    return JSONResponse({"text": answer})

  @app.post("/audio")
  async def audio_reply(file: UploadFile = File(...)) -> Response:
    audio_bytes = await file.read()
    if not audio_bytes:
      raise HTTPException(status_code=400, detail="Missing audio file")

    transcript = await transcribe_audio(audio_bytes, file.filename or "", file.content_type)
    answer = await generate_text(transcript)
    audio_out = await synthesize_speech(answer)
    return Response(content=audio_out, media_type=audio_content_type())

  return app
