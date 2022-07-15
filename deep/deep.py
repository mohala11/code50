question = str.lower(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))
x = ["42", "forty-two", "forty two"]
question = question.strip()
if question in x:
    print("Yes!")
else:
    print("No!")
