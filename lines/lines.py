import sys


while True:
    try:
        if len(sys.argv) == 1:
            print("Too few command-line arguments")
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
        elif sys.argv[1].endswith(".py") == False:
            print("Not a Python file")
        else:
            i = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    i += 1
                print(i)
    except FileNotFoundError:
        sys.exit("File does not exist")



#print(i)

