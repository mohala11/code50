date = str(input("Date: "))
x = date[-5]
if date[-5] == "/":
    date = date.split("/")
    date[0], date[1] = float(date[0]), float(date[1])
    print(f"{date[2]}-{date[0]:.2f}-{date[1]:2f}")
else:
    print("fok uuuuuuuuuuuuuuuuuuu")
