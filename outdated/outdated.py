date = str(input("Date: "))
x = date[-5]
if date[-5] == "/":
    date = date.split("/")
    print(f"{date[2]:.2f}-{date[0]:.2f}-{date[1]}")
else:
    print("fok uuuuuuuuuuuuuuuuuuu")
