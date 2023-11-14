
import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "5942694529:AAHI96YWQC1yFFPHVTMUMjM_XmfOD7Ex2oA"  # <-- Tokeningizni shu yerga yozing
bot = telebot.TeleBot(token=TOKEN)


# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f'Assalom alaykum, {username} Kirill-Lotin botiga xush kelibsiz!'
    xabar += '\nMatningizni yuboring.'
    bot.reply_to(message, xabar)

@bot.message_handler(["info"])
def send_info(message):
    info = "Bu BOT AvazbekCoderPy tomonidan yasalgan ! \n\nKANAL: @AvazbekCoderPy \nINSTAGRAM: https://instagram.com/AvazbekCoderPy"
    bot.reply_to(message, info)

@bot.message_handler(["help"])
def send_help(message):
    help_msg = "QO'LLANMA: \nBu BOT sizga Matnlarni KIRILL alifbosidan LOTIN alifbosiga va LOTIN alifbosidan KIRILL alifbosiga o'girishga yordam beradi."
    bot.reply_to(message, help_msg)

# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    if msg.count("o'") or msg.count("O'") or msg.count("g'") or msg.count("G'"):
        msg2 = msg.maketrans("'", "‘")
        msg = msg.translate(msg2)

    javob = lambda msg: to_cyrillic(msg) if msg.isascii() or msg.count("‘") or msg.count("’") else to_latin(msg)
    bot.reply_to(message, javob(msg))



bot.polling()
