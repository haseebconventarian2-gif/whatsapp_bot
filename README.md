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

Python · FastAPI · Azure OpenAI · LangChain · FAISS

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

<!-- code-audit-details -->

## 🔄 Runtime Flow

`Text/audio → Azure STT → Azure chat → Azure TTS/text`

This flow is derived from the current entry points and service calls.

## 🗂 Code Map

| Path | Responsibility |
| --- | --- |
| `__pycache__/` | Supporting resource |
| `api/` | Supporting resource |
| `app/` | Supporting resource |
| `docs/` | Supporting resource |
| `fastapi_app.py` | Supporting resource |
| `main.py` | Application entry point |
| `package.json` | Node.js dependencies |
| `package-lock.json` | Supporting resource |
| `requirements.txt` | Python dependencies |

## 🔐 Environment Variables

| Variable | Purpose |
| --- | --- |
| `AZURE_OPENAI_API_VERSION` | Azure OpenAI connection/model |
| `AZURE_TTS_FORMAT` | Optional runtime setting |
| `AZURE_TTS_VOICE` | Optional runtime setting |

## 🌐 Detected API Routes

| Method | Endpoint |
| --- | --- |
| `GET` | `/` |
| `GET` | `/health` |
| `POST` | `/audio` |
| `POST` | `/text` |

## 🧪 Validation Guide

1. Install dependencies in a clean virtual environment.
2. Start the documented entry point and test the root or health route.
3. Exercise one valid and one invalid request.
4. Verify external-service errors are handled clearly.
5. Confirm secrets, private data, indexes, and model artifacts are ignored.

## 🔒 Production Checklist

- Use managed secret storage and rotate exposed credentials.
- Add authentication, authorization, rate limiting, and request-size limits.
- Add automated tests, structured logging, monitoring, and health checks.
- Pin and audit dependencies.
- Define retention and privacy controls for audio and customer data.

## ⚠️ Code-Audit Notes

- Documentation reflects the current repository code and may expose integrations that need separate cloud accounts, model assets, or channel approval.
- Treat the project as a reference implementation until its security and deployment configuration are hardened.
