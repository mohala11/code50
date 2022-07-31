import re
d = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = str.strip((input("Date: ")))
        # сторим переменную для определения формата даты
        x = date[-5]
        # если дата формата MM/DD/YYYY
        if date[-5] == "/":
            date = date.split("/")
            date[0], date[1] = int(date[0]), int(date[1])
            if date[0] > 12:
                raise ValueError
            elif date[1] > 31:
                raise ValueError
            elif len(date[2]) > 4:
                raise ValueError
            else:
                print(f"{date[2]}-{date[0]:02}-{date[1]:02}")
                break
        # если дата формата MONTHTITLE DD, YYYY
        elif date[-5] == " ":
            date = date.split(" ")
            # проверяем строку на наличие запятой после даты
            coma = re.compile(',')
            if(coma.search(date[1]) == None):
                raise ValueError
            else:
                date[1] = date[1].replace(",", "")
                date[1] = int(date[1])
                if date[0] not in d:
                    raise ValueError
                elif date[1] > 31:
                    raise ValueError
                elif len(date[2]) > 4:
                    raise ValueError
                else:
                    month = d.index(date[0])+1
                    print(f"{date[2]}-{month:02}-{date[1]:02}")
                    break
        else:
            raise ValueError
    except ValueError:
        pass












