import axios from 'axios';
import { saveAudio } from './mediaStore.js';

const TWILIO_BASE = 'https://api.twilio.com/2010-04-01';

function requireEnv(name) {
  const v = process.env[name];
  if (!v) throw new Error(`Missing required env var: ${name}`);
  return v;
}

function twilioAuth() {
  return {
    username: requireEnv('TWILIO_ACCOUNT_SID'),
    password: requireEnv('TWILIO_AUTH_TOKEN')
  };
}

function messageUrl() {
  const sid = requireEnv('TWILIO_ACCOUNT_SID');
  return `${TWILIO_BASE}/Accounts/${sid}/Messages.json`;
}

function baseUrl() {
  return requireEnv('PUBLIC_BASE_URL').replace(/\/+$/, '');
}

function audioContentType() {
  const format = (process.env.AZURE_TTS_FORMAT || 'mp3').toLowerCase();
  const isMp3 = format === 'mp3' || format === 'mpeg' || format === 'audio/mpeg';
  return isMp3 ? 'audio/mpeg' : 'audio/ogg';
}

export async function downloadMedia(mediaUrl) {
  const file = await axios.get(mediaUrl, {
    responseType: 'arraybuffer',
    auth: twilioAuth()
  });

  return Buffer.from(file.data);
}

export async function replyText(to, text) {
  const from = requireEnv('TWILIO_WHATSAPP_NUMBER');

  const body = new URLSearchParams({
    To: to,
    From: from,
    Body: text
  });

  await axios.post(messageUrl(), body, {
    auth: twilioAuth(),
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  });
}

export async function replyAudio(to, audioBuffer) {
  const from = requireEnv('TWILIO_WHATSAPP_NUMBER');
  const contentType = audioContentType();
  const mediaId = saveAudio(audioBuffer, contentType);
  const mediaUrl = `${baseUrl()}/media/${mediaId}`;

  const body = new URLSearchParams({
    To: to,
    From: from,
    MediaUrl: mediaUrl
  });

  await axios.post(messageUrl(), body, {
    auth: twilioAuth(),
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
  });
}
