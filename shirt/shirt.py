import sys
from PIL import Image
import pathlib

def main():
    check_image_file()
    print(sys.argv[1][-4:].lower())


def check_image_file():
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1][-4:].lower() != ".jpg" or sys.argv[1][-4:].lower() != ".jpeg" or sys.argv[1][-4:].lower() != ".png":
            sys.exit("Invalid input")
        elif pathlib.Path(sys.argv[1].lower()).suffix != pathlib.Path(sys.argv[2].lower()).suffix:
            sys.exit("Input and output have different extensions")


main()