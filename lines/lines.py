import sys

i = o

with open(sys.argv[1]) as file:
    for line in file:
        i += 1


print(i)

