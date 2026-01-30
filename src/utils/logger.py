import logging
from datetime import datetime

class DataBotLogger:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f'logs/databot_{datetime.now().strftime("%Y%m%d")}.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("DataBot")
    
    def log_query(self, user, question, response):
        self.logger.info(f"User: {user} | Q: {question} | R: {response[:100]}...")