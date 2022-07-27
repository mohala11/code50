def main():
    fraction = input("Fraction: ")
    x = count(fraction)
    print(f"{x} %")


def count(fraction):
    while True:
        try:
            x = int(fraction[0])
            y = int(fraction[2])
            return int(x / y *100)
        except ValueError:
            pass
        except ZeroDivisionError:
            print("ya tvoy rot ebal")


main()