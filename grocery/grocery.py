grocery_list = {}
while True:
    try:
        item = str.upper(input())
        if item not in grocery_list:
            i = 1
            grocery_list[item] = i
        elif item in grocery_list:
            grocery_list[item] += 1
    except EOFError:
        d = sorted(grocery_list.items())
        print(value, key, sep=" ")
        break
