from dotenv import load_dotenv
import telegram
import os


load_dotenv()
telegram_token = os.getenv('TELEGRAM_TOKEN')
chat_id = os.getenv('CHAT_ID')
bot = telegram.Bot(token=telegram_token)
#bot.send_message(chat_id=chat_id, text="Это пробное сообщение")
bot.send_document(chat_id=chat_id, document=open('images/nasa_apod5.jpg', 'rb'))


