
def main():
    text = "Greeting: "
    greeting = str.lower(input(text).strip())


def check(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")
