import os
from flask import Flask, request, jsonify
from transformers import pipeline
from dotenv import load_dotenv
from flask_cors import CORS
from ..ai.llms import use_gemini

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.post('/api/chat')
def chat():
    try:
        user_message = request.json.get('message')
        print(user_message)
        if not user_message:
            return jsonify({'error': 'No message sent'}), 400
        bot_response = use_gemini(user_message, 'gemini-2-flash-exp') 
        
        # generator(user_message, max_length=150, num_return_sequences=1)
        print(bot_response)
        return jsonify({'response': bot_response.content})
    except Exception as e:
        print(f'chatbot error: {e}')
        return jsonify({'error': 'an error occured'}), 500
    
    
@app.get('/api/chat')
def getChat():
    try:
        user_message  = 'hi there, how are yoU?'
        bot_response = use_gemini(user_message) 
        return jsonify({'response': bot_response.content})
    except Exception as e: 
        print(f'error: {e}')
        return jsonify({'error': 'error'}), 500


if __name__ == '__main__':
    app.run(debug=True)