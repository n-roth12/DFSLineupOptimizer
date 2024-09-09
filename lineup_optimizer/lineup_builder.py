from typing import List, Set
from .lineup_builder_slot import LineupBuilderSlot
from .lineup import Lineup
from .settings import SETTINGS

from random import randint
from math import floor

STACK_ORDER = ["QB", "WR", "TE", "RB", "DST"]


class LineupBuilder:

    def __init__(self, site: str,
                 draftables: list, mode: str = "FULL_ROSTER", weighted_cost_map: dict = {}):
        self.lineup_slots: List[LineupBuilderSlot] = []
        self.site: str = site
        self.mode: str = mode
        self.teams: Set[str] = set([])

        for position, eligible_positions in SETTINGS[site].MODES.get(
                mode).get("POSITIONS").items():
            self.lineup_slots.append(
                LineupBuilderSlot(position,
                                  site,
                                  eligible_positions.get("ELIGIBLE_POSITIONS"),
                                  eligible_positions.get("PTS_MULTIPLIER"),
                                  eligible_positions.get("SALARY_MULTIPLIER"))
            )
        if len(weighted_cost_map) == 0:
            self.create_weighted_cost_map_and_teams_set(draftables)
        else:
            self.weighted_cost_map = weighted_cost_map

    def get(self, position_title: str) -> LineupBuilderSlot:
        return next((lineup_slot for lineup_slot in self.lineup_slots if (
            lineup_slot.title == position_title)), None)

    def build(self) -> Lineup:
        lineup = {}
        lineup_ids = []

        for lineup_slot in self.lineup_slots:
            player = None
            for i in range(10):
                position = self.pick_eligible_position(
                    lineup_slot.eligible_positions)
                player = self.pick_player(
                    position=position,
                    eligible_teams=lineup_slot.eligible_teams,
                    max_salary=lineup_slot.max_salary,
                    taken_ids=lineup_ids,
                    pts_multiplier=lineup_slot.pts_multiplier,
                    salary_multiplier=lineup_slot.salary_multiplier
                )
                if player:
                    lineup_ids.append(player.get("id"))
                    lineup[lineup_slot.title] = player
                    break

        return Lineup(lineup=lineup, site=self.site, mode=self.mode)

    def fill(self, lineup: Lineup) -> Lineup:
        new_lineup = {}
        lineup_ids = lineup.get_player_ids()

        for lineup_slot in self.lineup_slots:
            position = self.pick_eligible_position(
                lineup_slot.eligible_positions
            )
            if lineup.is_slot_empty(lineup_slot.title):
                player = self.pick_player(
                    position=position,
                    taken_ids=lineup_ids
                )
                new_lineup[lineup_slot.title] = player
                lineup_ids.append(player.get("id"))
            else:
                new_lineup[lineup_slot.title] = lineup.get(lineup_slot.title)

        return Lineup(lineup=new_lineup, site=self.site, mode=self.mode)

    # for tested lineups, about a third of all generated lineups are over the salary cap
    # strictness should be an integer between 1 and 10
    def optimize(self, lineup: Lineup = {}, strictness: int = 10) -> Lineup:
        best_lineup_projection = float('-inf')
        best_lineup = None

        for i in range(10 * strictness):
            generated_lineup = self.fill(lineup=lineup)
            lineup_salary = generated_lineup.get_lineup_salary()
            lineup_projection = generated_lineup.get_lineup_projected_points()

            if (lineup_projection > best_lineup_projection
                    and lineup_salary <= SETTINGS[self.site].MODES.get(
                        self.mode).get("SALARY_CAP")):
                best_lineup = generated_lineup
                best_lineup_projection = lineup_projection

        return best_lineup

    def with_composition_rule(self, position: str, num_players: int):
        count = 0

        for slot in self.lineup_slots:
            if position in slot.eligible_positions:
                count += 1
                if len(slot.eligible_positions) > 1:
                    slot.eligible_positions = [position]
                if count >= num_players:
                    return self

        return None

    def with_punt_rule(self, position_title: str, max_salary: int = None):
        lineup_slot = self.get(position_title)
        if not lineup_slot:
            return None
        lineup_slot.set_max_salary(max_salary)
        return self

    def with_stack_rule(self, team_abbr1: str, num_players1: int,
                        team_abbr2: str, num_players2: int):
        count1 = 0
        count2 = 0

        for lineup_slot in sorted(self.lineup_slots,
                                  key=lambda x:
                                  self.stack_order_helper(x.eligible_positions)):
            if count1 == num_players1 and count2 == num_players2:
                lineup_slot.set_eligible_teams(
                    [team for team in self.teams if (team != team_abbr1 and team != team_abbr2)])

            elif count2 == num_players2:
                lineup_slot.set_eligible_teams([team_abbr1])
                count1 += 1
            elif count1 == num_players1:
                lineup_slot.set_eligible_teams([team_abbr2])
                count2 += 1
            else:
                # we first try to stack the first two players of
                # team1 before any players on team2
                if count1 > count2 + 1:
                    lineup_slot.set_eligible_teams([team_abbr2])
                    count2 += 1
                else:
                    lineup_slot.set_eligible_teams([team_abbr1])
                    count1 += 1

        if count1 == num_players1 and count2 == num_players2:
            return self
        print("fail")
        return None

    def stack_order_helper(self, eligible_positions: list) -> int:
        return min([STACK_ORDER.index(pos) for pos in eligible_positions])

    def pick_eligible_position(self, eligible_positions: list) -> str:
        t = randint(0, len(eligible_positions) - 1)
        return eligible_positions[t]

    def create_weighted_cost_map_and_teams_set(self, draftables: list) -> None:
        weighted_cost_map = {}
        teams_set = set([])

        for draftable in draftables:
            if draftable.get("status") in SETTINGS[self.site].INJURED_STATUSES:
                continue

            teams_set.add(draftable.get("team_abbr"))

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

        self.weighted_cost_map = weighted_cost_map
        self.teams = teams_set

    def pick_player(self, position: str, taken_ids: list = [],
                    eligible_teams: List[str] = [], max_salary: int = None,
                    pts_multiplier: float = 1.0,
                    salary_multiplier: float = 1.0) -> dict:
        eligible_players = [player for player in self.weighted_cost_map[position] if (
            (len(eligible_teams) < 1 or player.get("team_abbr") in eligible_teams)
            and (max_salary is None or player.get("salary") <= max_salary)
            and (player.get("id") not in taken_ids)
        )]
        eligible_players = eligible_players[
            :min(len(eligible_players),
                 self.nth_pos_percentile(position, len(eligible_players)))]

        if not len(eligible_players):
            return None
        index_to_pick = randint(0, len(eligible_players) - 1)

        return eligible_players[index_to_pick]

    def nth_pos_percentile(self, pos: str, num_players: int):
        if pos in SETTINGS[self.site].EXCLUSION_CONSTANTS.keys():
            return max(1, floor(SETTINGS[self.site].EXCLUSION_CONSTANTS[pos] * num_players))
        return max(1, floor(SETTINGS[self.site].EXCLUSION_CONSTANTS["DEFAULT"] * num_players))
