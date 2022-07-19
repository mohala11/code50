def main():
    text = "What time is it? "
    time = str(input(text))
    result = convert(time)
    if result >= 7.0 and result <= 8.0:
        print("breakfast time")
    elif result >= 12.0 and result <= 13.0:
        print("lunch time")
    elif result >= 18.0 and result <= 19.0:
        print("dinner time")
    else:
        print()



def convert(time):
    hours, minutes = time.split(":")
    floatminutes = float(minutes) / 60
    floattime = float(hours) + floatminutes
    return floattime



if __name__ == "__main__":
    main()
