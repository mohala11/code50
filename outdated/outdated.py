date = str(input("Date: "))
x = date[-5]
print(x)
if date[-5] == "/":
    date = date.split("/")
    print(f"{date[2]}-{date[0]}-{date[1]}")
else:
    print("fok uuuuuuuuuuuuuuuuuuu")
    