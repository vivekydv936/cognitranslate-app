# app.py (version 8 - Favicon Fix)

import os
from flask import Flask, render_template, request, session, make_response

# --- Configure the Flask App ---
app = Flask(__name__)
# A secret key is required to use sessions in Flask
app.secret_key = os.urandom(24)

# --- Configure the Gemini API ---
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")
if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
    print("ERROR: GOOGLE_API_KEY not found in environment variables.")
else:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

# --- Centralized Language List ---
LANGUAGES = [
    "Arabic", "Bengali", "Chinese (Simplified)", "Dutch", "English",
    "French", "German", "Hindi", "Indonesian", "Italian", "Japanese",
    "Korean", "Polish", "Portuguese", "Russian", "Spanish", "Swedish",
    "Turkish", "Vietnamese"
]

# --- NEW: Route to handle favicon.ico requests ---
@app.route('/favicon.ico')
def favicon():
    # Return a 204 No Content response
    return make_response('', 204)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Initialize session history if it doesn't exist
    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':
        original_text = request.form.get('text_to_translate')
        target_language = request.form.get('target_language')
        source_language_form = request.form.get('source_language')
        
        translation_result = ""
        detected_language_display = ""
        final_source_language = source_language_form

        try:
            if not API_KEY or API_KEY == "YOUR_API_KEY_HERE":
                 raise ValueError("API Key is not configured.")

            if source_language_form == 'Detect Language':
                if original_text and original_text.strip():
                    detection_prompt = f"""Detect the language of the following text. Return only the name of the language. Text: "{original_text}" """
                    detection_response = model.generate_content(detection_prompt)
                    detected_language_name = detection_response.text.strip()
                    final_source_language = detected_language_name
                    detected_language_display = f"Detected: {detected_language_name}"

            if original_text and original_text.strip():
                translation_prompt = f"""Translate the following text from {final_source_language} to {target_language}. Only return the final translated text. Text: "{original_text}" """
                translation_response = model.generate_content(translation_prompt)
                translation_result = translation_response.text.strip()

                # Add successful translation to history
                history_item = {
                    'original': original_text,
                    'translation': translation_result,
                    'source': final_source_language,
                    'target': target_language
                }
                session['history'].insert(0, history_item)
                session['history'] = session['history'][:5]
                session.modified = True
            
        except Exception as e:
            translation_result = f"An error occurred: {e}"

        return render_template('index.html',
                               translation=translation_result,
                               original_text=original_text,
                               selected_target_language=target_language,
                               selected_source_language=source_language_form,
                               detected_language=detected_language_display,
                               history=session['history'],
                               languages=LANGUAGES)
    else:
        # Initial page load
        return render_template('index.html',
                               translation="",
                               original_text="",
                               selected_target_language="Spanish",
                               selected_source_language="Detect Language",
                               detected_language="",
                               history=session['history'],
                               languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
