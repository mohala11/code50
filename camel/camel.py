def main():
    text = "CamelCase: "
    user_input = str(input(text))
    s = user_input.split()
#    print(s)
    convert(user_input)


def convert(user_input):
    s = user_input.split()
        for i in s:
            if i.isupper:
                i = "_" + i.lower()
                return i
            else:
                return i
    print(i)



main()