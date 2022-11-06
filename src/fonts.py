import os

fontDict = {
    "cascadia": "fonts/CascadiaMono.ttf",
    "fantasque": "fonts/FantasqueSansMono-Regular.ttf",
    "hack": "fonts/Hack-Regular.ttf",
    "sourcecodepro": "fonts/SourceCodePro-Regular.ttf",
    "ubuntu": "fonts/UbuntuMono-R.ttf",
}

fontList = []
for k, v in fontDict.items():
    fontList.append(k)