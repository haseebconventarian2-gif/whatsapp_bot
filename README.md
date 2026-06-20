<div align="center">

# WhatsApp AI Bot

WhatsApp AI bot using FastAPI and Azure OpenAI for text conversations, transcription, and synthesized voice replies.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Reference%20Implementation-6366F1)

</div>

---

## Overview

WhatsApp AI bot using FastAPI and Azure OpenAI for text conversations, transcription, and synthesized voice replies.

## Highlights

- Text conversation endpoint
- Speech-to-text and text-to-speech
- Conversational AI responses
- WhatsApp integration

## Tech Stack

Python Â· FastAPI Â· Azure OpenAI Â· LangChain Â· FAISS

## Getting Started

```bash
git clone https://github.com/haseebconventarian2-gif/whatsapp_bot.git
cd whatsapp_bot
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Configure Azure OpenAI deployments and any messaging-channel credentials in `.env`.

> Store credentials in `.env` and never commit secrets.

## Run

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Project Status

This is a learning and reference implementation. Review security, validation, monitoring, and deployment settings before production use.

## Detailed Code Reference

**Runtime flow:** `Text/audio -> STT -> retrieval -> LLM -> TTS/text -> channel reply`

### Repository map

- `__pycache__/` - supporting package or resources
- `api/` - supporting package or resources
- `app/` - supporting package or resources
- `docs/` - supporting package or resources
- `fastapi_app.py` - project file
- `main.py` - project file
- `package.json` - project file
- `package-lock.json` - project file
- `README.md` - project file
- `requirements.txt` - project file

### Validation checklist

1. Install dependencies in a clean virtual environment.
2. Configure only the environment variables needed by enabled integrations.
3. Start the documented entry point and test its health or root route.
4. Exercise successful and invalid requests.
5. Confirm secrets, private datasets, indexes, and model artifacts are ignored.

### Production checklist

- Use managed secret storage.
- Add authentication, authorization, rate limiting, and request-size limits.
- Add automated tests, structured logs, monitoring, and health checks.
- Pin and audit dependencies.
- Define retention and privacy controls for audio and customer data.

> This README reflects the current codebase. External AI, telephony, and messaging features require their respective accounts, assets, and approvals.

