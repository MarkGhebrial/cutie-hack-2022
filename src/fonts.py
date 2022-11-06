import os

executable_dir = os.path.dirname(os.path.realpath(__file__))

fontDict = {
    "cascadia": executable_dir + "/../fonts/CascadiaMono.ttf",
    "fantasque": executable_dir + "/../fonts/FantasqueSansMono-Regular.ttf",
    "hack": executable_dir + "/../fonts/Hack-Regular.ttf",
    "sourcecodepro": executable_dir + "/../fonts/SourceCodePro-Regular.ttf",
    "ubuntu": executable_dir + "/../fonts/UbuntuMono-R.ttf",
}

fontList = []
for k, v in fontDict.items():
    fontList.append(k)