import random, re, math
from PIL import Image, ImageFilter, ImageOps


class Pixel(object):
    def __init__(self, pixel, x, y):
        self.pixel = pixel
        self.x = x
        self.y = y


class ImageTool(object):

    @staticmethod
    def pixeling(image, koef_transform_x, koef_transform_y):  # [0-1]
        koef_transform_x = float(koef_transform_x)
        koef_transform_y = float(koef_transform_y)
        img = image.convert('RGB')  # convert to jpg
        img_small = img.resize((int(img.size[0] / koef_transform_x), int(img.size[1] / koef_transform_y)),
                               Image.BILINEAR)
        return img_small.resize(img.size, Image.NEAREST)

    @staticmethod
    def mixing_pixels(img, mix_percent):  # [0-1]
        index1, index2, list_pixel = 0, 0, []
        mix_percent = float(mix_percent)
        if mix_percent > 1:
            mix_percent = 1
        if mix_percent < 0:
            mix_percent = 0
        img = img.convert('RGB')  # convert to jpg
        pixels = img.load()
        for y in range(0, img.size[1]):
            for x in range(0, img.size[0]):
                list_pixel.append(Pixel(pixels[x, y], x, y))
        counter = 0
        while counter / float(img.size[0] * img.size[1]) < mix_percent:
            while index1 == index2:
                index1 = random.randint(0, len(list_pixel) - 1)
                index2 = random.randint(0, len(list_pixel) - 1)
            r1, g1, b1 = list_pixel[index1].pixel[0], list_pixel[index1].pixel[1], list_pixel[index1].pixel[2]
            r2, g2, b2 = list_pixel[index2].pixel[0], list_pixel[index2].pixel[1], list_pixel[index2].pixel[2]
            pixels[list_pixel[index1].x, list_pixel[index1].y] = (r2, g2, b2)  # Set colour
            pixels[list_pixel[index2].x, list_pixel[index2].y] = (r1, g1, b1)  # Set colour
            counter += 2
            if index1 < index2:
                index2, index1 = index1, index2
            list_pixel.pop(index1)
            list_pixel.pop(index2)
            index1 = index2 = 0
        return img

    @staticmethod
    def set_pixels_by_function(img, str_func):
        # string = "R:r;\nG:g+random.randint(-10,10);\nB:b+random.randint(0,150);A:a-0.1);"
        if len(re.findall("^[R|G|B|A]:", str_func)) != 0:
            str_func = re.sub(r"[R|G|B|A]:", "", str_func)
            list_rgb = str_func.split(";")
            img = img.convert('RGBA')  # convert to jpg
            pixels = img.load()
            for y in range(img.size[1]):  # y
                for x in range(img.size[0]):  # x
                    r, g, b, a = pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], pixels[x, y][3]
                    pixels[x, y] = (int(eval(list_rgb[0], {
                        '__builtins__': {'r': r, 'g': g, 'b': b, 'a': a, 'math': math, 'random': random}})), int(
                        eval(list_rgb[1],
                             {'__builtins__': {'r': r, 'g': g, 'b': b, 'a': a, 'math': math, 'random': random}})), int(
                        eval(list_rgb[2],
                             {'__builtins__': {'r': r, 'g': g, 'b': b, 'a': a, 'math': math, 'random': random}})), int(
                        eval(list_rgb[3], {'__builtins__': {'r': r, 'g': g, 'b': b, 'a': a, 'math': math,
                                                            'random': random}})))  # Set colour
        else:
            print("Invalid data")
        return img

    @staticmethod
    def blur(img, radius):
        return img.filter(ImageFilter.GaussianBlur(float(radius)))

    @staticmethod
    def unsharp_mask(img, radius, percent, threshold):
        return img.filter(ImageFilter.UnsharpMask(int(radius), int(percent), int(threshold)))

    @staticmethod
    def rank_filter(img, size, rank):
        return img.filter(ImageFilter.RankFilter(size, int(rank)))

    @staticmethod
    def rotate(img, degree):
        return img.rotate(float(degree))

    @staticmethod
    def mirror(img):
        return ImageOps.mirror(img)

    @staticmethod
    def solarize(img, threshold):
        return ImageOps.solarize(img, int(threshold))

    @staticmethod
    def invert(img):
        return ImageOps.invert(img)

    @staticmethod
    def gradient_composite(img, img2):
        img = img.convert('RGBA')
        img2 = img2.convert('RGBA')
        mask = Image.open('example_photo/gradation_h.jpg').convert('L').resize(img.size)
        return Image.composite(img, img2, mask)

    @staticmethod
    def composite(img, img2):
        img = img.convert('RGBA')
        img2 = img2.convert('RGBA')
        mask = Image.new("L", img.size, 128)
        return Image.composite(img, img2, mask)


'''
R:r-50;
G:g-50;
B:b-50;
A:a-0.2

hello - information about the bot
help - please,read this
start - start working bot
commands - print commands list
pixeling - add pixel effect to photo
mixing_pixels - random mix pixel from your photo
filter - set every pixel by function
blur - add blur effect to photo
unsharp_mask - increase subjective image clarity
rank_filter - add point effect
rotate - rotate photo on x degree
mirror - create mirror copy your image
solarize - invert some pixels
invert - invert color pixels
composite - overlay 2 pictures
gradient_composite - composite with gradient
sec_img - you can load second image for some commands
math - math operation and functions

'''


