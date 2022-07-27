while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        if x > y:
            except ValueError:
                pass
        elif y == 0:
            raise ZeroDivisionError
        percent = int(x / y * 100)



print(f"{percent}%")
