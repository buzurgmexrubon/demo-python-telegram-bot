import telebot

from transliterate import to_latin, to_cyrillic

TOKEN = "7311647904:AAGEfT97ucv_Xh_9AvdNKWctSEZmcG7Q3zY"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


# MODES
# - Auto
# - Latin
# - Cirill

# text = input("Please enter words: ")
#
# if text.isascii():
#     print(to_cyrillic(text))
# else:
#     print(to_latin(text))


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Hi there, I am latin to cyrillic bot.
I am here to convert latin to cyrillic and cyrillic to latin to you.\
""",
    )


@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Hi there, I am latin to cyrillic bot.
THIS IS HELP SECITON\
""",
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    result = get_result(message.text)
    bot.reply_to(message, result)


def get_result(message: str) -> str:
    # result = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    if message.isascii():
        result = to_cyrillic(message)
    else:
        result = to_latin(message)
    return result


bot.polling()
