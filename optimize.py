import sys
from lineup_optimizer import optimize_lineup


def optimize(args: list[str]):
    if len(args) < 3:
        print("Missing arguments: must include both fame mode and player pool filename.")
        return
    mode = args[1].upper()
    filepath = args[2]
    lineup = optimize_lineup(mode, filepath)
    print(lineup)


if __name__ == "__main__":
    optimize(sys.argv)
