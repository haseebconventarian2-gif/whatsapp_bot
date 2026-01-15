UI_HTML = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Azure AI Bot</title>
    <style>
      :root {
        --bg: #0c1317;
        --panel: #111b21;
        --chat: #0b141a;
        --incoming: #202c33;
        --outgoing: #005c4b;
        --text: #e9edef;
        --muted: #8696a0;
        --accent: #25d366;
      }
      * { box-sizing: border-box; }
      body {
        margin: 0;
        font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
        background: linear-gradient(180deg, #0c1317, #0b141a 50%, #0b141a);
        color: var(--text);
      }
      .app {
        max-width: 980px;
        margin: 24px auto;
        padding: 16px;
      }
      .shell {
        border-radius: 16px;
        overflow: hidden;
        background: var(--panel);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
        border: 1px solid #1f2a30;
      }
      .topbar {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 14px 16px;
        background: #202c33;
      }
      .avatar {
        width: 36px;
        height: 36px;
        border-radius: 999px;
        background: linear-gradient(135deg, #25d366, #128c7e);
      }
      .title {
        font-size: 16px;
        font-weight: 600;
      }
      .subtitle {
        color: var(--muted);
        font-size: 12px;
      }
      .chat {
        background:
          radial-gradient(500px 300px at 80% 0%, rgba(255,255,255,0.02), transparent),
          var(--chat);
        min-height: 420px;
        padding: 18px;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
      .bubble {
        max-width: 75%;
        padding: 10px 12px;
        border-radius: 12px;
        line-height: 1.35;
        font-size: 14px;
        word-wrap: break-word;
      }
      .incoming { background: var(--incoming); align-self: flex-start; }
      .outgoing { background: var(--outgoing); align-self: flex-end; }
      .composer {
        display: grid;
        grid-template-columns: 1fr auto auto;
        gap: 8px;
        padding: 12px;
        border-top: 1px solid #1f2a30;
        background: #111b21;
      }
      .input {
        width: 100%;
        padding: 10px 12px;
        border-radius: 10px;
        border: 1px solid #1f2a30;
        background: #202c33;
        color: var(--text);
      }
      .btn {
        border: none;
        border-radius: 10px;
        padding: 10px 12px;
        cursor: pointer;
        font-weight: 600;
      }
      .btn.send { background: var(--accent); color: #0b141a; }
      .btn.mic { background: #2a3942; color: var(--text); }
      .panel {
        display: grid;
        grid-template-columns: 1fr auto auto;
        gap: 8px;
        padding: 12px;
        border-top: 1px solid #1f2a30;
        background: #111b21;
      }
      .hint { color: var(--muted); font-size: 12px; }
      @media (max-width: 700px) {
        .composer, .panel { grid-template-columns: 1fr; }
        .bubble { max-width: 90%; }
      }
    </style>
  </head>
  <body>
    <div class="app">
      <div class="shell">
        <div class="topbar">
          <div class="avatar"></div>
          <div>
            <div class="title">Azure AI Bot</div>
            <div class="subtitle">online • text or voice</div>
          </div>
        </div>
        <div class="chat" id="chat">
          <div class="bubble incoming">Send a text or record a voice note to start.</div>
        </div>
        <div class="composer">
          <input id="textInput" class="input" placeholder="Type a message" />
          <button class="btn send" id="sendText">Send</button>
          <button class="btn mic" id="recordBtn">Record</button>
        </div>
        <div class="panel">
          <input id="audioFile" class="input" type="file" accept="audio/*" />
          <button class="btn mic" id="sendAudio">Send Audio</button>
          <div class="hint" id="recordHint">Mic ready</div>
        </div>
      </div>
    </div>
    <script>
      const textInput = document.getElementById("textInput");
      const audioFile = document.getElementById("audioFile");
      const chat = document.getElementById("chat");
      const recordBtn = document.getElementById("recordBtn");
      const recordHint = document.getElementById("recordHint");

      let mediaRecorder = null;
      let chunks = [];

      function addBubble(text, type) {
        const bubble = document.createElement("div");
        bubble.className = "bubble " + type;
        bubble.textContent = text;
        chat.appendChild(bubble);
        chat.scrollTop = chat.scrollHeight;
        return bubble;
      }

      function addAudioBubble(blob, type) {
        const bubble = document.createElement("div");
        bubble.className = "bubble " + type;
        const audio = document.createElement("audio");
        audio.controls = true;
        audio.src = URL.createObjectURL(blob);
        audio.style.width = "220px";
        bubble.appendChild(audio);
        chat.appendChild(bubble);
        chat.scrollTop = chat.scrollHeight;
      }

      async function sendText() {
        const text = (textInput.value || "").trim();
        if (!text) return;
        addBubble(text, "outgoing");
        textInput.value = "";
        const thinking = addBubble("...", "incoming");
        const res = await fetch("/text", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text })
        });
        const data = await res.json().catch(() => ({}));
        thinking.textContent = data.text || ("Error: " + res.status);
      }

      async function sendAudio(file) {
        if (!file) return;
        addAudioBubble(file, "outgoing");
        const thinking = addBubble("Voice note received...", "incoming");
        const form = new FormData();
        form.append("file", file);
        const res = await fetch("/audio", { method: "POST", body: form });
        if (!res.ok) {
          thinking.textContent = "Error: " + res.status;
          return;
        }
        const blob = await res.blob();
        thinking.remove();
        addAudioBubble(blob, "incoming");
      }

      document.getElementById("sendText").addEventListener("click", sendText);
      textInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") sendText();
      });

      document.getElementById("sendAudio").addEventListener("click", async () => {
        if (!audioFile.files.length) return;
        await sendAudio(audioFile.files[0]);
        audioFile.value = "";
      });

      async function startRecording() {
        if (!navigator.mediaDevices?.getUserMedia) {
          recordHint.textContent = "Mic not supported in this browser.";
          return;
        }
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          mediaRecorder = new MediaRecorder(stream);
          chunks = [];
          mediaRecorder.ondataavailable = (e) => { if (e.data.size) chunks.push(e.data); };
          mediaRecorder.onstop = async () => {
            const blob = new Blob(chunks, { type: mediaRecorder.mimeType });
            stream.getTracks().forEach((t) => t.stop());
            recordHint.textContent = "Sending voice note...";
            await sendAudio(blob);
            recordHint.textContent = "Mic ready";
            recordBtn.textContent = "Record";
          };
          mediaRecorder.start();
          recordHint.textContent = "Recording...";
          recordBtn.textContent = "Stop";
        } catch (err) {
          recordHint.textContent = "Mic access denied.";
        }
      }

      recordBtn.addEventListener("click", async () => {
        if (mediaRecorder && mediaRecorder.state === "recording") {
          mediaRecorder.stop();
          return;
        }
        await startRecording();
      });
    </script>
  </body>
</html>
"""
