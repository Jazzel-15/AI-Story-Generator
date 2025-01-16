from flask import Flask, render_template, request, jsonify
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the API key from the environment variable (this will be commented out during local testing)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded correctly (we won't need this check since we're mocking)
# if not openai.api_key:
#     raise ValueError("No API key found. Please check your .env file.")

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_story():
    """Handle story generation."""
    # Get inputs from the form
    character = request.form.get('character')
    setting = request.form.get('setting')
    theme = request.form.get('theme')

    # Create the prompt for the model
    prompt = f"Create a short story with the following details:\n" \
             f"- Main character: {character}\n" \
             f"- Setting: {setting}\n" \
             f"- Theme: {theme}\n"

    # --- Mocked Response (Currently Active) ---
    simulated_response = {
        'choices': [
            {'text': f"Once upon a time, there was a brave {character} in the {setting}. The theme of their adventure was {theme}."}
        ]
    }
    
    # Extract and return the generated story (mocked response)
    story = simulated_response['choices'][0]['text'].strip()

    # --- Uncomment the below code when you're ready to test with the real OpenAI API ---
    """
    try:
        # Call OpenAI API to generate the story (this is commented out for local testing)
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            prompt=prompt,
            max_tokens=300,
            temperature=0.7
        )
        
        # Extract and return the generated story
        story = response['choices'][0]['text'].strip()
    except Exception as e:
        # Return any error message
        return jsonify({"error": str(e)})
    """

    return jsonify({"story": story})

if __name__ == '__main__':
    app.run(debug=True)
