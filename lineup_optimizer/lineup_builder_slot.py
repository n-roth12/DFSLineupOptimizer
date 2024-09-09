from typing import List


class LineupBuilderSlot:
    def __init__(self, title: str, site: str, eligible_positions: list,
                 pts_multiplier: float, salary_multiplier: float,
                 eligible_teams: List[str] = [], max_salary: int = None):
        self.title = title
        self.eligible_positions = eligible_positions
        self.eligible_teams = eligible_teams
        self.max_salary = max_salary
        self.pts_multiplier = pts_multiplier
        self.salary_multiplier = salary_multiplier

    def __str__(self) -> str:
        return f"{self.title} ({self.eligible_positions})"

    def set_eligible_teams(self, eligible_teams: List[str]):
        self.eligible_teams = eligible_teams

    def set_eligible_positions(self, eligible_positions: list):
        self.eligible_positions = eligible_positions

    def set_max_salary(self, max_salary: int):
        self.max_salary = max_salary
