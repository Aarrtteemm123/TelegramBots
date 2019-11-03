import pyowm, telebot, re, emoji

bot = telebot.TeleBot("950431741:AAE2_y35enqibtRHIydrauOZ3vpC_C-jBGs")

owm = pyowm.OWM('a88284f4fcb44b8bbff21119bcc8ac4a', language="ru")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, emoji.emojize('Hello:blush:', use_aliases=True) +
                     ",I weather456bot\n"+"I know weather in any city." +
                     "\nWrite name city (or) country\n"+"Example: Kyiv,Ukraine\n/help")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "/start")
    bot.send_message(message.chat.id, "/examples")


@bot.message_handler(commands=['examples'])
def send_example(message):
    bot.send_message(message.chat.id, "Format: Kyiv,Ukraine\nKyiv\nUkraine\n"
                                      "Kyiv,Ukr\nKyiv,UKR\n50.45, 30.48")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    try:
        if len(re.findall("^[0-9]|-[0-9]", message.text)) != 0:
            coord = re.split(",", message.text)
            weather = (owm.weather_at_coords(float(coord[0]), float(coord[1]))).get_weather()
        else:
            weather = (owm.weather_at_place(message.text)).get_weather()

        msg = "Temp: " + str(weather.get_temperature('celsius')['temp']) + "°C"\
              +"\n" + "Wind: " + str(weather.get_wind()['speed']) + " m/s" + \
              "\nHumidity: " + str(weather.get_humidity()) + "%" + \
              "\nStatus: " + str(weather.get_status())
        bot.send_message(message.chat.id, msg)
    except:
        bot.send_message(message.chat.id,emoji.emojize("Sorry:pensive:", use_aliases=True)
                         + ",I don't know this place")


bot.polling(none_stop=True)
