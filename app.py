import telebot
from config import TOKEN, START_HELP_MESSAGE, VALUES_MESSAGE, HELP_MESSAGE
from extensions import convert

# Initialize the bot with the provided TOKEN
bot = telebot.TeleBot(TOKEN)


# Handler for /start and /help commands
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Sends a welcome message with instructions when /start is called.
    bot.reply_to(message, START_HELP_MESSAGE)


# Handler for /help commands
@bot.message_handler(commands=['help'])
def send_welcome(message):
    # Sends a welcome message with instructions when /help is called.
    bot.reply_to(message, HELP_MESSAGE)


# Handler for /values command
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    # Sends a message with the list of available currencies when /values is called.
    bot.reply_to(message, VALUES_MESSAGE)


# Handler for all text messages
@bot.message_handler(content_types=['text'])
def handle_text_messages(message: telebot.types.Message):
    # Processes any text message received.
    convert(bot, message)


# Start polling for messages
bot.polling()
