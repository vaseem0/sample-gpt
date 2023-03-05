import openai
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import os

updater = Updater("1998286989:AAEzYv8hGxoSxJ7cCgn1GPNPwdS9ZKcum30", use_context=True)

def start(update, context):
    update.message.reply_text("paste api key")

def chat(update, context):
    context.user_data['api']=update.message.text
    openai.api_key = context.user_data['api']
    response = openai.Completion.create(
            model="text-curie-001",
            prompt= "what is 1+1",
            temperature=0.1,
            max_tokens=3,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0,
            #stop=["\n"]
        )
    r = response["choices"][0]["text"]
    final_response=r[1:]
    update.message.reply_text(final_response)
    print(msg)
def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, error)
def main():
    """Start the bot."""
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, chat))

    # log all errors
    dp.add_error_handler(error)
    
    updater.start_polling()
    
    updater.idle()

if __name__ == '__main__':
    main()
    
