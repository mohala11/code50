def main():
    text = "CamelCase: "
    user_input = str(input(text))
    convert(user_input)


def convert(user_input):
    s = list(user_input)
    outcome = "snake_case: "
    for i in s:
        if i.isupper():
            i = "_" + i.lower()
            outcome += i
        else:
            outcome += i
    print(outcome)


main()
