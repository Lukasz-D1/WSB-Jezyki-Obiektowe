from carwash import *


def main():
    wheels_strat = WheelsHandWashStrategy()
    body_strat = BodyHandWashStrategy()
    carwash = Wash(wheels_strat, body_strat)

    car_order = {
        "wheels": True,
        "body": True
    }

    carwash(car_order)


if __name__ == '__main__':
    main()
