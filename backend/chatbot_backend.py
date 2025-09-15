from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Use environment variable for security
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)  # Allow frontend to call this API

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "Please send a message!"})

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": user_message}]
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
