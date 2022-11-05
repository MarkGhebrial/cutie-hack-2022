from PIL import Image
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