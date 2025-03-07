
import requests  
import json  
import os  
import yaml 

from logger import log

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

history = config.get('history', {})  

class OllamaChatbot:
    #the init function is used to initialize the chatbot with the base url, model, chat history, system prompt, and keep alive time
    def __init__(self, base_url, model):
        self.base_url = base_url
        self.model = model
        self.chat_history = self.load_chat_history()
        self.system_prompt = ""
        self.keep_alive = "10m"
     
    def load_chat_history(self):
        if history == True:
            if os.path.exists("chat_history.json"):
                with open("chat_history.json", "r") as file:
                    return json.load(file)
        return [] 

    def save_chat_history(self):
        with open("chat_history.json", "w") as file:
            json.dump(self.chat_history, file)
    #the save_chat_history function is used to save the chat history to the chat_history.json file


    def generate_completion(self, prompt, system_message="", stream=True):
        headers = {"Content-Type": "application/json"}
        data = {
            "model": self.model,
            "prompt": prompt,
            "stream": stream,
            "system": system_message,
            "keep_alive": self.keep_alive
        }
        response = requests.post(f"{self.base_url}/api/generate", headers=headers, data=json.dumps(data), stream=stream)
        
        if stream:
            full_response = ""
            for line in response.iter_lines():
                if line:
                    try:
                        response_part = json.loads(line.decode('utf-8'))['response']
                        full_response += response_part
                        log(response_part)
                        yield response_part
                    except (json.JSONDecodeError, KeyError) as e:
                        print(f"\nError parsing response: {e}")
                        return
        else:
            try:
                return response.json()['response']
            except (json.JSONDecodeError, KeyError) as e:
                print(f"\nError parsing response: {e}")
                return ""
    #the generate_completion function is used to generate a completion from the llama server using the prompt, system message, and keep alive time


    def chat(self, user_input):
        
        log(user_input)

        prompt = user_input

        # Save user query
        #self.chat_history.append({"role": "user", "content": user_input})
        #prompt = "\n".join([f"{entry['role']}: {entry['content']}" for entry in self.chat_history])
        
        try:
            full_message = ""
            for message in self.generate_completion(prompt, self.system_prompt):#generates completion
                full_message += message
            #self.chat_history.append({"role": "bot", "content": full_message})#appends completion to chat history
            #self.save_chat_history()
            return full_message
        except requests.exceptions.RequestException as e:#checks if there is an error
            print(f"\nError: {e}")
            return "Error: Failed to generate response." 
