def main():
    plate = input("Plate: ")
    x = len(plate)
    print(x)
    if x == 4 or x == 6:
        is_valid(plate, x)
    else:
        print("loh")


def is_valid(plate, x):
    if x == 4:
        if type(plate[0:2]) == "class 'str'" and type(plate[3:4]) == "class 'int'":
            print("Valid")
        else:
            print("Invalid")
    elif x == 6:
        if type(plate[0:3]) == "class 'int'" and type(plate[4:6]) == "class 'int'":
            print("Valid")
        else:
            print("Invalid")



main()
