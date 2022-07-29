date = str(input("Date: "))
x = date[-5]
print(x)
if date[-5] == "/":
    date = date.split("/")
    