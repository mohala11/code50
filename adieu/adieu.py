import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = str(input("Name: "))
        name_list.append(name)
    except EOFError:
        print(p)
        break

