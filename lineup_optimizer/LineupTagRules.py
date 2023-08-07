from lineup_optimizer.Lineup import Lineup

DRAFTKINGS_PUNT_PRICE = 4000
STACK_TYPES = [(3, 1), (3, 2), (4, 1), (4, 2), (4, 3),
               (5, 1), (3, 0), (4, 0), (2, 1), (5, 0)]
COMPOSITION_TYPES = [{"RB": 3}, {"WR": 4}, {"TE": 2}]


class LineupTagRules:
    def check_punt_rule(lineup: Lineup) -> tuple[bool, dict]:
        for player in lineup.lineup.values():
            if player.get("salary") < DRAFTKINGS_PUNT_PRICE:
                return True, player.get("position")
        return False, None

    def check_composition_rule(composition: dict, lineup: Lineup) -> bool:
        position_count = {}
        for player in lineup.lineup.values():
            if player and player.get("position"):
                if player.get("position") in position_count.keys():
                    position_count[player["position"]] += 1
                else:
                    position_count[player["position"]] = 1
        for position in composition.keys():
            if composition[position] != position_count[position]:
                return False
        return True

    def check_stack_rule(lineup: Lineup) -> list:
        stack_map = {}
        for player in [x for x in lineup.lineup.values() if x]:
            if player.get("game").get("gameId") not in stack_map.keys():
                stack_map[player.get("game").get("gameId")] = {
                    "homeTeam": {"team": player.get("game").get("homeTeam"),
                                 "players": [player] if (
                                    player.get("team") == player.get("game").get("homeTeam")
                                  ) else ([])
                                 },
                    "awayTeam": {"team": player.get("game").get("awayTeam"),
                                 "players": [player] if (
                                    player.get("team") == player.get("game").get("awayTeam")
                                 ) else []}
                }
            else:
                if player.get("team") == player.get("game").get("homeTeam"):
                    stack_map[player.get("game").get(
                        "gameId")]["homeTeam"]["players"].append(player)
                else:
                    stack_map[player.get("game").get(
                        "gameId")]["awayTeam"]["players"].append(player)
        result = []
        for gameId in stack_map.keys():
            players_larger = max(len(stack_map[gameId]["homeTeam"]["players"]),
                                 len(stack_map[gameId]["awayTeam"]["players"]))
            players_smaller = min(len(stack_map[gameId]["homeTeam"]["players"]),
                                  len(stack_map[gameId]["awayTeam"]["players"]))
            if (players_larger, players_smaller) in STACK_TYPES:
                result.append((players_larger, players_smaller))
        return result
