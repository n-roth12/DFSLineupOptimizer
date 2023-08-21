from .site_configs import SITES


class LineupBuilderSlot:

    # you would pass title="QB" or title="WR2" and it is
    # optional to pass eligible_positions
    def __init__(self, title: str, site: str, eligible_positions: list = None,
                 eligible_team_abbr: str = None, max_salary: int = None):
        self.title = title
        self.site = site
        if not eligible_positions or not len(eligible_positions):
            self.default_eligible_position(title)
        self.eligible_team = eligible_team_abbr
        self.max_salary = max_salary

    def __str__(self) -> str:
        return f'{self.title} ({self.eligible_positions})'

    def default_eligible_position(self, title: str):
        if title != "FLEX":
            self.eligible_positions = ["".join(filter(lambda x: x.isalpha(), title))]
        else:
            self.eligible_positions = SITES[self.site].FLEX_POSITIONS.get(title)

    def set_eligible_team(self, eligible_team_abbr: str):
        self.eligible_team = eligible_team_abbr

    def set_eligible_positions(self, eligible_positions: list):
        self.eligible_positions = eligible_positions

    def set_max_salary(self, max_salary: int):
        self.max_salary = max_salary
