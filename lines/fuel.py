def main():
    fraction = input("Fraction: ")
    fraction_convert = convert(fraction)
    print(gauge(fraction_convert))



def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            f = int(x) / int(y)
            if f <= 1:
                return int(f*100)
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
           raise


def gauge(fraction_convert):
    if fraction_convert >= 99:
        return "F"
    elif fraction_convert <= 1:
        return "E"
    else:
        return f"{fraction_convert}%"


if __name__ == "__main__":
    main()