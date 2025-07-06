import telebot
from telebot import types

BOT_TOKEN = "8119624986:AAGg5qMCFPMICyxWzK7x3tH1s_1SwP1PMJs"

bot = telebot.TeleBot(BOT_TOKEN)

channels = [
    ("Channel 1 🚀", "https://t.me/alonebiohere"),
    ("Channel 2 🚀", "https://t.me/+u69wKBtxFXlmZDc9"),
    ("Channel 3 🚀", "https://t.me/ghostpaymentproofs"),
    # Add more channels if you want
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id

    image_url = "https://ibb.co/67Q3YKQH"  # ← put your uploaded banner URL here
    bot.send_photo(chat_id, image_url, caption="✨ JOIN ALL CHANNELS FOR TG STAR 🚀")

    markup = types.InlineKeyboardMarkup()
    for name, link in channels:
        btn = types.InlineKeyboardButton(name, url=link)
        markup.add(btn)

    done_btn = types.InlineKeyboardButton("✅ I HAVE JOINED", callback_data="joined")
    markup.add(done_btn)

    bot.send_message(chat_id, "Join all channels to unlock exclusive content!", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "joined":
        bot.answer_callback_query(call.id, "Thank you for joining!")
        bot.send_message(call.message.chat.id, "✅ Verified! You can now access VIP content.")

bot.infinity_polling()
