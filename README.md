# local-chatbot: French Chef Chatbot
 
A CLI conversational chatbot playing the role of a Michelin-starred French chef. Runs entirely locally via [Ollama](https://ollama.com).
 
> Built as part of an LLM & agentic AI learning journey - 4th year Computer Science Engineering, INSA Rouen.
 
---
 
## Demo
 
![Chatbot demo](assets/demo_chatbot.gif)
 
---
 
## Features
 
- Multi-turn conversation with full history memory
- Token-by-token streaming responses
- `reset` command to clear conversation memory
- `save` command to export conversation history as JSON
- `quit` command to exit
- Configurable personality via `config.py`
- Robust API error handling
---
 
## Stack
 
| Tool | Role |
|---|---|
| Python 3.12 | Language |
| [Ollama](https://ollama.com) | Local LLM inference |
| Mistral 7B | Language model |
| openai SDK | API client (Ollama-compatible) |
| python-dotenv | Environment variable management |
 
---
 
## Installation
 
### Prerequisites
 
- Mac with [Homebrew](https://brew.sh) or equivalent
- Python 3.12+
### 1. Clone the project
 
```bash
git clone https://github.com/kawtareg/local-chatbot
cd local-chatbot
```
 
### 2. Install Ollama and the model
 
```bash
brew install ollama
brew services start ollama
ollama pull mistral
```
 
### 3. Set up Python environment
 
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
 
### 4. Run the chatbot
 
```bash
python3 main.py
```
 
---
 
## Usage
 
```
Enter a query after >>>, quit to exit,
reset to clear memory, save to export the conversation.
 
>>> Bonjour, qui es-tu ?
>>> Give me a blanquette de veau recipe
>>> save
>>> reset
>>> quit
```
 
Saved conversations are stored in `history/` as JSON files.
 
---
 
## Project structure
 
```
local-chatbot/
├── main.py          # entry point
├── chatbot.py       # chatbot logic (streaming, history, commands)
├── config.py        # system prompt and model parameters
├── requirements.txt
├── history/         # saved conversations (git-ignored)
│   └── .gitkeep
└── .gitignore
```
 
---
 
## Customization
 
Edit `config.py` to change the chatbot personality:
 
```python
MODEL = "mistral"       # or llama3, phi3, gemma...
TEMPERATURE = 0.3       # 0 = deterministic, 1 = creative
 
SYSTEM_PROMPT = """You are a Michelin-starred French chef..."""
```
 
You can also swap `mistral` for any model available on Ollama:
 
```bash
ollama pull llama3
ollama pull phi3
ollama pull gemma
```
 
---
 
## What I learned
 
- LLM API calls with the openai SDK
- Conversation history management (`messages` format)
- Token-by-token streaming
- Modular Python project structure
- JSON data persistence
- Robust error handling with `try/except`
---
 
## Roadmap
 
- [ ] RAG system to give the chef access to external recipes
- [ ] Agentic version capable of searching recipes online
---
 
## Author
 
**Kawtar El Gueddari** — [GitHub](https://github.com/kawtareg) · INSA Rouen Normandie
