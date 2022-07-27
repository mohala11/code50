def main():
    fraction = input("Fraction: ")
    x = count(fraction)
    print(f"{x} %")


def count(fraction):
    while True:
        x = int(fraction[0])
        y = int(fraction[2])
        try:
            i = x / y *100
            if x > y:
                raise ValueError("zaebaL")
        except ValueError:
            pass
            percent = x / y * 100

    print(f"{percent}%")