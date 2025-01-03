from typing import Literal
import vertexai 
import os
from vertexai.generative_models import GenerativeModel

ModelName = Literal[
    'gemini-1.5-flash-002',
]

class GeminiWrapper:
    
    __id = 'GOOGLE_PROJECT_ID'
    __model:GenerativeModel
    
    def __init__(self, model_name:ModelName):
        PROJECT_ID = os.getenv(self.__id)
        if not PROJECT_ID: 
            raise Exception('No Google Project ID in env. Add with key:  ')
        vertexai.init(PROJECT_ID)
        self.__model = GenerativeModel(model_name)
    
    def get_response(self, input_text, **kwargs):
        """
        Args:
            * generation_config,
            * safety_settings
            * tools
            * tool_config
            * labels
            * streams
        """
        return self.__model.generate_content(kwargs, contents=input_text).text
