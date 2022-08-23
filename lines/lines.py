import sys

i = 0

with open(sys.argv[1]) as file:
    if len(sys.argv) == 1:
        print("Too few command-line arguments")
    for line in file:
        i += 1


print(i)

