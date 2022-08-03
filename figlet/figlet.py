import sys
from pyfiglet import Figlet
import random

def main():
    x = str(input("Input: "))
    if len(sys.argv) == 1:
        rng(x)
    if len(sys.argv) == 3:
        specificfont(x)
    else:
        sys.exit("Invalid usage")


def rng(x):
    figlet = Figlet()
    list = figlet.getFonts()
    font = random.choice(list)
    figlet.setFont(font=font)
    print(figlet.renderText(x))


def specificfont(x):
    figlet = Figlet()
    list = figlet.getFonts()
    if sys.argv[1] != "-f" or sys.argv[1] != "--font" and sys.argv[2] not in list:
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(x))


main()
