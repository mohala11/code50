def main():
    user_input = str(input("Please input something with :) or :( "))
    convert(user_input)


def convert(user_input):
    splitted_input = user_input.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "🙁"
    }
    outcome = " "
    for word in splitted_input:
        outcome += emojis.get(word, word) + " "
    print(outcome)


main()