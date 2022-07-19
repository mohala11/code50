def main():
    text = "What time is it? "
    time = str(input(text))
    result = convert(time)
        if result >= 7.0 and <= 8.0:
            print("breakfast time")
        elif result >= 12.0 and <= 13.0:
            print("meal time")
        elif result >= 18.0 and <= 19.0:
            print("dinner time")
        else:
            print()



def convert(time):
    hours, minutes = time.split(":")
    floatminutes = minutes / 60
    floattime = hours + floatminutes
    return floattime



if __name__ == "__main__":
    main()
