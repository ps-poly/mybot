import logging, ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')

def get_constellation(update, context):
    print('Вызван /planet')
    user_planet = update.message.text.lower().capitalize().split()[1]
    check_planet = ephem.user_planet('2021/02/27')
    constellation = ephem.constellation(check_planet)
    update.message.reply_text(constellation)

def talk_to_me(update, context):
    user_text = update.message.text
    update.message.reply_text(user_text)


def main():
    mybot = Updater("1642966586:AAHdEZv5sRtM5_NQGFMBOOZnWSj3O9XiktU", use_context=True)


    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()

