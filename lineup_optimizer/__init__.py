from .settings import SETTINGS
from .parsers import parse_csv, get_site_from_filepath
from .lineup_builder import LineupBuilder
import re


def optimize_lineup(mode: str, filepath: str, stack: str = ''):
    site = get_site_from_filepath(filepath)
    parser = parse_csv(filepath)
    lineup_builder = LineupBuilder(mode=mode,
                                   site=SETTINGS[site].NAME,
                                   draftables=parser.players)
    if (stack != ''):
        pattern = r'([A-Z]+)?(\d+)-([A-Z]+)?(\d+)'
        match = re.match(pattern, stack)
        if not match:
            print(f"---ERROR: {stack} IS NOT A VALID STACK STRING---")
            return
        matches = [int(x) if x and x.isdigit()
                   else x for x in match.groups() if x is not None]
        matches = re.findall(r'[A-Z]+|\d+', stack)
        if (len(matches) != 2 and len(matches) != 4):
            print(f"---ERROR: {stack} IST NOT A VALID STACK STRING")
            return
        lineup_builder.with_stack_rule(matches)
    best_proj_points = float("-inf")
    best_lineup = None

    for i in range(300):
        lineup = lineup_builder.build()
        salary = lineup.get_lineup_salary()
        proj_points = lineup.get_lineup_projected_points()
        if salary <= SETTINGS[site].MODES.get(mode).get("SALARY_CAP") and (
                proj_points > best_proj_points):
            best_proj_points = proj_points
            best_lineup = lineup
    return best_lineup
