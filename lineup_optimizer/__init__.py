from .settings import SETTINGS
from .parsers import parse_csv, get_site_from_filepath
from .lineup_builder import LineupBuilder


def optimize_lineup(mode: str, filepath: str):
    site = get_site_from_filepath(filepath)
    parser = parse_csv(filepath)
    lineup_builder = LineupBuilder(SETTINGS[site].MODES.get(mode).get("POSITIONS"),
                                   SETTINGS[site].NAME,
                                   draftables=parser.players,
                                   mode=mode)
    best_proj_points = float("-inf")
    best_lineup = None

    for i in range(300):
        lineup = lineup_builder.build()
        salary = lineup.get_lineup_salary()
        proj_points = lineup.get_lineup_projected_points()
        if salary <= SETTINGS[site].MODES.get(mode).get("SALARY_CAP") and proj_points > best_proj_points:
            best_proj_points = proj_points
            best_lineup = lineup
    return best_lineup
