import telebot, emoji, re, os, random
from PIL import Image
from Image import ImageTool
from User import User

bot = telebot.TeleBot("1002702968:AAFwE3-tvk8Cnv_6usaWZAAwAKwaNrsx4BE")

user_list = {}


@bot.message_handler(commands=['sec_img'])
def sec_img_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/sec-img.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            bot.send_message(message.chat.id, "Ok,send me your second photo")
            user_list[message.chat.id].fl_second_img = True
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['hello'])
def send_hello(message):
    if user_list.__contains__(message.chat.id):
        bot.send_message(message.chat.id, "Hello " + message.from_user.first_name
                         + emoji.emojize(' :blush:', use_aliases=True) +
                         ",I picture456bot\n" + "I can make your photo even better" +
                         emoji.emojize(":relieved:", use_aliases=True))
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['math'])
def math_command(message):
    if user_list.__contains__(message.chat.id):
        bot.send_message(message.chat.id, "You can use this math command for filter:\n"
                                          "sin - math.sin(x)\n"
                                          "cos - math.cos(x)\n"
                                          "tg - math.tan(x)\n"
                                          "log - math.log(x,base)\n"
                                          "e³ - math.exp(3)\n"
                                          "a² - a**b or math.pow(a,2)\n"
                                          "a! - math.factorial(a)\n"
                                          "Format:\n"
                                          "R:r+50;\n"
                                          "G:g*0.2;\n"
                                          "B:b-20;\n"
                                          "A:a-0.2")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['help'])
def help_command(message):
    if user_list.__contains__(message.chat.id):
        user_list[message.chat.id].help = True
        bot.send_message(message.chat.id, "Select command")
        string = "/pixeling - add pixel effect to photo\n" \
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
                 "/sec_img - you can load second image for some commands"
        bot.send_message(message.chat.id, string)
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['start'])
def start_command(message):
    user_list[message.chat.id] = User()
    bot.send_message(message.chat.id, "Send me photo(as a photo, not a file!)")
    bot.send_message(244084290, "New user!(" + str(len(user_list)) + ")\nIt's "
                     + message.from_user.first_name +
                     " " + message.from_user.last_name)


@bot.message_handler(commands=['commands'])
def commands_command(message):
    if user_list.__contains__(message.chat.id):
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
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['pixeling'])
def pixeling_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/pixeling.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                koef = re.split(r'\W| ', str(user_list[message.chat.id].parameter))
                new_img = ImageTool.pixeling(Image.open(user_list[message.chat.id].filename), koef[0], koef[1])
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['mixing_pixels'])
def mixing_pixels_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/mixing-pixels.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.mixing_pixels(img, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['filter'])
def filter_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/filter.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.set_pixels_by_function(img, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['blur'])
def blur_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/blur.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.blur(img, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['unsharp_mask'])
def unsharp_mask_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/mask.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                list_param = re.split("\W| ", str(parameter))
                new_img = ImageTool.unsharp_mask(img, list_param[0], list_param[1], list_param[2])
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['rank_filter'])
def rank_filter_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/rank-filter.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.rank_filter(img, 9, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['rotate'])
def rotate_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/rotate.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.rotate(img, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['mirror'])
def mirror_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/mirror.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                new_img = ImageTool.mirror(img)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "please,upload image")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['solarize'])
def solarize_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/solorize.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                parameter = user_list[message.chat.id].parameter
                new_img = ImageTool.solarize(img, parameter)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "Incorrect data or image not uploaded :(")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['invert'])
def invert_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/invert.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                bot.send_message(message.chat.id, "please,wait...")
                img = Image.open(user_list[message.chat.id].filename)
                new_img = ImageTool.invert(img)
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "please,upload image")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['composite'])
def composite_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/composite.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                img = Image.open(user_list[message.chat.id].filename)
                img2 = Image.open(user_list[message.chat.id].filename2)
                new_img = ImageTool.composite(img, img2)
                bot.send_message(message.chat.id, "please,wait...")
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "please,upload second image /sec_img")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(commands=['gradient_composite'])
def gradient_composite_command(message):
    if user_list.__contains__(message.chat.id):
        if user_list[message.chat.id].help:
            bot.send_photo(message.chat.id, open("example_photo/gradient-composite.png", 'rb'))
            user_list[message.chat.id].help = False
        else:
            try:
                img = Image.open(user_list[message.chat.id].filename)
                img2 = Image.open(user_list[message.chat.id].filename2)
                new_img = ImageTool.gradient_composite(img, img2)
                bot.send_message(message.chat.id, "please,wait...")
                processing_result(message, new_img)
            except:
                bot.send_message(message.chat.id, "please,upload second image /sec_img")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(content_types=['text'])
def get_messege(message):
    if user_list.__contains__(message.chat.id):
        user_list[message.chat.id].parameter = message.text
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(content_types=['document'])
def warning(message):
    if user_list.__contains__(message.chat.id):
        bot.send_message(message.chat.id, "Send me photo(as a photo, not a file!)")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    if user_list.__contains__(message.chat.id):
        try:

            raw = message.photo[2].file_id
            name = "download_photo/" + raw + ".jpg"
            file_info = bot.get_file(raw)
            downloaded_file = bot.download_file(file_info.file_path)
            new_file = open(name, 'wb')
            new_file.write(downloaded_file)
            new_file.close()
            if user_list[message.chat.id].fl_second_img:
                user_list[message.chat.id].filename2 = name
                user_list[message.chat.id].fl_second_img = False
            else:
                user_list[message.chat.id].filename = name
        except:
            bot.reply_to(message, "image upload failed :(")
        bot.send_message(message.chat.id, "Ok,write parameter(s) and select a command /help")
    else:
        bot.send_message(message.chat.id, "Click on this command /start")


def processing_result(msg, pic):
    filename = 'result' + str(random.randint(0, 1000000)) + '.png'
    pic.save(filename)
    bot.send_photo(msg.chat.id, open(filename, 'rb'))
    os.remove(filename)


bot.polling(none_stop=True)
