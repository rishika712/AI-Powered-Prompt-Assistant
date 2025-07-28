import google.generativeai as genai
import os
from dotenv import load_dotenv
import csv

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Three functions with prompt variations
def answer_question(query):
    prompts = [
        f"Answer this question concisely: {query}",
        f"Explain in detail: {query}",
        f"Give 3 interesting facts about: {query}"
    ]
    return [ai_response(p) for p in prompts]

def summarize_text(text):
    prompts = [
        f"Summarize this text in 3 sentences: {text}",
        f"Provide key bullet points for: {text}",
        f"Write a short overview: {text}"
    ]
    return [ai_response(p) for p in prompts]

def generate_creative_content(topic):
    prompts = [
        f"Write a short story about {topic}",
        f"Create a poem about {topic}",
        f"Generate a creative idea involving {topic}"
    ]
    return [ai_response(p) for p in prompts]

# Feedback storage
def save_feedback(response_text, feedback_value):
    with open('feedback.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([response_text, feedback_value])
