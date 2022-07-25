def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() == False or len(s) < 2 or len(s) > 6:
        return False
    for i in range(2):
        if s[i].isalpha() == False:
            return False
    temp = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            temp += s[i]
            if temp[0] == "0":
                return False
    if s.isalpha():
        return True



main()