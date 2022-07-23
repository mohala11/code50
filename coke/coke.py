def main():
    price = 50
    coinbase = [5, 10, 25]
    while price > 0:
        s = int(input('Amount Due: ' + str(price) + '\nInsert Coin: '))
        if s in coinbase:
            price = price - s
        else:
            break
    print('Change Owed:', abs(price))


main()
