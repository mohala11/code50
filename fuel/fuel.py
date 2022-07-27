def main():
    x = count("Fraction: ")
    if x >= 99:
        print("F")
    elif x <= 1:
        print("E")
    else:
        print(f"{x}%")


def count(promt):
    while True:
        try:
            fraction = input(promt).split("/")
            x = int(fraction[0])
            y = int(fraction[1])yes
            
            if x > y:
                raise ValueError
            elif y == 0:
                raise ZeroDivisionError
            else:
                return round(x / y * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


main()