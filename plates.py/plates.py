def main():
    plate = input("Plate: ")
    x = len(plate)
    if x == 4 or x == 6:
        is_valid(plate, x)
    else:
        print("Invalid")


def is_valid(plate, x):
    s = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if x == 4:
        if plate[0:2] not in s and plate[2] in s[1:9] and plate[3] in s:
            print("Valid")
        else:
            print("Invalid")
    else:
        if plate[0:3] not in s and plate[3] in s[1:9] and plate[4:6] in s:
            print("Valid")
        else:
            print("Invalid")


main()
