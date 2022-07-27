while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        percent = x / y * 100
    e
        if x > y:
            raise ValueError
    finally:
        print(f"{percent}%")
