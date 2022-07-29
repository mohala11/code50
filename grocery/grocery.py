grocery_list = {}
while True:
    try:
        item = str.upper("")
        if item not in grocery_list:
            i = 1
            grocery_list[item] = i
        elif item in grocery_list:
            grocery_list[item] +=1
    except EOFError:
        break
print(grocery_list)