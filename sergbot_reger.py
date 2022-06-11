import telebot
from telebot import types

# serg
# serg1542bot

bot = telebot.TeleBot('5135207222:AAFzxEu_RTzzZasguJvMdpF__742pMM1Dcw')

# !!!Бот регистратор!!!
name = age = surname = ''

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Я - бот. Напиши привет, чтобы познакомиться.')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == '':
        bot.send_message(message.chat.id, 'Бот-регистратор приветствует тебя!!!\n Ты кто?, давай знакомиться')
        keyboard = types.InlineKeyboardMarkup()
        key_films = types.InlineKeyboardButton(text='Какашка', callback_data='kaks')
        key_cars = types.InlineKeyboardButton(text='Норм чел', callback_data='chel')
        keyboard.add(key_films, key_cars)
        bot.send_message(message.chat.id, text='Выбери кто ты по жизни', reply_markup=keyboard)

    if message.text == '/reg':
        bot.send_message(message.chat.id, 'Хай, имя твое какое?')
        bot.register_next_step_handler(message, reg_name)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.chat.id, 'А фамилию свою напиши!')
    bot.register_next_step_handler(message, reg_surname)


def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.chat.id, 'Сколько тебе лет? Можешь соврать))))')
    bot.register_next_step_handler(message, reg_age)


def reg_age(message):
    global age
    age = message.text
    if 1 <= int(age) <= 25:
        bot.send_message(message.chat.id, 'Молодежь подвалила!')
    elif 25 < int(age) <= 45:
        bot.send_message(message.chat.id, 'Что, нечем заняться?')
    else:
        bot.send_message(message.chat.id, 'А что тут делают пенсы? )))')

    bot.send_message(message.chat.id, f'Тебя зовут {name} {surname}. Тебе {age} лет')
    bot.send_message(message.chat.id, 'Все, ты теперь у меня под колпаком. Ха-ха-ха!!!')

    with open('users.txt', encoding='utf-8', mode='a') as file:
        s = name + ' ' + surname + ' ' + age + '\n'
        file.write(s)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'kaks':
        bot.send_message(call.message.chat.id, 'Ну жесть конечно... Не надо знакомиться со мной!')
    if call.data == 'chel':
        bot.send_message(call.message.chat.id, 'Ну тогда точно давай знакомиться!, нажми /reg')


bot.polling(none_stop=True, interval=0)
