# 🧠 Doc2Code Assistant

Your own **AI coding assistant** powered by **local language models** — no internet, no OpenAI, just raw power on your machine 💻⚡

---

## ✨ Features

✅ Runs entirely **locally** using `phi3:mini` (or any Ollama-supported model)  
✅ Uses your **GPU** for fast inference *(if available)*  
✅ Clean and interactive **Streamlit UI** for querying docs and generating code  
✅ **No dependencies** on OpenAI, APIs, or external services  
✅ Automatically checks for **GPU usage** 💪

---

## 🚀 Getting Started

### 1. 📦 Install Ollama

#### Linux/macOS

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows

Download the installer and follow the setup instructions.

### 2. 📥 Download a Model

#### Pull your preferred local model (default: phi3:mini):

```bash
ollama pull phi3:mini
```

You can also try others like `codellama:7b` or `mistral:7b`.

### 3. 🧪 (Optional) Test the Model in Terminal

```bash
ollama run phi3:mini
```

### 4. 🎛️ Run the App

```bash
streamlit run app.py
```

Then open your browser at http://localhost:8501

### 📝 Notes
Your documents should be placed in the docs/ folder. The assistant will index and learn from them automatically.

If you want to switch models, update the model name in app.py:

```bash
    llm = Ollama(model="your-model-name-here")
```

### ⚙️ Requirements

Python 3.10+
Ollama installed and running
Streamlit:

```bash
pip install streamlit llama-index llama-index-llms-ollama llama-index-embeddings-huggingface
```

### 🤝 Contributing
Ideas, improvements, or bugs? Open an issue or submit a PR — contributions are welcome!

### 🔐 License
MIT License
