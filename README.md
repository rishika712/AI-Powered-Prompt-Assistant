# 🌟 AI-Powered Prompt Assistant  
A web-based AI Assistant built using **Google Gemini API** that performs multiple tasks based on user prompts. This project is designed for **Prompt Engineering** and demonstrates how prompt design impacts AI responses.  

---

## ✅ Features  
- **Answer Questions** – Get factual responses based on your queries.  
- **Summarize Text** – Summarize long paragraphs or articles into concise text.  
- **Generate Creative Content** – Write stories, poems, or creative ideas.  
- **Feedback Loop** – Collect user feedback (`helpful / not helpful`) and store it in `feedback.csv` for future improvements.  

---

## 🛠 Tech Stack  
- **Frontend**: HTML, CSS (Flask templates)  
- **Backend**: Python (Flask)  
- **AI Model**: Google Gemini (`gemini-1.5-flash`)  
- **Others**: dotenv for API key security  

---

## 📂 Project Structure  
AI-Powered-Prompt-Assistant/ai-assistant
│

├── app.py # Flask application

├── ai_helper.py # Handles AI requests & prompts

├── templates/

│ └── index.html # Web interface

├── static/

│ └── style.css # Styling

├── feedback.csv # Stores user feedback

├── requirements.txt # Requirements

└── .env # API Key (not uploaded to GitHub)

---

## ⚡ How It Works  
1. **Select a Function** – Choose from Answer Questions, Summarize Text, or Generate Creative Content.  
2. **Enter Your Input** – Type your query or text.  
3. **Get Responses** – AI generates responses based on well-designed prompts.  
4. **Provide Feedback** – Mark if the response was helpful (stored in `feedback.csv`).  

---

## 🔐 Setup & Installation  
### 1. Clone the repository  
```bash
git clone https://github.com/rishika712/AI-Powered-Prompt-Assistant.git
cd AI-Powered-Prompt-Assistant
```
### 2. Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure API Key
Create a .env file in the project root:
```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```
### 5. Run the Flask app
```bash
 python app.py
### The app will run on http://127.0.0.1:5000/.
```

---

## 📊 Feedback Storage

1. Feedback is collected after each response (Yes/No).

2. Saved in feedback.csv.

3. This can be analyzed later to refine prompts and improve the assistant.

---

## 🚀 Future Improvements

1. Add user authentication.

2. Include voice input and text-to-speech output.

3. Implement real-time feedback analysis.

---
