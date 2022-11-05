import argparse
from PIL import Image
from PIL import ImageEnhance

def main():
    parser = argparse.ArgumentParser(description="Convert an image to ASCII art.")

    parser.add_argument(
        "imageName",
        help="The path of the image to convert"
    )
    parser.add_argument(
        "-f", "--font",
        dest="fontName",
        help="Which system font to use"
    )
    parser.add_argument("-o",
        dest="outName",
        help="What file to output the resulting art to"
    )

    args = parser.parse_args()

    print(args.imageName)

    print("Hello world")

    # Load image and convert it to grayscale
    im = ImageEnhance.Color(Image.open(args.imageName)).enhance(0.0)

if __name__ == "__main__":
    main()