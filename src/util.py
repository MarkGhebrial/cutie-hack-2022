from PIL import Image, ImageFont, ImageDraw
import math
from main import CHARACTERS

def bounding_box(font: ImageFont, s: str): # Returns a tuple of (width, height):

    (left, top, right, bottom) = font.getbbox(CHARACTERS)

    height = bottom + top

    (left, top, right, bottom) = font.getbbox(s)

    width = right - left

    return (width, height)

def char_to_img(font: ImageFont, c: str): # Returns an Image
    (w, h) = bounding_box(c)

    # Create an image that's the same size as the chracter
    img = Image.new("RGB", (w, h), (0, 0, 0))

    d = ImageDraw.Draw(img)

    d.text((0, 0), c, font=font, fill=(255, 255, 255))

def font_proportions(font: ImageFont):
    '''
    Returns the height/width ratio of characters in the specified font.
    If the font is not monospace (i.e. the width/height of each
    character is different), then `None` is returned
    '''

    boundingBox = bounding_box(font, "a")
    for c in CHARACTERS:
        if bounding_box(font, c) != boundingBox:
            return None
    return boundingBox[1] / boundingBox[0]


def chunk_image(im: Image, font: ImageFont, columns = 50):
    proportions = font_proportions(font)

    chunkWidth = math.ceil(im.width / columns)
    chunkHeight = chunkWidth * proportions

    for x in range(columns):
        y = 0
        while y < im.height:
            out = im.crop((x * chunkWidth, y, (x+1) * chunkWidth, y + chunkHeight))
            y += int(chunkHeight)
            yield out