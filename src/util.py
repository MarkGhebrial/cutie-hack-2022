from PIL import Image, ImageFont
import math

def chunk_image(im: Image, charProportions, columns = 50):
    chunkWidth = math.ceil(im.width / columns)
    chunkHeight = chunkWidth * charProportions

    for x in range(columns):
        y = 0
        while y < im.height:
            out = im.crop((x * chunkWidth, y, (x+1) * chunkWidth, y + chunkHeight))
            y += int(chunkHeight)
            yield out

def bounding_box(font: ImageFont, s: str): # Returns a tuple of (width, height):
    pass

def char_to_string(font: ImageFont, c: str): # Returns an Image
    pass