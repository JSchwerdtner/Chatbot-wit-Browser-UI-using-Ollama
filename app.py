import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Initialize the Client with your Key
client = genai.Client(api_key=os.getenv("YOURGOOGLEAPIKEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.get_json().get("message", "")
    try:
        # We use a model, from which we know that it is in your list
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=user_input
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)