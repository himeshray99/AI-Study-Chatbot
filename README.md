# AI-Study-Chatbot
AI Study Chatbot using LLaMA (Ollama) and Streamlit for simple, level-based concept explanations.
# 📚 AI Study Chatbot (LLaMA - Local)

An AI-powered chatbot that explains concepts like a teacher using a local LLaMA model.

---
<img width="1246" height="744" alt="Video AI Study Chatbot" src="https://github.com/user-attachments/assets/7fac8815-dd14-4449-a813-ec365825db87" />

## 🚀 Features

* Ask any study-related question
* Get clear, simple explanations
* Choose difficulty level (Beginner / Intermediate / Advanced)
* Runs **locally using LLaMA (no API required)**

---

## 🧠 Tech Stack

* Python
* Streamlit
* Ollama (LLaMA model)

---

## ⚙️ Setup Instructions

### 1. Install Ollama

Download and install Ollama from:
https://ollama.com

---

### 2. Run LLaMA Model

Open Command Prompt / Terminal and run:

```bash
ollama run llama3
```

⚠️ Keep this running in the background.

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the App

```bash
streamlit run app.py
```

---

## 💡 Example Questions

* Explain photosynthesis
* What is machine learning?
* Explain Newton’s laws in simple terms

## ⚙️ How This App Works (Technical Overview)

The application follows a **client–server architecture** where the Streamlit frontend interacts with a locally hosted LLM via Ollama.

---

### 🔄 Request–Response Flow

1. **User Input (Frontend)**

   * The user enters a query in the Streamlit UI (`st.chat_input`).
   * A difficulty level (Beginner / Intermediate / Advanced) is selected.

---

2. **Prompt Construction**

   * The app dynamically constructs a prompt based on:

     * User query
     * Selected difficulty level
   * Example:

     ```
     Explain photosynthesis for a beginner with simple examples.
     ```

---

3. **API Call to Local LLM (Ollama)**

   * The app sends an HTTP POST request to the local Ollama server:

     ```python id="req01"
     POST http://localhost:11434/api/generate
     ```

   * Payload:

     ```json id="req02"
     {
       "model": "llama3",
       "prompt": "...",
       "stream": false
     }
     ```

---

4. **LLM Processing (LLaMA via Ollama)**

   * Ollama routes the request to the LLaMA model running locally.
   * The model performs:

     * Tokenization
     * Context processing
     * Text generation

---

5. **Response Handling**

   * Ollama returns a JSON response:

     ```json id="req03"
     {
       "response": "Generated explanation..."
     }
     ```
   * The app extracts:

     ```python id="req04"
     response.json()["response"]
     ```

---

6. **Frontend Rendering**

   * The response is displayed using Streamlit:

     * `st.chat_message()` for chat UI
     * `st.write()` for formatted output

---

### 🧠 Internal Components

#### 1. UI Layer (Streamlit)

* Handles:

  * User input
  * Layout & rendering
  * Chat interface

---

#### 2. Prompt Layer

* Responsible for:

  * Formatting user queries
  * Injecting learning level context
  * Ensuring structured outputs

---

#### 3. LLM Interface Layer (`utils/llm.py`)

* Handles communication with Ollama
* Abstracts API calls
* Ensures clean separation from UI

---

#### 4. Local Model Layer (Ollama + LLaMA)

* Runs entirely on local machine
* No external API calls
* Handles:

  * Inference
  * Token generation

---

### 🔄 Data Pipeline

```text id="pipe02"
User Input
   ↓
Streamlit UI (Frontend)
   ↓
Prompt Engineering Layer
   ↓
HTTP Request 
   ↓
Ollama Server
   ↓
LLaMA Model Inference
   ↓
Generated Response (JSON)
   ↓
Streamlit Rendering
```

---

### 🏗️ System Architecture (Detailed)

```text id="arch02"
+--------------------------+
|      Frontend UI         |
|      (Streamlit)         |
+------------+-------------+
             |
             v
+--------------------------+
|   Prompt Engineering     |
|  (Level-based logic)     |
+------------+-------------+
             |
             v
+--------------------------+
|   API Interface Layer    |
|  (HTTP request handler)  |
+------------+-------------+
             |
             v
+--------------------------+
|     Ollama Server        |
| (Local LLM Orchestrator) |
+------------+-------------+
             |
             v
+--------------------------+
|     LLaMA Model          |
|  (Text Generation Engine)|
+--------------------------+
```

---

### ⚡ Key Design Decisions

* **Local-first architecture**

  * No dependency on external APIs
  * Ensures privacy and offline capability

* **Separation of concerns**

  * UI, logic, and model interaction are modular

* **Prompt-driven control**

  * Difficulty level handled via prompt engineering

* **Stateless interaction**

  * Each query is processed independently
  * (No persistent memory yet)


### 🔮 Future Technical Enhancements

* Context memory (conversation history)
* Streaming responses (token-by-token)
* Vector database for retrieval (RAG)
* API abstraction layer for cloud deployment
* Multi-modal support (images, diagrams, 3D)

---


## ⚠️ Important Note

* This app runs **locally only**
* You must have Ollama and LLaMA installed
* It will not work on cloud platforms like Streamlit Cloud

---

## 🔮 Future Improvements

* Chat memory
* Better UI (chat bubbles)
* Voice input
* Deployment with API-based model

---

## 📷 Screenshot

<img width="1246" height="744" alt="Video AI Study Chatbot" src="https://github.com/user-attachments/assets/7fac8815-dd14-4449-a813-ec365825db87" />


⭐ If you like this project, give it a star!

