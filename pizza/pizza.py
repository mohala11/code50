from tabulate import tabulate
import sys
import csv


def main():
    check_cvs_file()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            pizza = []
            for row in reader:
                pizza.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(pizza[1:], headers=pizza[0], tablefmt="grid"))


def check_cvs_file():
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a Python file")


if __name__ == "__main__":
    main()











