def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    marks = [",", " ", ".", "/", "*", "_", "-", ";", ":"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in s and list(s) not in marks:
        if i[1] and i[2] in numbers:
            break
        elif i[3:].isdigit() and i[3] == 0:
            break
        else:
            return s


main()