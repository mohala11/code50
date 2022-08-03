import sys
from pyfiglet import Figlet
import random

def main():
    x = str(input("Input "))
#    if sys.argv[1] == None:
    random(x)
#    else:
#        specificfont(x)


def random(x):
    figlet = Figlet()
    list = figlet.getFonts()
    font = random.choice(list)
    figlet.setFont(font=font)
    print(figlet.renderText(x))




main()
