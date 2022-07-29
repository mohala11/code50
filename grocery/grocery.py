# заводим словарь
grocery_list = {}
# цикл наполнения
while True:
    try:
        # запрашиваем айтем
        item = str.upper(input())
        # если айтем новый
        if item not in grocery_list:
            # стартовое количество айтема
            i = 1
            # запись айтема и количества айтема в словарь
            grocery_list[item] = i
            # если айтем уже в словаре
        elif item in grocery_list:
            # увеличивает количество айтема на 1
            grocery_list[item] += 1
    # если юзер прерывает цикл
    except EOFError:
        # сортируем словарь по айтемам
        {k: v for k, v in sorted(grocery_list.items(), key=lambda v: v[1])}
        print(grocery_list)
        # выводим словарь на экран в виде КОЛИЧЕСТВО АЙТЕМ
        #for key, value in grocery_list.items():
            #print(value, key, sep = " ")
        break
