import logging
import random
import re
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
load_dotenv()
TOKEN = os.environ.get('TOKEN')

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


jokes = [
    ("Have you heard of Sugon?", "Sugon deez nuts"),
    ("Do you have ligma?", "Ligma balls"),
    ("Have you heard the new Imagine Dragons song?", "Imagine dragging deez nuts across your face"),
    ("Have you seen Candice?", "Can deez nuts fit in your mouth"),
    ("What is 19 in french?", "Dix-neuf"),
    ("Excuse me do you like Wendy's?", "Because you're gonna like it when deez nuts meet your face"),
    ("Do you like pudding?", "Why don't you put deez nuts in your mouth"),
    ("Roses are red, Violets are Blue", "Can I quarantine deez nuts inside of you"),
    ("Do you enjoy parodies?", "Why don't you enjoy a pair of deez nuts"),
    ("Have you seen Landon?", "Yeah slip fall and land on deez nuts"),
    ("Are you into fitness?", "Why don't you fit deez nuts in your mouth"),
    ("Have you heard about the beekeeping IG?", "Be keeping deez nuts in your mouth"),
    ("Do you know what happened in Kenya today?", "Kenya fit deez nuts in your mouth"),
    ("Wanna come to the West Indies?", "In deez nuts lol")
]


length = len(jokes) - 1

def deeznuts(update, context):
    """Sends a deez nuts joke"""
    context.bot.delete_message(
        chat_id=update.effective_chat.id,
        message_id=update.message.message_id
    )
    a = random.randint(0, length)
    for i in range(0, 2):
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=jokes[a][i]
        )

def msgPreprocessor(msg):
    result = msg.lower()
    specialChars = "[^A-Za-z0-9]+"
    result = re.sub(specialChars, "", result)
    return result

def reply(update, context):
    msg = msgPreprocessor(update.message.text)
    if "quason" in msg:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="(quason)"
        )


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("deeznuts", deeznuts))
    # dp.add_handler(MessageHandler(Filters.text and (~Filters.command), reply))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://javier-ong-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()