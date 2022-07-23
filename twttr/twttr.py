def main():
    text = 'Input: '
    user_input = str(input(text))
    convert(user_input)


def convert(user_input):
    s = list(user_input)
    outcome = 'Output: '
    list_of_vowels = ['E', 'Y', 'U', 'I', 'O', 'A', 'e', 'y', 'u', 'i', 'o', 'a']
    for i in s:
        if i in list_of_vowels:
            outcome = outcome
        elif i not in list_of_vowels:
            outcome += i
    print(outcome)
    

