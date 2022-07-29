date = str(input("Date: "))
x = date[-5]
if date[-5] == "/":
    date = date.split("/")
    date[0], date[1] = int(date[0]), int(date[1])
    if len(date[0]) > 2 and date[0] > 12:
        print("dolbaeb1")
    elif len(date[1]) > 2 and date[1] > 31:
        print("dolbaeb2")
    elif len(date[2]) > 4:
        print("dolbaeb3")
    else:
        print(f"{date[2]}-{date[0]:02}-{date[1]:02}")
else:
    print("fok uuuuuuuuuuuuuuuuuuu")
