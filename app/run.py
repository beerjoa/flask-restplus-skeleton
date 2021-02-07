import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".flaskenv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from src import create_app

config_name = os.getenv('FLASK_CONFIG') or 'dev'
app = create_app(config_name)

if __name__ == '__main__':
    app.run(use_reloader=True, host="0.0.0.0", port=8080)
