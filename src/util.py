from PIL import Image, ImageFont, ImageDraw
import math

from img_util import *
from main import CHARACTERS

def bounding_box(font: ImageFont, s: str): # Returns a tuple of (width, height):
    (left, top, right, bottom) = font.getbbox(CHARACTERS)
    height = bottom + top

    (left, top, right, bottom) = font.getbbox(s)
    width = right - left

    return (width, height)

def char_to_img(font: ImageFont, c: str, invert = False): # Returns an Image
    (w, h) = bounding_box(font, c)

    textColor = (255, 255, 255)
    background = (0, 0, 0)
    if invert:
        textColor = (0, 0, 0)
        background = (255, 255, 255)

    # Create an image that's the same size as the chracter
    img = Image.new("RGB", (w, h), background)

    d = ImageDraw.Draw(img)

    d.text((0, 0), c, font=font, fill=textColor)

    return img

def font_proportions(font: ImageFont):
    '''
    Returns the height/width ratio of characters in the specified font.
    If the font is not monospace (i.e. the width/height of each
    character is different), then `None` is returned
    '''

    boundingBox = bounding_box(font, "a")
    # for c in CHARACTERS:
    #     if bounding_box(font, c) != boundingBox:
    #         return None
    return boundingBox[1] / boundingBox[0]


def chunk_image(im: Image, font: ImageFont, columns = 50):
    proportions: float = font_proportions(font)

    chunkWidth = im.width / columns
    chunkHeight = chunkWidth * proportions

    y = 0
    while y < im.height:
        for x in range(columns):
            out = im.crop((x * chunkWidth, y, (x+1) * chunkWidth, y + chunkHeight))
            yield out
        y += int(chunkHeight)

def find_brightness_constant(char_brightnesses: dict, invert = False):
    if invert:
        return 0.75

    max = char_brightnesses["a"]

    for c in CHARACTERS:
        if char_brightnesses[c] > max:
            max = char_brightnesses[c]

    return 500.0 / max

def find_best_char(im: Image, char_brightnesses: dict, invert = False):
    '''
    Find the character whoose brightness best matches the brightness of
    the image. Accepts a dictionary of `char: brightness` pairs
    '''

    k = find_brightness_constant(char_brightnesses, invert)

    imgBrightness = avg_pixel_brightness(im)

    bestChar = " "
    bestBrightness = 0
    for c, b in char_brightnesses.items():
        if (abs(imgBrightness - b * k) < abs(imgBrightness - bestBrightness)):
            bestChar = c
            bestBrightness = b * k

    return bestChar