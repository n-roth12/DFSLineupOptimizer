from .settings import SETTINGS
from .parsers import parse_csv, get_site_from_filepath
from .lineup_builder import LineupBuilder
import re


def optimize_lineup(mode: str, filepath: str, stack: str = None):
    site = get_site_from_filepath(filepath)
    parser = parse_csv(filepath)
    lineup_builder = LineupBuilder(mode=mode,
                                   site=SETTINGS[site].NAME,
                                   draftables=parser.players)
    if (stack != ''):
        matches = re.findall(r'[A-Z]+|\d+', stack)
        lineup_builder.with_stack_rule(matches[0], int(
            matches[1]), matches[2], int(matches[3]))
    best_proj_points = float("-inf")
    best_lineup = None

    for i in range(300):
        lineup = lineup_builder.build()
        # print(lineup)
        salary = lineup.get_lineup_salary()
        proj_points = lineup.get_lineup_projected_points()
        if salary <= SETTINGS[site].MODES.get(mode).get("SALARY_CAP") and (
                proj_points > best_proj_points):
            best_proj_points = proj_points
            best_lineup = lineup
    return best_lineup
