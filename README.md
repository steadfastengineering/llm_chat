# Ollama Chatbot

The Ollama Chatbot is an AI-powered web application that facilitates real-time interaction with users. This chatbot is built with Flask for the backend and HTML, CSS, and jQuery for a responsive and user-friendly interface. It supports instant messaging, chat history, and can be customized with additional data to answer specific questions, making it ideal for various applications, including educational support. 

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
bash
-Copy code
-pip install flask requests
-ollama pull <desired_model>
-ollama serve
-You can download the pre-trained Ollama Llama 2 model from the Ollama GitHub repository.

-Run the application:

-bash
-Copy code
-python app.py
-Open your web browser:

-Navigate to http://localhost:5000 to start using the chatbot.

-File Structure
-app.py: Backend Flask application handling bot interactions.
-templates/index.html: Frontend HTML providing the chat interface.
-static/:
-artificial-intelligence.png: Bot avatar image.
-user.jpg: User avatar image.
-chat_history.json: Stores chat history for persistent conversations.
-Usage
-Sending Messages:
-Type your message in the input field and press Enter or click Send to send it.
 
License
This project is licensed under the MIT License. See the LICENSE file for details.
 