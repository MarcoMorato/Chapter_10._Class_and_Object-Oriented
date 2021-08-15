import coin


def main():
    my_coin = coin.Coin()
    print(my_coin.get_sideup())

    flip(my_coin)

    print(my_coin.get_sideup())


def flip(my_coin):
    my_coin.toss()


main()
