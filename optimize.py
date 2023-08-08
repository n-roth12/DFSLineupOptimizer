import sys
from lineup_optimizer.LineupBuilder import LineupBuilder
from lineup_optimizer import SITES


def optimize(args: list[str]):
    if len(args) < 3:
        print('Missin arguments: must include both site and player pool filename.')
        return
    site = args[1]
    filename = args[2]
    x = LineupBuilder(SITES[site], SITES[site].LINEUP_SLOTS)
    print(x)


if __name__ == '__main__':
    optimize(sys.argv)
