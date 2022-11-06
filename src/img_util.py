from PIL import Image

def avg_pixel_brightness(im: Image):
    sum = 0
    count = 0

    for x in range(im.width):
        for y in range(im.height):
            pixel = im.getpixel((x,y))
            if type(pixel) == int:
                sum += pixel
            else:
                sum += pixel[0]
            count += 1

    return sum / count