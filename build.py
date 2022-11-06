import platform
import PyInstaller.__main__

system = platform.system()

if system == "Linux" or system == "Darwin":
    PyInstaller.__main__.run([
        "src/main.py",
        "--onefile",
        "--add-data", "fonts:fonts",
        "--name", "imascii"
    ])

elif system == "Windows":
    PyInstaller.__main__.run([
        "src/main.py",
        "--onefile",
        "--add-data", "fonts;fonts",
        "--name", "imascii"
    ])

else:
    print("System \"" + system + "\" not supported")