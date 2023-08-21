from .lineup_builder_slot import LineupBuilderSlot
from .lineup import Lineup
from .site_configs import SITES

from random import randint

STACK_ORDER = ["QB", "WR", "TE", "RB", "DST"]
NUM_PLAYERS_TO_CONSIDER = 10
NUM_OF_LINEUPS_TO_CONSIDER = 10


class LineupBuilder:

    def __init__(self, positions: list, site: str, draftables: list):
        self.lineup_slots = []
        self.site = site
        for position in positions:
            self.lineup_slots.append(LineupBuilderSlot(title=position, site=site))
        self.weighted_cost_map = self.create_weighted_cost_map(draftables)

    def get(self, position_title: str) -> LineupBuilderSlot:
        return next((lineup_slot for lineup_slot in self.lineup_slots if (
            lineup_slot.title == position_title)), None)

    def build(self) -> Lineup:
        lineup = {}
        lineup_ids = []
        for lineup_slot in self.lineup_slots:
            player = self.pick_player(
                position=self.pick_eligible_position(lineup_slot.eligible_positions),
                team_abbr=lineup_slot.eligible_team,
                max_salary=lineup_slot.max_salary,
                taken_ids=lineup_ids
            )
            lineup_ids.append(player.get("id"))
            lineup[lineup_slot.title] = player
        return Lineup(lineup=lineup, site=self.site)

    def fill(self, lineup: Lineup) -> Lineup:
        new_lineup = {}
        lineup_ids = lineup.get_player_ids()
        for lineup_slot in self.lineup_slots:
            if lineup.is_slot_empty(lineup_slot.title):
                player = self.pick_player(
                    position=self.pick_eligible_position(lineup_slot.eligible_positions),
                    taken_ids=lineup_ids
                )
                new_lineup[lineup_slot.title] = player
                lineup_ids.append(player.get("id"))
            else:
                new_lineup[lineup_slot.title] = lineup.get(lineup_slot.title)
        return Lineup(lineup=new_lineup, site=self.site)

    # for tested lineups, about a third of all generated lineups are over the salary cap
    # strictness should be an integer between 1 and 10
    def optimize(self, lineup: Lineup = {}, strictness: int = 5) -> Lineup:
        best_lineup_projection = 0.0
        best_lineup = None
        for i in range(NUM_OF_LINEUPS_TO_CONSIDER * (10 * strictness)):
            generated_lineup = self.fill(lineup=lineup)
            lineup_salary = generated_lineup.get_lineup_salary()
            lineup_projection = generated_lineup.get_lineup_projected_points()
            if (lineup_projection > best_lineup_projection
                    and lineup_salary <= SITES.get(self.site).SALARY_CAP):
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

    # first team with always get the QB, best to pass team with
    # more players first, could make wrapper method
    def with_stack_rule(self, team_abbr1: str, num_players1: int,
                        team_abbr2: str, num_players2: int):
        count1 = 0
        count2 = 0
        for lineup_slot in sorted(self.lineup_slots,
                                  key=lambda x:
                                  self.stack_order_helper(x.eligible_positions)):
            if count1 == num_players1 and count2 == num_players2:
                return self
            if count2 == num_players2:
                lineup_slot.set_eligible_team(team_abbr1)
                count1 += 1
            elif count1 == num_players1:
                lineup_slot.set_eligible_team(team_abbr2)
                count2 += 1
            else:
                # we first try to stack the first two players of
                # team1 before any players on team2
                if count1 > count2 + 1:
                    lineup_slot.set_eligible_team(team_abbr2)
                    count2 += 1
                else:
                    lineup_slot.set_eligible_team(team_abbr1)
                    count1 += 1
        if count1 == num_players1 and count2 == num_players2:
            return self
        return None

    def stack_order_helper(self, eligible_positions: list) -> int:
        return min([STACK_ORDER.index(pos) for pos in eligible_positions])

    def pick_eligible_position(self, eligible_positions: list) -> str:
        return eligible_positions[randint(0, len(eligible_positions) - 1)]

    def create_weighted_cost_map(self, draftables: list) -> dict:
        weighted_cost_map = {}
        for draftable in draftables:
            fantasy_points_per_game = 0.0 if (
                draftable.get("avg_points") == "-") else (
                float(draftable.get("avg_points", 0.0)))
            value = fantasy_points_per_game / int(draftable.get("salary"))
            draftable["value"] = value
            if draftable.get("position") not in weighted_cost_map.keys():
                weighted_cost_map[draftable["position"]] = [draftable]
            else:
                weighted_cost_map[draftable["position"]].append(draftable)
        for position in weighted_cost_map.keys():
            weighted_cost_map[position].sort(
                key=lambda player: player.get("value"), reverse=True)
        return weighted_cost_map

    def pick_player(self, position: str, taken_ids: list = [],
                    team_abbr: str = None, max_salary: int = None) -> dict:
        eligible_players = [player for player in self.weighted_cost_map[position] if (
            (team_abbr is None or player.get("team") == team_abbr)
            and (max_salary is None or player.get("salary") <= max_salary)
            and (player.get("status") not in SITES.get(self.site).INJURED_STATUSES)
            and (player.get("id") not in taken_ids)
        )]
        if not len(eligible_players):
            return None
        index_to_pick = randint(0, min(NUM_PLAYERS_TO_CONSIDER - 1,
                                len(eligible_players) - 1))
        return eligible_players[index_to_pick]
