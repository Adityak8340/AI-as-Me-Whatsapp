<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/5969/5969113.png" width="150" height="150"/>
  <h1 style="color: #25D366;">🤖 AI-as-Me WhatsApp Bot</h1>
  <p><i>A personal AI assistant that can impersonate you on WhatsApp!</i></p>

  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
  [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?logo=whatsapp&logoColor=white)](https://www.whatsapp.com)
  [![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow)](https://huggingface.co/spaces)
</div>

---

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">🌟 Features</h3>
</div>

- 🧠 **Smart Conversations**: Powered by a fine-tuned LLM that learns your chat style
- 📱 **WhatsApp Integration**: Seamlessly works with WhatsApp through Green API
- 🔒 **Privacy Focused**: Only responds to specified contacts
- ⚡ **Real-time**: Instant message processing and responses
- 🎯 **Targeted Responses**: Personalized AI responses based on context

---

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">🚀 Quick Start</h3>
</div>

1. **Clone the repository**
```bash
git clone https://github.com/adityak8340/AI-as-Me-Whatsapp.git
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

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">🛠️ Architecture</h3>
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

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">💡 Usage Examples</h3>
</div>

<div style="width: 100%; background-color: #f6f8fa; padding: 15px; border-radius: 6px;">

```python
# Send a message to your bot
"Hey, what's up?"

# Bot responds with your style
"Just working on some code, 
thinking about grabbing coffee soon! 
How about you? 😊"
```

</div>

---

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">🔮 Future Enhancements</h3>
</div>

- [ ] Multi-language support
- [ ] Voice message handling
- [ ] Image recognition capabilities
- [ ] Group chat support
- [ ] Advanced conversation memory

---

<div align="center" style="margin: 30px 0;">
  <h3 style="color: #34B7F1;">📜 License</h3>
  <p>MIT © 2024 Aditya Kumar Tiwari</p>
</div>

<div align="center" style="margin-top: 50px; padding: 20px; background-color: #f8f9fa; border-radius: 6px;">
  <p style="margin: 10px 0;">Made with ❤️ and ☕</p>
  <p style="font-weight: bold;">Star ⭐ this repo if you find it useful!</p>
</div>
<div align="center" style="margin: 30px 0;">
  <div class="tech-stack" style="display: flex; justify-content: center; gap: 20px; margin: 20px 0;">
    <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" width="50" height="50" class="tech-icon" style="animation: float 3s ease-in-out infinite;"/>
    <img src="https://www.vectorlogo.zone/logos/whatsapp/whatsapp-icon.svg" width="50" height="50" class="tech-icon" style="animation: float 3s ease-in-out infinite 0.2s;"/>
    <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="50" height="50" class="tech-icon" style="animation: float 3s ease-in-out infinite 0.4s;"/>
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" width="50" height="50" class="tech-icon" style="animation: float 3s ease-in-out infinite 0.4s;"/>
  </div>
</div>

<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}
.tech-icon:hover {
  transform: scale(1.2);
  transition: transform 0.3s ease;
}
</style>
<div align="center">
    <br>
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF69B4&center=true&vCenter=true&width=435&lines=Built+with+%E2%9D%A4%EF%B8%8F;Feel+free+to+contribute!" alt="Typing SVG" />
    <p align="center">
        <img src="https://img.shields.io/github/stars/adityak8340/AI-as-Me-Whatsapp?style=social" alt="Stars">
        <img src="https://img.shields.io/github/forks/adityak8340/AI-as-Me-Whatsapp?style=social" alt="Forks">
        <img src="https://img.shields.io/github/issues/adityak8340/AI-as-Me-Whatsapp?style=social" alt="Issues">
    </p>
</div>