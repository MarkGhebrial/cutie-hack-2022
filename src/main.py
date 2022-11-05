import argparse
from PIL import Image, ImageEnhance, ImageFont, ImageDraw

CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]{\}|;:',<.>/? "

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

    fontName = "cour.ttf"

    font = ImageFont.truetype(fontName, 15)

    chunkWidth = math.ceil(im.width / args.columns)
    chunkHeight = int(chunkWidth * font_proportions(font))

    font = ImageFont.truetype(fontName, chunkHeight)

    charBrightnesses = {}
    for c in CHARACTERS:
        charBrightnesses[c] = avg_pixel_brightness(char_to_img(font, c))
        print(c + " " + str(charBrightnesses[c]))

    art = ""

    col = 0
    for img in chunk_image(im, font, args.columns):
        art += find_best_char(img, charBrightnesses)
        col += 1
        if col >= args.columns:
            col = 0
            art += "\n"

    print(art)

if __name__ == "__main__":
    main()