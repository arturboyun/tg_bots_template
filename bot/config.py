from configparser import ConfigParser
from urllib.parse import urljoin

config = ConfigParser()
config.read('config.ini')


# Default
BOT_TOKEN = config.get('default', 'bot_token', fallback=None)
SKIP_UPDATES = config.getboolean('default', 'skip_updates', fallback=True)
OWNER_ID = config.getint('default', 'owner_id', fallback=None)


# Database
DB_NAME = config.get('database', 'db_name', fallback=None)
DB_HOST = config.get('database', 'db_host', fallback='localhost')
DB_PORT = config.get('database', 'db_port', fallback='5432')
DB_USER = config.get('database', 'db_user', fallback='postgres')
DB_PASS = config.get('database', 'db_pass', fallback='102938Ruin')


# Webhook
USE_WEBHOOK = config.getboolean('webhook', 'use_webhook', fallback=False)

WEBHOOK_HOST = config.get('webhook', 'webhook_host', fallback='localhost')
WEBHOOK_PATH = config.get('webhook', 'webhook_path', fallback='/')
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'


# Webserver
WEBAPP_HOST = config.get('webserver', 'webapp_host', fallback='localhost')
WEBAPP_PORT = config.get('webserver', 'webapp_port', fallback='3001')

# TODO: re-check
