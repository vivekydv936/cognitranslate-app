CogniTranslate 
The soul of translation.
CogniTranslate is a modern, web-based translation service powered by Google's Gemini generative AI. Unlike traditional translators, it focuses on providing natural, context-aware translations that preserve the tone and nuance of the original text. This project was built to demonstrate the practical application of Large Language Models (LLMs) in creating intelligent and user-friendly tools.

Live Demo: https://cognitranslate-app.vercel.app/



✨ Features
AI-Powered Translations: Leverages the Gemini 1.5 Flash model for high-quality, nuanced translations.

Multi-Language Support: A wide, alphabetized list of languages to choose from.

Context-Aware Prompts: Utilizes prompt engineering to ensure translations are contextually appropriate.

Responsive Design: A clean, modern, and fully responsive user interface that works on desktop and mobile devices.

Interactive UI: Smooth animations and a loading indicator provide a polished user experience.

State Persistence: Remembers your selected language even after a translation is complete.

🛠️ Technology Stack
Backend: Python with the Flask framework.

Frontend: HTML5, Tailwind CSS, and vanilla JavaScript.

AI Model: Google Gemini API.

Version Control: Git & GitHub.

Deployment: Vercel.

🚀 Getting Started
To run this project on your local machine, follow these steps:

Prerequisites
Python 3.x installed on your system.

A Google AI API Key. You can get one from Google AI Studio.

Installation & Setup
Clone the repository:

git clone [https://github.com/vivekydv936/cognitranslate-app.git](https://github.com/vivekydv936/cognitranslate-app.git)
cd cognitranslate-app

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows: .\venv\Scripts\Activate

On macOS/Linux: source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Configuration
The application requires your Google AI API key to function.

Open the app.py file.

Find the following line:

API_KEY = "YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with your actual API key.

Note: For a production deployment, it is critical to use environment variables instead of hardcoding the key.

Running the Application
With the dependencies installed and the API key configured, you can start the Flask development server:

flask run

Or, for a more reliable method:

python -m flask run

The application will be available at http://127.0.0.1:5000 in your web browser.

☁️ Deployment
This project is configured for easy deployment on Vercel. The vercel.json file in the root directory contains the necessary build and routing configurations. To deploy, simply import the GitHub repository into Vercel and add your API_KEY as an environment variable in the project settings.