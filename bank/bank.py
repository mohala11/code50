def main():
    text = "Greeting: "
    greeting = str.lower(input(text).strip())
    result = check(greeting)
    print(result)


def check(greeting):
    if greeting.startswith("hello"):
        a = "$0"
        return a
    elif greeting.startswith("h"):
        a = "$20"
        return a
    else:
        a = "$20"
        return a

main()