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
        new_list = sorted(grocery_list.items(), key=lambda x: x[0], reverse=False)
        for i in new_list:
            print(i[1], i[0])
        break
