def main():
    x = count("Fraction: ")
    print(f"{x} %")


def count(promt):
    while True:
        try:
            x = int(promt[0])
            y = int(promt[2])
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            return float(x / y * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()