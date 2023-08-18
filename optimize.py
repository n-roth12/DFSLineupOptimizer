import sys
from lineup_optimizer import optimize_lineup


def optimize(args: list[str]):
    if len(args) < 3:
        print('Missin arguments: must include both site and player pool filename.')
        return
    site = args[1].upper()
    filename = args[2]

    lineup = optimize_lineup(site, filename)
    print(lineup)


if __name__ == '__main__':
    optimize(sys.argv)
