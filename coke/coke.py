def main():
    price = '50'
    coinbase = ['5', '10', '25']
    s = int(input('Amount Due: ' + price + '\nInsert Coin: '))
    for s in coinbase and price >= 0:
        price -= s
        

main()
