import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = int(os.getenv("USER_ID", "0"))

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.id == USER_ID:
        bot.send_message(message.chat.id, "✅ Бот активний та чекає на сигнали!")

@bot.message_handler(commands=["тест"])
def test_signal(message):
    if message.from_user.id == USER_ID:
        with open("ada_bos_example.png", "rb") as photo:
            bot.send_photo(message.chat.id, photo, caption="🔔 Тестовий сигнал: ADA злам структури!")

bot.polling()
