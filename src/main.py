import argparse

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


if __name__ == "__main__":
    main()