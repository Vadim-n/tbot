import config
import telebot
import datetime
import random as r
import math

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if not config.game:
        if message.text.lower() == 'игра':
            bot.send_message(message.chat.id, 'Попробуйте уградать число от 1 до 5')
            config.game = True
            return
        if message.text.lower() == 'дата':
            bot.send_message(message.chat.id, datetime.datetime.now().strftime('%d.%m.%Y'))
            return
        if message.text.lower() == 'время':
            bot.send_message(message.chat.id, datetime.datetime.now().strftime('%H:%M'))
            return
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет, '+message.from_user.first_name+'!')
            return
        bot.send_message(message.chat.id, 'Извините, я вас не понимаю')
    else:
        try:
            guess = int(message.text)
            answer = math.ceil(r.random()*5)
            if guess == answer:
                bot.send_message(message.chat.id, 'Поздравляю, вы угадали!')
            else:
                bot.send_message(message.chat.id, 'К сожалению, вы не угадали. Было загадано число {0}'.format(answer))
        except ValueError:
            if message.text.lower() == 'стоп':
                config.game = False
                bot.send_message(message.chat.id, 'Вы вышли из режима игры')
                return
            else:
                bot.send_message(message.chat.id, 'Введите число!')
            
if __name__ == '__main__':
    bot.polling(none_stop=True)
