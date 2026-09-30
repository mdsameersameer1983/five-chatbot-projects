import os
from flask import Flask, render_template, request, jsonify
from google import genai
from google.genai import types

app = Flask(__name__)
SYSTEM_PROMPT = 'You are a patient coding helper. Explain code and errors in plain language, ask for missing context, and provide small runnable examples. Call out assumptions, versions, and security concerns when relevant. Never claim code was executed unless it was. Encourage users to share language, framework, and full error text.'

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify(error="Please enter a message."), 400
    if len(message) > 8000:
        return jsonify(error="Please keep your message under 8,000 characters."), 413
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return jsonify(error="The chatbot is not configured yet. Add GEMINI_API_KEY to the environment."), 503
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"), contents=message, config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT, temperature=0.7))
        if not response.text:
            raise ValueError("The model returned an empty response.")
        return jsonify(reply=response.text)
    except Exception:
        app.logger.exception("Gemini request failed")
        return jsonify(error="I couldn’t get a response just now. Please try again in a moment."), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=False)
