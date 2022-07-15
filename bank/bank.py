def main():
    text = "Greeting: "
    greeting = str.lower(input(text).strip())
    check(greeting)



def check(g):
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")

main()