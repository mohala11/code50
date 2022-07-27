while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        percent = x / y * 100
        if x > y:
            raise ValueError("zaebaL")
    finally:
        print(f"{percent}%")
