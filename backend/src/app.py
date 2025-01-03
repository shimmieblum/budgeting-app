import os
from flask import Flask, request, jsonify
from transformers import pipeline
from dotenv import load_dotenv
from flask_cors import CORS

from ..models.geminiModelWrapper import GeminiWrapper

load_dotenv()

app = Flask(__name__)
CORS(app)
HUGGING_FACE_TOKEN = os.getenv('HF_TOKEN')

model = GeminiWrapper('gemini-1.5-flash-002')

if not HUGGING_FACE_TOKEN: 
    raise ValueError('HUGGING_FACE_TOKEN not defined')

try:
    generator = pipeline('text-generation', model='gpt2', token=HUGGING_FACE_TOKEN)
except Exception as e:
    print(f'Error initializing pipeline: {e}')
    exit(1)

@app.post('/api/chat')
def chat():
    try:
        user_message = request.json.get('message')
        print(user_message)
        if not user_message:
            return jsonify({'error': 'No message sent'}), 400
        bot_response = model.get_response(user_message) 
        
        # generator(user_message, max_length=150, num_return_sequences=1)
        print(bot_response)
        return jsonify({'response': bot_response[0]['generated_text']})
    except Exception as e:
        print(f'chatbot error: {e}')
        return jsonify({'error': 'an error occured'}), 500
    
    
@app.get('/api/chat')
def getChat():
    try:
        user_message  = 'hi there, how are yoU?'
        bot_response = model.get_response(user_message) 
        return jsonify({'response': bot_response})
    except Exception as e: 
        print(f'error: {e}')
        return jsonify({'error': 'error'}), 500


if __name__ == '__main__':
    app.run(debug=True)