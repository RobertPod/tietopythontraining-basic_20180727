#!/usr/bin/env python3


def main():
    print('Enter cost in dolars')
    dolars = int(input())
    print('Enter cost in cents')
    cents = int(input())
    print('Enter number cupcakes')
    cupcakes = int(input())
    total_cost: int = total_cost_in_cents(dolars, cents, cupcakes)
    print(str(total_cost // 100) + ' ' + str(total_cost % 100))


def total_cost_in_cents(dolars: int, cents: int, cupcakes: int):
    return (dolars * 100 + cents) * cupcakes


if __name__ == '__main__':
    main()
