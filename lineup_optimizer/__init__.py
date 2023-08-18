from lineup_optimizer.site_configs import SITES
from parsers import parse_csv
from lineup_optimizer.LineupBuilder import LineupBuilder


def optimize_lineup(site, filename):
    parser = parse_csv(filename)
    lineup_builder = LineupBuilder(SITES[site].LINEUP_SLOTS,
                                   SITES[site].NAME,
                                   draftables=parser.players)
    return lineup_builder.build()
