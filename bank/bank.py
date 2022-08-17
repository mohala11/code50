def main():
    text = "Greeting: "
    greeting = input(text)
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    var = str(greeting).lower().strip()
    if var.startswith("hello"):
        return 0
    elif var.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()