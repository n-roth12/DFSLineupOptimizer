class LineupBuilderSlot:
    def __init__(self, title: str, site: str, eligible_positions: list,
                 pts_multiplier: float, salary_multiplier: float,
                 eligible_team_abbr: str = None, max_salary: int = None):
        self.title = title
        self.eligible_positions = eligible_positions
        self.eligible_team = eligible_team_abbr
        self.max_salary = max_salary
        self.pts_multiplier = pts_multiplier
        self.salary_multiplier = salary_multiplier

    def __str__(self) -> str:
        return f"{self.title} ({self.eligible_positions})"

    def set_eligible_team(self, eligible_team_abbr: str):
        self.eligible_team = eligible_team_abbr

    def set_eligible_positions(self, eligible_positions: list):
        self.eligible_positions = eligible_positions

    def set_max_salary(self, max_salary: int):
        self.max_salary = max_salary
