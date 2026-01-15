import { parseMessage } from './utils/parser.js';
import { replyText, replyAudio, downloadMedia } from './services/whatsapp.js';
import { transcribeAudio, generateText, synthesizeSpeech } from './services/azure.js';

export async function verifyWebhook(req, res) {
  return res.status(200).send('OK');
}

export async function handleMessage(req, res) {
  // WhatsApp expects a quick ACK; do work after ACK.
  res.sendStatus(200);

  const msg = parseMessage(req.body);
  if (!msg) return;

  try {
    if (msg.type === 'text') {
      const answer = await generateText(msg.text);
      await replyText(msg.from, answer);
      return;
    }

    if (msg.type === 'audio') {
      const audioBuffer = await downloadMedia(msg.mediaUrl);
      const transcript = await transcribeAudio(audioBuffer);
      const answer = await generateText(transcript);
      const audioOut = await synthesizeSpeech(answer);
      await replyAudio(msg.from, audioOut);
      return;
    }
  } catch (err) {
    console.error('Handler error:', err?.response?.data || err?.message || err);
  }
}
