from flask import Flask, render_template, request, jsonify # These libraries are used to create the web application
import requests  
import json  
import os  
import yaml  

from ollamachatbot import OllamaChatbot

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

app = Flask(__name__) # Create the web application :)
model_name = config.get('llm', {})

 
@app.route('/')
def index():
    base_url = "http://localhost:11434" 
    chatbot = OllamaChatbot(base_url, model_name)
    chat_history = chatbot.chat_history
    return render_template('index.html', chat_history=chat_history)
#the index method is used to render the index.html file and display the chat history

@app.route('/chat', methods=['POST'])
def handle_chat():
    user_input = request.form['user_input']
    base_url = "http://localhost:11434" 
    chatbot = OllamaChatbot(base_url, model_name)
    response = chatbot.chat(user_input)
    return jsonify({'response': response})
#the handle_chat method is used to handle the chat functionality of the chatbot, including user input and generating responses


if __name__ == '__main__':
    app.run(debug=True)
#this condition is used to run the web application if the app.py file is executed directly
