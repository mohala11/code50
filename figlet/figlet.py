import sys
from pyfiglet import Figlet
import random

def main():
    x = str(input("Input: "))
    if len(sys.argv) == 1:
        rng(x)
    else:
        specificfont(x)


def rng(x):
    figlet = Figlet()
    list = figlet.getFonts()
    font = random.choice(list)
    figlet.setFont(font=font)
    print(figlet.renderText(x))


def specificfont(x):
    figlet = Figlet()
    if 
    print(figlet.renderText(x))


main()
