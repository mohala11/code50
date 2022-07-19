def main():
    text = "What time is it? "
    userinput = str(input(text))
    timesplit = userinput.split(" ")
    time = timesplit[0]
    jopka = timesplit[1]
    result = convert(time)
    if result >= 7.0 and result <= 8.0 and jopka == "a.m.":
        print("breakfast time")
    elif result >= 12.0 and result <= 12.(9) and jopka == "a.m.":
        print("lunch time")
    elif result == 1 and jopka == "p.m.":
        print("lunch time")
    elif result >= 6.0 and result <= 7.0 and jopka == "p.m.":
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
