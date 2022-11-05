import argparse
from PIL import Image
from PIL import ImageEnhance

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

    print(args.imageName)

    print("Hello world")

    # Load image and convert it to grayscale
    im = ImageEnhance.Color(Image.open(args.imageName)).enhance(0.0)

    for i in chunk_image(im, 1.6):
        print(str(i.width) + " " + str(i.height))

if __name__ == "__main__":
    main()