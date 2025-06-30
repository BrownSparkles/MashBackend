from flask import Flask, jsonify, render_template, request
import os
from google import genai
import json

app = Flask(__name__)

# Load Gemini API Key
GEMINI_API_KEY = "AIzaSyC1ny18rot1UEZ7kX2uy8vHrh7RWc-I2l0"

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key = GEMINI_API_KEY)

@app.route('/ai-categories', methods=['GET','POST'])
def get_ai_categories():
    theme = request.args.get('theme', 'classic')  # Default to 'classic' if empty
    # Now use `theme` as input to Gemini or category logic
    answer = None
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"""
            Generate a list of MASH game categories and 4 creative options each, for the theme "{theme}".
            Categories should be similar to: home, spouse, job, car, kids, pet, city.
            Return them as a JSON object.
            """
            )

        answer = json.loads(response.text.replace("```json","").replace("```",""))
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify(answer)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)