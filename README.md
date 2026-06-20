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
