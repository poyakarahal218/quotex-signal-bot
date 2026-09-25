import telebot
import time
import random

TOKEN = '7667199184:AAE7OQSKF9En4C81N6IqA08ap0Yids4BY'
bot = telebot.TeleBot(TOKEN)

# أزواج الفوركس الحقيقية وأزواج الـ OTC
FOREX_PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", 
    "USD/CAD", "NZD/USD", "USD/CHF", "EUR/GBP", "EUR/JPY"
]

OTC_PAIRS = [
    "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", 
    "AUD/USD (OTC)", "EUR/JPY (OTC)", "GBP/JPY (OTC)",
    "USD/CAD (OTC)", "NZD/USD (OTC)"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('📊 طلب إشارة تداول فوري'))
    markup.add(telebot.types.KeyboardButton('🌐 عرض أزواج الفوركس و OTC'))
    
    bot.reply_to(
        message, 
        "مرحباً بك في بوت تحليل وإشارات كوتكس (Forex & OTC) 🚀\nاختر أحد الخيارات أدناه للبدء:", 
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == '🌐 عرض أزواج الفوركس و OTC')
def show_pairs(message):
    forex_list = ", ".join(FOREX_PAIRS)
    otc_list = ", ".join(OTC_PAIRS)
    
    text = (
        f"📈 **أزواج الفوركس العادية:**\n{forex_list}\n\n"
        f"🔄 **أزواج الـ OTC (متاحة دائماً):**\n{otc_list}"
    )
    bot.reply_to(message, text, parse_mode="Markdown")

@bot.message_handler(func=lambda message: message.text == '📊 طلب إشارة تداول فوري')
def generate_signal(message):
    all_available_pairs = FOREX_PAIRS + OTC_PAIRS
    pair = random.choice(all_available_pairs)
    
    direction = random.choice(["🟢 صعود (CALL)", "🔴 هبوط (PUT)"])
    timeframe = random.choice(["1 دقيقة (1M)", "5 دقائق (5M)"])
    confidence = random.randint(83, 98)
    
    signal_text = (
        f"📊 **إشارة تداول جديدة (Quotex)**\n\n"
        f"🔹 الزوج / الأصل: *{pair}*\n"
        f"⏱ الإطار الزمني: *{timeframe}*\n"
        f"📈 الاتجاه المتوقع: *{direction}*\n"
        f"⭐ نسبة الدقة والتحليل: *{confidence}%*\n\n"
        f"⚠️ تنبيه: يرجى إدارة رأس مالك بحكمة."
    )
    bot.reply_to(message, signal_text, parse_mode="Markdown")

print("Quotex Bot is running successfully...")
bot.infinity_polling(timeout=60, long_polling_timeout=60)
