def main():
    text = "Expression: "
    userinput = input(text).split(" ")
    x = float(userinput[0])
    y = userinput[1]
    z = float(userinput[2])
    result = mathandmagic(x, y, z)
    print(result)


def mathandmagic(x, y, z):
    if y == "+":
        d = x + z
        return d
    elif y == "-":
        d = x - z
        return d
    elif y == "*":
        d = x * z
        return d
    elif y == "/":
        d = x / z
        return d
    else:
        return "Enter correct expression!"


main()