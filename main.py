import telebot

bot = telebot.TeleBot('6651929953:AAFC2JDxspvcfd7shtoegtZZiDBUiGpOFtM')


@bot.message_handler()  # Обозначим что сейчас будем писать боту
def send_text(message):  # Функция принятия текста от пользователя.
    if message.text == 'Игра говно':  # Если ваш текст “привет”
        bot.send_message(message.chat.id, 'Ты говно, а игра дерьмо')  # бот пришлёт вам “Привет друг”

    elif message.text == 'Сука':  # Если ваш текст “ запись ”
        bot.send_message(message.chat.id, 'Чильнись')  # message text скопирует ваше сообщение и перенаправит его вам.

    elif message.text == 'Заебало':  # Если ваш текст “ Пока”
        bot.send_message(message.chat.id, 'Будь счастлив, друг!')

    else:  # Применяется если введенный вариант не соответствует словам: привет, запись, пока.
        bot.send_message(message.chat.id, 'Я тупенький я не понимаю тебя!')


bot.infinity_polling()
