def main():
    text = "What time is it? "
    userinput = str(input(text))
    timesplit = userinput.split(" ")
    time = timesplit[0]
    is_am_time = timesplit[1] == "a.m."
    result = convert(time)
    if result >= 7.0 and result <= 8.0 and is_am_time:
        print("breakfast time")
    elif result >= 12.0 and result <= 12.99 and is_am_time:
        print("lunch time")
    elif result == 1 and !is_am_time:
        print("lunch time")
    elif result >= 6.0 and result <= 7.0 and !is_am_time:
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
