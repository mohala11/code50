import sys
from pyfiglet import Figlet

x = str.input("Input ")
if sys.argv[1] == None:
    random(x)
else:
    specificfont(x)


