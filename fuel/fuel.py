def main():
    fraction = input("Fraction: ").split("/")
    x = convert(fraction)
    print(gauge(x))



def convert(fraction):
    while True:
        try:
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


def gauge(x):
    if x >= 99:
        return "F"
    elif x <= 1:
        return "E"
    else:
        return f"{x}%"


if __name__ == "__main__":
    main()