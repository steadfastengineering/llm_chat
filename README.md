# LLM Chat

Converse with a Ollama model via Flask web app.

Original Credit for this app goes to: Shrinkhal01/CHATBOT-LLama-2

## Features

- Real-time Messaging: Instantaneous chat interaction with the bot.
- Chat History: View and scroll through previous conversations.
- User-friendly Interface: Designed for easy navigation and interaction.
- Responsive Design: Works seamlessly across devices.
- **Chat History Storage:** Stores chat history in `chat_history.json` for persistent conversation history.

## Usage

1. **Configure and Install App Requirements:**
   ```bash 
   python install -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
2. **Ollama**
   ```bash
   sudo apt-get install ollama
   ollama serve
   ollama pull <desired_model_to_use:model_tag>
3. **Update app.py with model choice**
   ```python
   llm_model = '<desired_model_to_use:model_tag>'
4. **Run:**
   ```bash
   flask run
  
License
This project is licensed under the MIT License. See the LICENSE file for details.
 