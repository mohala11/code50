grocery_list = {}
while True:
    try:
        item = str.upper(input())
        if item not in grocery_list:
            i = 1
            grocery_list[item] = i
            print(grocery_list)
        elif item in grocery_list:
            grocery_list[item] += 1
            print(grocery_list)
    except EOFError:
        print(grocery_list)
        break