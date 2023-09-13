from .settings import SETTINGS


class Lineup:

    def __init__(self, lineup: dict, site: str, mode: str = "FULL_ROSTER") -> None:
        self.lineup = lineup
        self.player_ids = self.get_player_ids()
        self.site = site
        self.mode = mode
        self.allows_duplicates = False

    def __str__(self) -> str:
        result = ""
        for key in self.lineup.keys():
            result += f"{key}: {self.lineup.get(key).get('name')} \n"
        result += f"SALARY: {str(self.get_lineup_salary())}"
        return result

    def get(self, lineup_slot: str):
        return self.lineup.get(lineup_slot)

    def get_lineup_as_list(self) -> list:
        return [player for player in self.lineup.values()]

    def get_lineup_as_dict(self) -> dict:
        return self.lineup

    def get_site(self) -> str:
        return self.site

    def get_lineup_projected_points(self) -> float:
        points_sum = 0
        for pos, player in self.lineup.items():
            if player:
                points_sum += 0.0 if (
                    player.get("fppg") == "-" or not player.get("fppg")
                ) else (
                    SETTINGS[self.site].MODES[self.mode]["POSITIONS"].get(pos).get("PTS_MULTIPLIER") * float(player.get("fppg"))
                )

        return points_sum

    def get_lineup_salary(self) -> int:
        salary_sum = 0
        for player in self.lineup.values():
            if player and player.get("salary"):
                salary_sum += player.get("salary")

        return salary_sum

    def get_player_ids(self) -> list:
        return [self.lineup.get(lineup_slot).get("playerSiteId") for lineup_slot in
                list(self.lineup.keys()) if self.lineup.get(lineup_slot)]

    def get_empty_slots(self) -> list:
        return [position for position in self.lineup.keys() if (
            self.is_slot_empty(position))]

    def has_empty_slots(self) -> bool:
        return len(self.get_empty_slots()) > 1

    def is_slot_empty(self, lineup_slot: str) -> bool:
        player = self.lineup.get(lineup_slot)
        if not player:
            return True
        return (len(player.keys()) < 1)

    def add_player_at_position(self, lineup_slot: str, player: dict) -> bool:
        if player.get("playerSiteId") in self.player_ids:
            return False
        if self.is_position_eligible_for_slot(
            lineup_slot=lineup_slot,
            position=player.get("position")
        ):
            self.lineup[lineup_slot] = player
            self.player_ids.append(player.get("playerSiteId"))
            return True

        return False

    def add_players(self, players: list) -> bool:
        eligible_positions = [x for x in self.lineup.keys()]
        for player in players:
            eligible_positions.remove(self.add_player(
                player=player, eligible_positions=eligible_positions
            ))

    def add_player(self, player: dict, eligible_positions: list = None) -> str:
        if not eligible_positions:
            eligible_positions = self.lineup.keys()

        for lineup_slot in eligible_positions:
            if self.is_position_eligible_for_slot(
                lineup_slot=lineup_slot, position=player.get("position")
            ):
                self.add_player_at_position(lineup_slot=lineup_slot, player=player)
                return lineup_slot

        return None

    def is_position_eligible_for_slot(self, lineup_slot: str, position: str) -> bool:
        return position in SETTINGS[self.site].MODES[self.mode]["POSITIONS"].get(
            lineup_slot).get("ELIGIBLE_POSITIONS")
