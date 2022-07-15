text = "Greeting: "
greeting = str.lower(input(text).strip())
if greeting.startswith("hello") == True:
    print("$0")
elif greeting.startswith("h") == True:
    print("$20")
else:
    print("$100")
