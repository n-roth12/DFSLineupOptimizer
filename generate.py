import sys
from lineup_optimizer import optimize_lineup
from lineup_optimizer.exporter import export_lineups
from lineup_optimizer.parsers import get_site_from_filepath


def generate(args: list[str]):
    if len(args) < 3:
        print("Missing arguments: must include both fame mode and player pool filename.")
        return
    mode = args[1].upper()
    num_lineups = int(args[2])
    filepath = args[3]
    site = get_site_from_filepath(filepath)

    result = []
    for i in range(num_lineups):
        result.append(optimize_lineup(mode, filepath).lineup)

    export_lineups(site, mode, result)


if __name__ == "__main__":
    generate(sys.argv)
