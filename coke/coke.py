def main():
    price = '50'
    coinbase = ['5', '10', '25']
    s = int(input('Amount Due: ' + price + '\nInsert Coin: '))
    while s in coinbase and price >= 0:
        price += s;
        print('Amount Due: ' + price + '\nInsert Coin: ')


main()
