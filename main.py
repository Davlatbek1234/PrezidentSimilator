import telebot

bot = telebot.TeleBot("BU_YERGA_TOKENINGIZNI_QO'YING")

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id,
        "👑 Xush kelibsiz, Prezident Bek!\n\n"
        "Qaysi yo‘lni tanlaysiz?\n"
        "1️⃣ So‘mni BTC bilan qutqarish\n"
        "2️⃣ Korrupsiyani yo‘qotish\n"
        "3️⃣ Xalq dardini tinglash\n\n"
        "Tanlovingizni 1, 2 yoki 3 deb yozing.")

@bot.message_handler(func=lambda m: m.text in ['1', '2', '3'])
def handle_choice(message):
    if message.text == '1':
        bot.send_message(message.chat.id, "BTC yo‘li tanlandi!")
    elif message.text == '2':
        bot.send_message(message.chat.id, "Korrupsiyaga zarba!")
    elif message.text == '3':
        bot.send_message(message.chat.id, "Xalq dardini tinglash boshlandi!")

bot.polling()
