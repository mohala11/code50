def main():
    fraction = input("Fraction: ")
    fraction_convert = convert(fraction)
    print(gauge(fraction_convert))



def convert():
    while True:
        try:
            fraction = input("Fraction: ").split("/")
            if int(fraction[0]) > int(fraction[1]):
                raise ValueError
            elif int(fraction[1]) == 0:
                raise ZeroDivisionError
            else:
                return round(int(fraction[0]) / int(fraction[1]) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def gauge(fraction_convert):
    if fraction_convert >= 99:
        return "F"
    elif fraction_convert <= 1:
        return "E"
    else:
        return f"{fraction_convert}%"


if __name__ == "__main__":
    main()