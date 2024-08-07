import requests
import os
from dotenv import load_dotenv

load_dotenv()

# https://api.telegram.org/bot{token}/getUpdates
bot_token = os.getenv('TOKEN_BOT_TELEGRAM')
id_canal = '-1002233473125'

api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

def enviar_mensagem_telegram(mensagem):
    resposta = requests.post(
        api_url,
        json={
            "chat_id": id_canal,
            "text": mensagem
        }
)