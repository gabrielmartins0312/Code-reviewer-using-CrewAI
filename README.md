# 🧠 Laravel Code Reviewer with CrewAI

This project leverages **CrewAI** to analyze and suggest improvements to PHP Laravel code using a multi-agent artificial intelligence system. It allows you to paste Laravel code and receive a detailed report with recommendations based on best practices, security, and clean code principles.

---

## 🚀 Why use CrewAI?

**CrewAI** is a powerful library for orchestrating collaborative AI agents. Instead of relying on a single agent to handle everything, this project utilizes **specialized agents**, each with its own responsibility:

- 📝 **Analyzer**: Understands the structure and semantics of the code
- 🔒 **Security Expert**: Identifies security flaws and vulnerabilities
- 🎯 **Refactoring Expert**: Applies clean code principles and Laravel best practices
- 🧪 **Final Reviewer**: Consolidates all suggestions into a clear final report

### ✅ Benefits of using multiple agents

- **Separation of concerns**: Each agent focuses on a specific aspect of the code
- **Improved accuracy** and depth of analysis
- **Collaborative intelligence**: Agents work together for more complete results
- **Scalability**: Easily add new roles like Testing, Performance, etc.

---

## ⚙️ Tech Stack

- **Python 3.11+**
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [LangChain](https://www.langchain.com/)
- **Flask** (API backend)
- **HTML + JavaScript (Bootstrap + Highlight.js)** for the frontend

---

## 💻 Getting Started

### 1. Clone the repository
```
git clone https://github.com/your-username/project-name.git
cd project-name
```

### 2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate    # On Linux/macOS
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set your OpenAI API key and Model

Create a .env file in the project root:
```
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL_NAME=your-model-name
```

### 5. Start the Flask backend
```
python app.py
```
This will start the server at http://127.0.0.1:5000.

### 6. Open the web interface
```
python -m http.server 8080
```
Then visit: http://localhost:8080

## 📄 How to Use

    Paste your Laravel PHP code into the textarea

    (Optional) Add a short description of the function

    Click Analyze Code

    Receive:

        Analyzed report with improvements

        Security and clean code suggestions

        Final refactored and indented function

## 🤝 Contributing

Pull requests are welcome!
Feel free to suggest new agents, improve the UI, or extend functionality.

## 🧠 Credits

This project is inspired by the open-source CrewAI initiative.
It was created to simplify and automate Laravel code review using AI-powered agents.
