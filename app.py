# app.py (version 4 - Final Fix)

import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# --- Configure the Gemini API ---
API_KEY = "AIzaSyDAHLpGZQAvhX8A7RkPvdKC9Zt8pit3_nc" # Make sure your key is here
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
# ---------------------------------

@app.route('/', methods=['GET', 'POST'])
def home():
    # This new logic separates the GET and POST requests completely.

    if request.method == 'POST':
        # This block only runs when the user submits the form.
        original_text = request.form.get('text_to_translate')
        target_language = request.form.get('target_language')
        translation_result = ""

        prompt = f"""
        Translate the following text from English to {target_language}.
        Do not provide any explanations or notes.
        Only return the final translated text.

        English text: "{original_text}"
        """
        try:
            response = model.generate_content(prompt)
            translation_result = response.text
        except Exception as e:
            translation_result = f"Error: {e}"

        # Render the page with the results AND the language they selected.
        return render_template('index.html',
                               translation=translation_result,
                               original_text=original_text,
                               selected_language=target_language)
    else:
        # This block only runs on the initial page load.
        # It renders the page with default empty values.
        return render_template('index.html',
                               translation="",
                               original_text="",
                               selected_language="Spanish") # Default language

if __name__ == '__main__':
    app.run(debug=True)