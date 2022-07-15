question = str.lower(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip())
x = ["42", "forty-two", "forty two"]
if question in x:
    print("Yes!")
else:
    print("No!")
