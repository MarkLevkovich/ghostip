from telebot import TeleBot
from telebot.types import Message
from ipcode import get_info_by_ip

TOKEN = '8112149382:AAEVQMyPkkgHEom9196SwRAd1BdR9wzxVgg'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message:Message):
    bot.send_message(message.chat.id, f"Hi, {message.from_user.username} 👋\n ╰┈➤I will help you find out a lot of things with just one IP address 👀\n ╰┈➤But remember, you can't use this without asking permission from the owner of this IP 📛\n‼️ The author is not responsible for your actions ‼️")


@bot.message_handler(commands=['ip'])
def handle_ip_command(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "ℹ️ Using: <code>/ip 8.8.8.8</code>", parse_mode='HTML')
        return

    ip = args[1]
    bot.send_chat_action(message.chat.id, 'typing')
    info = get_info_by_ip(ip)
    bot.reply_to(message, info, parse_mode='HTML', disable_web_page_preview=True)






bot.polling(non_stop=True)