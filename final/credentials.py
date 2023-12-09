import os

# Fetch credentials from environment variables eventually
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
