def main():
    text = "CamelCase: "
    user_input = str(input(text))
    s = user_input.split()
#    print(s)
    convert(s)


def convert(s):
    for i in s:
        if i.isupper:
            i = "_" + i.lower()
            return i
        else:
            return i
    print(i)



main()