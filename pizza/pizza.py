from tabulate import tabulate
import sys
import csv


def main():
    check_cvs_file()
    try:
        




def check_cvs_file():
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a Python file")





    else:

except FileNotFoundError:
    sys.exit("File does not exist")




