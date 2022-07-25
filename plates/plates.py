def main():
    plate = input("Plate: ")
    x = len(plate)
    marks = [",", " ", ".", "/", "*", "_", "-", ";", ":"]
    if 2 <= x <= 6 and list(plate) not in marks:
        is_valid(plate, x)
    else:
        print("Invalid")


def is_valid(plate,x):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if x == 2:
        if plate[0:2] not in numbers:
            print("Valid")
        else:
            print("Invalid")
    if x == 3:
        if plate[0:2] not in numbers and plate[2] in numbers[1:10] or plate[0:3] not in numbers:
            print("Valid")
        else:
            print("Invalid")
    if x == 4:
        if plate[0:2] not in numbers and plate[2] in numbers[1:10] and plate[3] in numbers:
            print("Valid")
        elif plate[0:3] not in numbers and plate[3] in numbers[1:10] or plate[0:4] not in numbers:
            print("Valid")
        else:
            print("Invalid")
    if x == 5:
        if plate[0:2] not in numbers and plate[2] in numbers[1:10] and plate[3:5] in numbers:
            print("Valid")
        elif plate[0:3] not in numbers and plate[3] in numbers[1:10] and plate[4] in numbers:
            print("Valid")
        elif plate[0:4] not in numbers and plate[4] in numbers[1:10] or plate[0:5] not in numbers:
            print("Valid")
        else:
            print("Invalid")
    if x == 6:
        if plate[0:2] not in numbers and plate[2] in numbers[1:10] and plate[3:6] in numbers:
            print("Valid")
        elif plate[0:3] not in numbers and plate[3] in numbers[1:10] and plate[4:6] in numbers:
            print("Valid")
        elif plate[0:4] not in numbers and plate[4] in numbers[1:10] and plate[5] in numbers:
            print("Valid")
        elif plate[0:5] not in numbers and plate[5] in numbers[1:10] or plate[0:6] not in numbers:
            print("Valid")
        else:
            print("Invalid")


main()