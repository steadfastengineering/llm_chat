# LLM Chat

Converse with an Ollama model via a very simple Flask web app.

Original Credit for this app goes to: Shrinkhal01/CHATBOT-LLama-2
  
## Usage

1. **Configure and Install App Requirements:**
   ```bash 
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Ollama**
   ```bash
   sudo apt-get install ollama
   ollama serve
   ollama pull <desired_model_to_use:model_tag>
   ```
3. **Update config.yaml as needed**
   ```JSON
   ...
   llm: llama3.2:1b
   embedding_model: "all-MiniLM-L6-v2"
   ...
   ```
5. **Run:**
   ```bash
   flask run
   ```
   or 
   ``` bash
   gunicorn -w 4 -b 0.0.0.0:1337 'app:app'
   ```

This project is licensed under the MIT License. 