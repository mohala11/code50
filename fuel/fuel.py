while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        percent = x / y * 100
    except ValueError:
        if x > y:
            break
    finally:
        print(f"{percent}%")
