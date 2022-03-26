import telegram.ext
import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")

def start_command(update, context):
    update.massage.reply_text('Type something random to get starteted')

def help_command(update, context):
    update.massage.reply_text('Google')

def handle_massage(update, context):
    text: str = str(update.massage.text).lower()
    response = R.sample_responses(text)

    update.massage.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_massage))

    dispatcher.add_error_handler(error)

    updater.start_polling(1)
    updater.idle()

main()

