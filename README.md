# GenAI Chatbot with LangChain

## 🌟 Overview
This project is a Generative AI-powered chatbot built with LangChain, designed to provide natural and intelligent responses to user queries. It integrates multiple language models and supports flexible interactions.

---

## 🛠️ Features
- Support for multiple LLMs (e.g., `llama3`, `mixtral`).
- Customizable system prompts to define agent behavior.
- User-friendly web-based interface.
- Easily extendable architecture using LangChain.
- API-driven chatbot interaction.


## ⚙️ Installation

### Prerequisites
- Python 3.8+
- `pip` package manager

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/Arjun-commit/GenAI_chatbot_langchain.git
   cd GenAI_chatbot_langchain

2. Create a Python virtual environment:
    python -m venv venv
    source venv/bin/activate   # For Linux/MacOS
    venv\Scripts\activate      # For Windows

3. Install the dependencies:
    pip install -r requirements.txt

4. Run the application:
    python -m uvicorn App.main:app --reload


🖼️ Directory Structure
GenAI_chatbot_langchain/
├── app.py                # Backend application entry point
├── requirements.txt      # Python dependencies
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
├── frontend/             # Frontend code (React or other framework)
├── README.md             # Documentation
└── demo/                 # Screenshots or demo files


📖 Usage
Define Your AI Agent:

Enter a system prompt to customize the chatbot's personality and behavior.
Choose a Model:

Select an AI model from the dropdown (e.g., llama3, mixtral).
Enter Your Query:

Type a message and press "Submit."
Wait for the Response:

A response will be generated and displayed in the interface.


⚡ API Reference
The backend provides an API endpoint for interacting with the chatbot.

POST /chat


Request Body:
{
  "messages": ["Your input message here"],
  "model_name": "llama3-70b-8192",
  "system_prompt": "Define AI behavior here"
}

Response:
{
  "messages": [
    {
      "type": "user",
      "content": "Your input message here"
    },
    {
      "type": "ai",
      "content": "The chatbot's response"
    }
  ]
}


🛠️ Contributing
Contributions are welcome! Follow these steps to contribute:

1. 
Fork the repository.
Create a feature branch:

2. 
git checkout -b feature-name
Commit your changes:

3. 
git commit -m "Add new feature"
Push to your branch and create a pull request.


💬 Support
If you encounter any issues or have suggestions, feel free to open an issue in this repository.