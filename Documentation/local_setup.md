# 🧾 MASH Game Service – Local Setup Guide

This guide walks you through setting up and running a Flask-based MASH game category generator that uses the **Gemini (Google Generative AI)** API to generate themed content.

---

## 📦 Requirements

- Python 3.8+
- A Google account (to get a Gemini API key)
- Pip (Python package manager)

---

## 📁 Project Structure

```
MashBackend/
├── main.py
├── templates/
│   └── index.html
├── venv                 # (optional for storing the API key securely)
├── requirements.txt
```

---

## 🔐 1. Get a Gemini API Key

1. Go to [Google AI Studio API keys](https://makersuite.google.com/app/apikey)
2. Click **"Create API Key"**
3. Copy your API key (it starts with `AIza...`)
4. Optionally, save it in a `.env` file:

```
GEMINI_API_KEY=your-api-key-here
```

Or set it as an environment variable:

```bash
export GEMINI_API_KEY=your-api-key-here
```

---

## 🛠 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install required packages:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, create one with:

```txt
flask
google-generativeai
python-dotenv
```

Or install manually:

```bash
pip install flask google-generativeai python-dotenv
```

---

## 🧠 3. Code: `main.py`

```python
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
```

---

## 🖥️ 4. Frontend: `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>MASH Game - Themed Categories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2em;
            padding: 1em;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        input[type="text"] {
            width: 100%;
            padding: 0.5em;
            margin-top: 0.5em;
            font-size: 1em;
        }
        button {
            margin-top: 1em;
            padding: 0.5em 1em;
            font-size: 1em;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        pre {
            background-color: #eee;
            padding: 1em;
            border-radius: 5px;
            margin-top: 1em;
            white-space: pre-wrap; /* ✅ Fix to preserve indentation */
        }
    </style>
</head>
<body>
<div class="container">
    <label for="themeInput"><strong>Enter theme for MASH game</strong></label>
    <input type="text" name="theme" id="themeInput" placeholder="e.g. classic, sci-fi, fantasy, celebrity">
    <button onclick="getCategories()">Get Categories</button>

    <pre id="result"></pre>
</div>

<script>
    function getCategories() {
        const theme = document.getElementById('themeInput').value;
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = 'Loading...';
        fetch(`/ai-categories?theme=${encodeURIComponent(theme)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Failed to fetch categories");
                }
                return response.json();
            })
            .then(data => {
                resultDiv.textContent = JSON.stringify(data, null, 2);
            })
            .catch(error => {
                resultDiv.textContent = 'Error fetching categories.';
                console.error(error);
            });
    }
</script>
</body>
</html>
```

---

## ▶️ 5. Run the App

```bash
python main.py
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)