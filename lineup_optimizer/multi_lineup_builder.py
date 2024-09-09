from .lineup_builder_slot import LineupBuilderSlot
from .lineup import Lineup
from .lineup_builder import LineupBuilder
from .settings import SETTINGS

from random import randint
from math import floor
from typing import List

STACK_ORDER = ["QB", "WR", "TE", "RB", "DST"]


class MultiLineupBuilder:

    def __init__(self, num_lineups: int, site: str,
                 draftables: list, mode: str = "FULL_ROSTER"):
        self.lineup_slots = []
        self.site = site
        self.mode = mode

        for position, eligible_positions in SETTINGS[site].MODES.get(
                mode).get("POSITIONS").items():
            self.lineup_slots.append(
                LineupBuilderSlot(position,
                                  site,
                                  eligible_positions.get("ELIGIBLE_POSITIONS"),
                                  eligible_positions.get("PTS_MULTIPLIER"),
                                  eligible_positions.get("SALARY_MULTIPLIER"))
            )

        self.weighted_cost_map = self.create_weighted_cost_map_and_teams_set(draftables)
        self.lineups_builders = [LineupBuilder(site=site, draftables=draftables, weighted_cost_map=self.weighted_cost_map)]

    def get(self, position_title: str):
        return

    def build(self) -> List[Lineup]:
        return

    def with_composition_rule(self, position: str, num_players: int):
        for lineup in self.lineups:
            lineup.with_composition_rule(position, num_players)

    def with_punt_rule(self, position_title: str, max_salary: int = None):
        for lineup in self.lineups:
            lineup.with_punt_rule(position_title, max_salary)

    def with_stack_rule(self, team_abbr1: str, num_players1: int,
                        team_abbr2: str, num_players2: int):
        for lineup in self.lineups:
            lineup.with_stack_rule(team_abbr1, num_players1, team_abbr2, num_players2)
        return None
    
    # {"id": 9182983,
    #  "min_exposure": 5.4,
    #  "max_exposure": }
    def with_exposures(self, exposures: list):
        exposures.sort(key=lambda x: x.get("max_exposure"))
        # print(exposures)

    def create_weighted_cost_map_and_teams_set(self, draftables: list) -> dict:
        weighted_cost_map = {}

        for draftable in draftables:
            if draftable.get("status") in SETTINGS[self.site].INJURED_STATUSES:
                continue

            fantasy_points_per_game = 0.0 if (
                draftable.get("fppg") == "-") else (
                float(draftable.get("fppg", 0.0)))

            value = fantasy_points_per_game / int(draftable.get("salary"))
            draftable["value"] = value

            if draftable.get("position") not in weighted_cost_map.keys():
                weighted_cost_map[draftable["position"]] = [draftable]
            else:
                weighted_cost_map[draftable["position"]].append(draftable)

        for position in weighted_cost_map.keys():
            weighted_cost_map[position] = sorted(
                weighted_cost_map[position],
                key=lambda player: player.get("value"),
                reverse=True)

        return weighted_cost_map
