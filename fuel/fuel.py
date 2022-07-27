while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        if x > y:
            raise ValueError("zaebaL")
    except ValueError:
        pass
    percent = x / y * 100
    print(f"{percent}%")