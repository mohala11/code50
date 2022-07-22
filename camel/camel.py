def main():
    text = "CamelCase: "
    user_input = str(input(text))
    s = user_input.split()
#    print(s)
    convert(s)
    outcome = " "
    for i in s:
        outcome += 


def convert(s):
    for i in s:
        if i.isupper:
            i = "_" + i.lower()
            return i
        else:
            return i





main()