import telebot, emoji, re, os, random
from PIL import Image
from Image import ImageTool

bot = telebot.TeleBot("1002702968:AAFwE3-tvk8Cnv_6usaWZAAwAKwaNrsx4BE")

parameter = 0
img, img2 = Image, Image
fl_second_img = False


@bot.message_handler(commands=['sec_img'])
def sec_img_command(message):
    bot.send_message(message.chat.id, "Ok,send me your second photo")
    global fl_second_img
    fl_second_img = True


@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.send_message(message.chat.id, "Hello " + message.from_user.first_name
                     + emoji.emojize(' :blush:', use_aliases=True) +
                     ",I picture456bot\n" + "I can make your photo even better" +
                     emoji.emojize(":relieved:", use_aliases=True))


@bot.message_handler(commands=['math'])
def math_command(message):
    bot.send_message(message.chat.id, "You can use this math command for filter:\n"
                                      "sin - math.sin(x)\n"
                                      "cos - math.cos(x)\n"
                                      "tg - math.tan(x)\n"
                                      "log - math.log(x,base)\n"
                                      "e³ - math.exp(3)\n"
                                      "a² - a**b or math.pow(a,2)\n"
                                      "a! - math.factorial(a)")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Examples:\n"
                                      "1.pixeling - 4 6 (more 0)\n"
                                      "2.mixing_pixels - 0.75 (between 0 and 1)\n"
                                      "3.filter - please,use next format\nR:r-50;\nG:g/4;\nB:2*(b-r);\nA:a-0.2\n"
                                      "R-red(0≤r≤255),G-green(0≤g≤255),B-blue(0≤b≤255),A-transparency(0≤a≤1)\n/math")


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Send me photo(as a photo, not a file!)")


@bot.message_handler(commands=['commands'])
def commands_command(message):
    string = "/hello - information about the bot\n" \
             "/help - please,read this\n" \
             "/start - start working bot\n" \
             "/commands - print commands list\n" \
             "/pixeling - add pixel effect to photo\n" \
             "/mixing_pixels - random mix pixel from your photo\n" \
             "/filter - set every pixel by function\n" \
             "/blur - add blur effect to photo\n" \
             "/unsharp_mask - increase subjective image clarity\n" \
             "/rank_filter - add point effect\n" \
             "/rotate - rotate photo on x degree\n" \
             "/mirror - create mirror copy your image\n" \
             "/solarize - invert selected pixels\n" \
             "/invert - invert color pixels\n" \
             "/composite - overlay 2 pictures\n" \
             "/gradient_composite - composite with gradient\n" \
             "/sec_img - you can load second image for some commands\n" \
             "/math - math operation and functions"
    bot.send_message(message.chat.id, string)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Send me photo(as a photo, not a file!)")


@bot.message_handler(commands=['pixeling'])
def pixeling_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        koef = re.split(r'\W| ', str(parameter))
        new_img = ImageTool.pixeling(img, koef[0], koef[1])
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['mixing_pixels'])
def mixing_pixels_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.mixing_pixels(img, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['filter'])
def filter_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.set_pixels_by_function(img, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['blur'])
def blur_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.blur(img, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['unsharp_mask'])
def unsharp_mask_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        list_param = re.split("\W| ", str(parameter))
        new_img = ImageTool.unsharp_mask(img, list_param[0], list_param[1], list_param[2])
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['rank_filter'])
def rank_filter_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.rank_filter(img, 9, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['rotate'])
def rotate_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.rotate(img, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['mirror'])
def mirror_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.mirror(img)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['solarize'])
def solarize_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.solarize(img, parameter)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['invert'])
def invert_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.invert(img)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['composite'])
def composite_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.composite(img, img2)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(commands=['gradient_composite'])
def gradient_composite_command(message):
    try:
        bot.send_message(message.chat.id, "please,wait...")
        new_img = ImageTool.gradient_composite(img, img2)
        processing_result(message, new_img)
    except:
        bot.send_message(message.chat.id, "Incorrect data :(")


@bot.message_handler(content_types=['text'])
def get_messege(message):
    global parameter
    parameter = message.text


@bot.message_handler(content_types=['document'])
def warning(message):
    bot.send_message(message.chat.id, "Send me photo(as a photo, not a file!)")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global img, img2, fl_second_img
    try:

        raw = message.photo[2].file_id
        name = "download_photo/" + raw + ".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        new_file = open(name, 'wb')
        new_file.write(downloaded_file)
        new_file.close()
        if fl_second_img:
            img2 = Image.open(name)
            fl_second_img = False
        else:
            img = Image.open(name)
    except Exception as e:
        bot.reply_to(message, e)

    bot.send_message(message.chat.id, "Ok,write parameter(s) and select a command /help")


def processing_result(msg, pic):
    filename = 'result' + str(random.randint(0, 1000000)) + '.png'
    pic.save(filename)
    bot.send_photo(msg.chat.id, open(filename, 'rb'))
    os.remove(filename)


bot.polling(none_stop=True)
