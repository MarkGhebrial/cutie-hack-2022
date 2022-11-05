import argparse
from PIL import Image, ImageEnhance, ImageFont, ImageDraw

CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]{\}|;:',<.>/?"

from util import *

def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")

    parser.add_argument(
        "-f", "--font",
        dest="fontName",
        help="Which system font to use, must be a monospace font"
    )
    parser.add_argument("-o",
        dest="outName",
        help="What file to output the resulting art to"
    )

    parser.add_argument(
        "imageName",
        help="The path of the image to convert"
    )
    parser.add_argument(
        "columns",
        help="The width of the output art, in characters",
        type=int
    )

    args = parser.parse_args()

    # Load image and convert it to grayscale
    im = ImageEnhance.Color(Image.open(args.imageName)).enhance(0.0)

    for i in chunk_image(im, 1.6):
        print(str(i.width) + " " + str(i.height))
    fontName = "cour.ttf"

    font = ImageFont.truetype(fontName, 15)

    (left, top, right, bottom) = font.getbbox(CHARACTERS)

    txt = "q"

    (tempL, tempT, tempR, tempB) = font.getbbox(txt)

    print(tempL)
    print(tempR)
    print(top)
    print(bottom)

    img = Image.new("RGB", (tempR - tempL, bottom + top), (0, 0, 0))

    d = ImageDraw.Draw(img)

    d.text((0, 0), txt, font=font, fill=(255, 255, 255))

    # img = font.getmask(args.imageName, mode='L')
    img.show()

if __name__ == "__main__":
    main()