
# 🤖 Support Agent (AI Chat App)

This is an AI support agent that routes customer queries to different departments (like billing or technical). It's built using `openai-agents`.

---

## 📁 Simple Project Structure

```

support\_agent/
├── main.py            # Starts the app
├── config.py          # Loads API key from .env
├── context.py         # Handles user info
├── .env               # Stores API key

├── agents/            # AI agents live here
│   ├── triage.py      # Routes query to the right agent
│   ├── billing.py     # Handles billing issues
│   └── technical.py   # Handles technical issues

└── tools/             # Agent tools
├── refund.py      # Refund tool
└── restart\_service.py  # Restart service tool

````

---

## ⚙️ Quick Setup

1. **Create virtual environment**

```bash
uv venv support-agent
.\support-agent\Scripts\activate
````

2. **Install packages**

```bash
uv pip install openai-agents pydantic
```

3. **Add your API key to `.env` file**

```
OPENAI_API_KEY=your-key-here
```

4. **Run the app**

```bash
python main.py
```

---

## 🛡️ What Are Guardrails?

Guardrails are filters that clean the AI's reply.

**Example:** Removes the word "sorry"

```python
response = response.replace("sorry", "[filtered]")
```

You can add more filters as needed.

---

✅ That’s it! Your AI support agent is ready to run!

<img width="1282" height="781" alt="Screenshot 2025-08-03 203517" src="https://github.com/user-attachments/assets/9185e982-44a1-406a-afe1-84a90791cf8a" />





```

