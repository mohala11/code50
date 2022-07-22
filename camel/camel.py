def main():
    text = "CamelCase: "
    user_input = str(input(text))
#    print(s)
    convert(user_input)


def convert(user_input):
    s = user_input.split()
    outcome = " "
    for i in s:
        if i.isupper:
            i = "_" + i.lower()
            outcome += i
        else:
            outcome += i
    print(outcome)


main()
