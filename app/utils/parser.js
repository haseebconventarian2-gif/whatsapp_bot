export function parseMessage(payload) {
  try {
    const from = payload.From;
    if (!from) return null;

    const numMedia = Number(payload.NumMedia || 0);
    const mediaUrl = payload.MediaUrl0;
    const mediaType = payload.MediaContentType0;

    if (numMedia > 0 && mediaUrl && String(mediaType || '').startsWith('audio/')) {
      return { from, type: 'audio', mediaUrl, mediaType };
    }

    const text = payload.Body;
    if (text && String(text).trim()) {
      return { from, type: 'text', text };
    }

    return null;
  } catch {
    return null;
  }
}
