# LLM Chat

Converse with an Ollama model via a very simple Flask web app.

Original Credit for this app goes to: Shrinkhal01/CHATBOT-LLama-2
  
## Usage

1. **Configure and Install App Requirements:**
   ```bash 
   python -m venv venv
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
 