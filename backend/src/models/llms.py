from typing import Literal
from langchain_core.messages.ai import AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

GeminiModelName = Literal[
    'gemini-1.5-flash',
    'gemini-1.5-pro',
    'gemini-1.5-flash-8B', 
    'gemini-2.0-flash-exp', 
]

load_dotenv()

def use_gemini(prompt: str, model_name: GeminiModelName='gemini-1.5-flash') -> AIMessage:
    model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')
    response = model.invoke(prompt)
    return response

