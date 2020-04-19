from tsp import *


def main():
    x = Tsp(100)
    x.set_weights('constant')
    x.random_tour()

    for i in range(0, 10**3):
        x.transposition()
        x.reevaluate_tour()
    print(x.tour_lengths)


if __name__ == '__main__':
    main()
