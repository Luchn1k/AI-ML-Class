# AI & ML Class Repository

This repository contains code examples, practice scripts, and hands-on exercises for learning Artificial Intelligence, Machine Learning, and Large Language Model (LLM) application development.

---

## 📂 Repository Contents

| File | Description | Key Topics / Libraries |
| :--- | :--- | :--- |
| [`chat_bot.py`](file:///c:/Users/kalan/Documents/Projects/AI-ML-Class/chat_bot.py) | Interactive CLI context-bounded chatbot ("Aria") powered by LangChain and Groq. Answers questions strictly from provided reference material (*The Red Pyramid*). | LangChain, System Prompts, Context Grounding |
| [`llm_connect.py`](file:///c:/Users/kalan/Documents/Projects/AI-ML-Class/llm_connect.py) | Connects to different LLM providers using LangChain's unified `init_chat_model` interface. | LangChain, Groq, OpenRouter |
| [`test.py`](file:///c:/Users/kalan/Documents/Projects/AI-ML-Class/test.py) | Directly queries the OpenRouter REST API using Python's `requests` library. | REST APIs, HTTP Requests, JSON Parsing |
| [`test2.py`](file:///c:/Users/kalan/Documents/Projects/AI-ML-Class/test2.py) | Interacts directly with the official Groq client SDK with real-time response streaming. | Groq SDK, Streaming Responses |
| [`python_function.py`](file:///c:/Users/kalan/Documents/Projects/AI-ML-Class/python_function.py) | Core Python fundamentals: function definitions, return values, variable scope (`global` vs `local`), conditionals, and loops. | Python Basics |

---

## 🛠️ Prerequisites & Installation

### 1. Python Environment
Ensure you have Python 3.10+ installed. It is recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
.\venv\Scripts\activate.bat
```

### 2. Install Required Dependencies

Install the necessary libraries for the scripts:

```bash
pip install langchain langchain-core groq requests
```

---

## 🔑 API Keys Configuration

Several scripts require API keys for LLM providers:
- **Groq API Key**: Get one from [Groq Console](https://console.groq.com/).
- **OpenRouter API Key**: Get one from [OpenRouter](https://openrouter.ai/).

> [!WARNING]
> Never commit real API keys to version control. Keep keys in a local file (such as `api_keys.txt`, which is already included in `.gitignore`) or use environment variables.

To set your Groq API key via environment variable:

```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

In the scripts, replace placeholders like `"ADD_YOUR_API_KEY"` with your actual key or load them via `os.environ`.

---

## 🚀 How to Run the Scripts

### 1. Context-Bounded Chatbot (`chat_bot.py`)
Runs an interactive conversation in the terminal with "Aria", a bot restricted to answering questions based on *The Red Pyramid* context:

```bash
python chat_bot.py
```
- Type your question and press `Enter`.
- Type `q` to exit the loop.

### 2. Unified LangChain Model Connection (`llm_connect.py`)
Demonstrates how LangChain can switch between model providers (Groq and OpenRouter) with minimal code changes:

```bash
python llm_connect.py
```

### 3. OpenRouter REST API Request (`test.py`)
Demonstrates calling the OpenRouter completions endpoint directly using HTTP POST:

```bash
python test.py
```

### 4. Groq Streaming Completions (`test2.py`)
Uses the official Groq Python SDK to stream completion tokens to the console as they are generated:

```bash
python test2.py
```

### 5. Python Fundamentals (`python_function.py`)
Runs basic exercises exploring functions, scope, and control flow:

```bash
python python_function.py
```

---

## 📝 License & Notes
Created for learning and demonstration purposes in the AI/ML Class.