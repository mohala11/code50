d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
c = float(0)
while True:
    try:
        key = str.title(input("Item: "))
        if key in d:
            x = float(d[key])
            print(x)
            c += x
            print ("Total: $",float(c))
        elif key not in d:
            raise KeyError
    except KeyError:
        continue
    except EOFError:
        print("")
        break


