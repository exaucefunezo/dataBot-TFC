import os
from dotenv import load_dotenv
import json

class Config:
    def __init__(self):
        load_dotenv()
        
        self.mistral_api_key = os.getenv("MISTRAL_API_KEY")
        self.model = os.getenv("MODEL", "mistral-small-latest")
        self.temperature = float(os.getenv("TEMPERATURE", "0.1"))
        
        # Chargement configuration
        with open('config/settings.json', 'r') as f:
            self.settings = json.load(f)
    
    def get_database_config(self):
        return {
            'host': os.getenv('DB_HOST', 'localhost'),
            'database': os.getenv('DB_NAME', 'sales_data'),
            'user': os.getenv('DB_USER', 'admin')
        }