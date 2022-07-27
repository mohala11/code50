while True:
    try:
        fraction = input("Fraction: ")
        x = int(fraction[0])
        y = int(fraction[2])
        if x > y:
            raise ValueError:
            
        percent = int(x / y * 100)
        break
    except ValueError:
        if x > y:
            pass
    except ZeroDivisionError:
        pass

print(f"{percent}%")
