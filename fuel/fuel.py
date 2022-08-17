def main():
    a = str(input("Fraction: "))
    x = convert(a)
    print(gauge(x))



def convert(a):
    while True:
        try:
            fraction = a.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            else:
                return round(x / y * 100)
        except TypeError:
            pass
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