from telebot import types
import telebot

token = '6337523792:AAHSQtYvkSadkJrrScTtX35pGlxZezZbEo0'
my_chat_id = 1277442751
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton(text='Услуги')
    button2 = types.KeyboardButton(text='О нас')
    button3 = types.KeyboardButton(text='Оставить заявку')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Приветствуем! Мы - бухгалтерская компания! Добро пожаловать!', reply_markup=keyboard)


def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти в магазин", url="http://deepletter.com")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Добро пожаловать! Чтобы перейти в наш магазин, нажмите на кнопку ниже", reply_markup=keyboard)


def send_request(message):
    mes = f'Новая заявка: {message.text}'
    bot.send_message(my_chat_id, mes)
    bot.send_message(message.chat.id, 'Спасибо за заявку, наши специалисты скоро с Вами свяжутся!')


def send_service(message):
    bot.send_message(message.chat.id, '1. Составить годовой отчет')
    bot.send_message(message.chat.id, '2. Оплатить налоги за ТОО')
    bot.send_message(message.chat.id, '3. Рассчитать бюджет')


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    if message.text.lower() == 'о нас':
        info_func(message)
    if message.text.lower() == 'оставить заявку':
        bot.send_message(message.chat.id, 'Будем рады вам помочь, оставьте свои контактные данные')
        bot.register_next_step_handler(message, send_request)
    if message.text.lower() == 'услуги':
        send_service(message)


if __name__ == '__main__':
    bot.infinity_polling()