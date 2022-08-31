import sys
from PIL import Image
import pathlib

def main():
    check_image_file()


def check_image_file():
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        if sys.argv[1][-4:].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        if sys.argv[2][-4:].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")
        if pathlib.Path(sys.argv[1].lower()).suffix != pathlib.Path(sys.argv[2].lower()).suffix:
            sys.exit("Input and output have different extensions")


main()