# One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

# In a file called professor.py, implement a program that:

# Prompts the user for a level,. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total. If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:


import random

# я в душе не ебу зачем дана такая уебанская структура кода и какую стратегическую хуйню я должен решать в мейне, но раз уж я долбаеб, то я заколю функцию в переменную и передам ее другой функции, потому что да
def main():
    level = get_level()
    generate_integer(level)


# ну тут мы типа спрашиваем уровень сложности, хуе-мое, очень важно, очень функционально
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except:
            pass
    return level


# зато тут теперь ебанутые джунгли, джонни, ааааа, ифы на деревьях
def generate_integer(level):
            i = 0
            score = 0
            while i < 10:
                lowrange = 1 ** level - 1
                upperrange = 10 ** level
                x = random.randrange(lowrange, upperrange)
                y = random.randrange(lowrange, upperrange)
                z = x + y
                f = int(input(f"{x} + {y} = "))
                # если долбаеб не смог сложить два числа
                if f != z:
                    ya_debil(x, y, z)
                else:
                    score += 1
                i += 1
            print(f"Score: {score}")


def ya_debil(x, y, z):
    print("EEE")
    errorcount = 0
    while errorcount <= 1:
        f = int(input(f"{x} + {y} = "))
        errorcount += 1
        if f != z:
            print("EEE")
    print(f"{x} + {y} = {z}")



if __name__ == "__main__":
    main()
