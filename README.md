# CureBot: Autonomous Offline Medical Assistance AI

CureBot is a privacy-first Streamlit chatbot that runs locally with Ollama and the TinyLlama model. It is designed to provide a simple offline medical-assistance style chat experience while keeping conversations on the user's machine.

> Note: CureBot is an educational AI assistant project and is not a replacement for professional medical advice, diagnosis, or emergency care.

## Features

- Offline inference through Ollama
- Streamlit-based chat interface
- Local conversation history using `st.session_state`
- Background image styling for the app interface
- Lightweight TinyLlama model configuration

## Tech Stack

- Python
- Streamlit
- Ollama
- TinyLlama

## Project Structure

```text
.
├── background.jpg
├── LICENSE
├── mental_support.py
├── README.md
├── readme.text
└── requirements.txt
```

## Prerequisites

Install Python 3.12 or later.

Install Ollama from:

```text
https://ollama.com
```

Pull the required local model:

```bash
ollama pull tinyllama
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rohanchauhan-15/CureBot-Autonomous-Offline-Medical-Assistance-AI.git
cd CureBot-Autonomous-Offline-Medical-Assistance-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The App

Start the Streamlit app:

```bash
streamlit run mental_support.py
```

Then open the local Streamlit URL shown in your terminal.

## How It Works

The app stores chat messages in Streamlit session state and sends the conversation history to the local TinyLlama model through Ollama. Responses are displayed back in the Streamlit UI, and no cloud API is required for model inference.

## License

This project is licensed under the terms included in the `LICENSE` file.

## Developer

Rohan Chauhan
