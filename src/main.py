import argparse
from PIL import Image, ImageEnhance, ImageFont, ImageDraw

CHARACTERS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

from util import *
from fonts import fontList, fontDict

def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")

    parser.add_argument(
        "-f", "--font",
        dest="fontName",
        choices=fontList,
        default="sourcecodepro",
        help="Which font to use, must be a monospace font"
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
        default=100,
        type=int
    )

    args = parser.parse_args()

    # Load image and convert it to grayscale
    try:
        im = ImageEnhance.Color(Image.open(args.imageName)).enhance(0.0)
    except OSError:
        print("File " + args.imageName + " not found")
        return

    fontPath = fontDict[args.fontName]

    # Load the font initially to caluate the proportions of its caracters
    font = ImageFont.truetype(fontPath, 150)

    chunkWidth = math.ceil(im.width / args.columns)
    chunkHeight = int(chunkWidth * font_proportions(font))

    # Load the font a second time to size the caracters correctly
    font = ImageFont.truetype(fontPath, chunkHeight)

    charBrightnesses = {}
    for c in CHARACTERS:
        charBrightnesses[c] = avg_pixel_brightness(char_to_img(font, c))
        # print(c + " " + str(charBrightnesses[c]))

    art = "" # The final ASCII art
    col = 0
    for img in chunk_image(im, font, args.columns):
        art += find_best_char(img, charBrightnesses)
        col += 1
        if col >= args.columns: # Next row
            col = 0
            art += "\n"

    if args.outName != None:
        f = open(args.outName, "w")
        f.write(art)
        f.close
    else:
        print(art)

if __name__ == "__main__":
    main()