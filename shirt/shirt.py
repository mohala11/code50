import sys
from PIL import Image

def main():
    check_image_file()



def check_image_file():
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].lower().endswith() and sys.argv[2].endswith(".csv") == False:
            sys.exit("Not a CSV file")