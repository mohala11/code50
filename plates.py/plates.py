def main():
    plate = input("Plate: ")
    x = len(plate)
    if x != 4 or x != 6:
        print("Invalid")
    else:
        is_valid()


def is_valid(plate):
    if len(x) == 4:
        if type(plate[0:2]) == "str" and type(plate[3:4]) == "int":
            print("Valid")
        else:
            print("Invalid")
    elif len(x) == 6:
        if type(plate[0:3]) == "str" and type(plate[4:6]) == "int":
            print("Valid")
        else:
            print("Invalid")





#    if is_valid(plate):
#        print("Valid")
#   else:
#        print("Invalid")


#def is_valid(s):



main()
