import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
list = figlet.getFonts()

def main(figlet, list):
    a = check(list)
    x = str(input("Input: "))
    if a == 1:
        rng(x, list, figlet)
    elif a == 2:
        specificfont(x, figlet)
    elif a == 3:
        sys.exit("Invalid usage")
#    if len(sys.argv) == 1 or len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list:
#       x = str(input("Input: "))
#        if len(sys.argv) == 1:
#            rng(x, list, figlet)
#        elif sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list:
#            specificfont(x, figlet)
#        else:
#            sys.exit("Invalid usage")
#    else:
#        sys.exit("Invalid usage")


def check(list):
    if len(sys.argv) == 1:
        return 1
    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list:
        return 2
    else:
        return 3



def rng(x, list, figlet):
    figlet = Figlet()
    font = random.choice(list)
    figlet.setFont(font=font)
    print("Output:\n" + figlet.renderText(x))


def specificfont(x,  figlet):
    figlet = Figlet()
    figlet.setFont(font=sys.argv[2])
    print("Output:\n" + figlet.renderText(x))


if __name__ == "__main__":
    main(figlet, list)
