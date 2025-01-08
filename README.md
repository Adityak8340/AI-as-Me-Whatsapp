<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5969/5969113.png" width="150" height="150"/>
  <h1>🤖 AI-as-Me WhatsApp Bot</h1>
  <p><i>A personal AI assistant that can impersonate you on WhatsApp!</i></p>

  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
  [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?logo=whatsapp&logoColor=white)](https://www.whatsapp.com)
  [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces)
</div>

---

<div align="center">
  <h3>🌟 Features</h3>
</div>

- 🧠 **Smart Conversations**: Powered by a fine-tuned LLM that learns your chat style
- 📱 **WhatsApp Integration**: Seamlessly works with WhatsApp through Green API
- 🔒 **Privacy Focused**: Only responds to specified contacts
- ⚡ **Real-time**: Instant message processing and responses
- 🎯 **Targeted Responses**: Personalized AI responses based on context

---

<div align="center">
  <h3>🚀 Quick Start</h3>
</div>

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/AI-as-Me-Whatsapp.git
cd AI-as-Me-Whatsapp
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure your environment**
   - Create a Green API account at [green-api.com](https://green-api.com)
   - Update `.env` with your credentials:
```properties
WA_INSTANCE="your-instance-id"
WA_TOKEN="your-api-token"
ALLOWED_SENDER="Contact Name"
TARGET_CHAT_ID="xxxxx@c.us"
```

4. **Run the bot**
```bash
python ai_me.py
```

---

<div align="center">
  <h3>🛠️ Architecture</h3>
</div>

```mermaid
graph LR
    A[WhatsApp Message] --> B[Green API]
    B --> C[AI-as-Me Bot]
    C --> D[Hugging Face Model]
    D --> C
    C --> B
    B --> E[Response to WhatsApp]
```

---

<div align="center">
  <h3>💡 Usage Examples</h3>
</div>

<table>
<tr>
<td>

```python
# Send a message to your bot
"Hey, what's up?"

# Bot responds with your style
"Just working on some code, 
thinking about grabbing coffee soon! 
How about you? 😊"
```

</td>
</tr>
</table>

---

<div align="center">
  <h3>🔮 Future Enhancements</h3>
</div>

- [ ] Multi-language support
- [ ] Voice message handling
- [ ] Image recognition capabilities
- [ ] Group chat support
- [ ] Advanced conversation memory

---

<div align="center">
  <h3>📜 License</h3>
  <p>MIT © 2024 Aditya Kumar Tiwari</p>
</div>

<style>
  h1 { color: #25D366; }
  h3 { color: #34B7F1; }
  table { width: 100%; }
  td { background-color: #f6f8fa; padding: 15px; }
  .center { text-align: center; }
</style>

<div align="center">
  <p>Made with ❤️ and ☕</p>
  <p><b>Star ⭐ this repo if you find it useful!</b></p>
</div>
