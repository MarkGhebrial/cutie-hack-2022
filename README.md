# imascii

imascii is a simple utility for generating ASCII art from a bitmap
image. It supports most common image formats (jpeg and png have been
tested), and works cross platform (Windows and Linux have been
tested).

imascii's defining feature is its support for multiple fonts, which
matters because each monospaced font has different width/height
proportions for their characters. The default font, Cascadia, is used
in the VSCode terminal, so the art generated with default settings is
best viewed there.

# Run the program

For pre-built executables, check the releases on this repository.

Install python3 and pip.

Install dependencies with `pip install -r requirements.txt`.

To run from source code, execute `python src/main.py`.

To generate an executable, run `python build.py`. The resulting binary
will be in `dist/` and be called `main`.

# Usage

```
usage: main.py [-h] [-f {cascadia,fantasque,hack,sourcecodepro,ubuntu}]
               [-o OUTNAME] [-i]
               imageName columns

Convert an image to ASCII art.

positional arguments:
  imageName             The path of the image to convert
  columns               The width of the output art, in characters

options:
  -h, --help            show this help message and exit
  -f {cascadia,fantasque,hack,sourcecodepro,ubuntu}, --font {cascadia,fantasque,hack,sourcecodepro,ubuntu}
                        Which font to use, must be a monospace font
  -o OUTNAME            What file to output the resulting art to
  -i, --invert          Invert image colors if this flag is set (to appear
                        better on light mode terminals)

```