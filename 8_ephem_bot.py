"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    # print(text)
    update.message.reply_text(text)


def mars(update, context):
    user_text = update.message.text.split()[-1].lower()
    # print("text ", user_text)

    try:
        planet = getattr(ephem, user_text.capitalize())
        text = f"Сегодня {user_text} в созвездии {ephem.constellation(planet(ephem.now()))[1]}"
        update.message.reply_text(text)
    except:
        text = f"Я не знаю такую планету {user_text.capitalize()}.\nПопробуй ввести другую"
        update.message.reply_text(text)

    # if user_text == "mars":
    #     # data = ephem.Mars(ephem.now())
    #     data = getattr(ephem, "Mars")
    #     text = f"Сегодня в созвездии {ephem.constellation(data(ephem.now()))[1]}"      
    #     update.message.reply_text(text)
    # elif user_text == "jupiter":
    #     # data = ephem.Jupiter(ephem.now())
    #     data = getattr(ephem, "Jupiter")
    #     text = f"Сегодня в созвездии {ephem.constellation(data(ephem.now()))[1]}"
    #     update.message.reply_text(text)
    # else:
    #     text = "У меня нет данных о данной планете. Попробуй mars или Jupiter"
    #     update.message.reply_text(text)
    


def talk_to_me(update, context):
    user_text = update.message.text
    # print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater("1401318062:AAEeLSUKv2v3I4qnDb5RxCgfajSpM8BW_KA", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", mars))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
