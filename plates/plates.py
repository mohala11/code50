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
    c = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            c += s[i]
            if c[0] == "0":
                return False
    if s.isalpha():
        return True
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            x = i
            break
    valid = True
    for i in range(x, len(s)):
        if s[i].isalpha():
            valid = False

    if valid == False:
        return False
    return True



main()