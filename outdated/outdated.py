date = str(input("Date: "))
x = date[-5]
if date[-5] == "/":
    date = date.split("/")
elif len(date[0]) > 2 and date[0] > 12:
    print("dolbaeb")
    date[0], date[1] = int(date[0]), int(date[1])
    print(f"{date[2]}-{date[0]:02}-{date[1]:02}")

else:
    print("fok uuuuuuuuuuuuuuuuuuu")
