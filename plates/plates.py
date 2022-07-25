def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    marks = [",", " ", ".", "/", "*", "_", "-", ";", ":"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(s) <=6 and s not in marks:
        if s[0] and s[1] in numbers:
            break
        elif 
        else:
            return s

main()