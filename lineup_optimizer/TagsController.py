from lineup_optimizer.LineupTagRules import LineupTagRules
from lineup_optimizer.Lineup import Lineup

DRAFTKINGS_PUNT_PRICE = 4000
STACK_TYPES = [(3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1),
               (3, 0), (4, 0), (2, 1), (5, 0)]
COMPOSITION_TYPES = [{"RB": 3}, {"WR": 4}, {"TE": 2}]


class TagsController:
    def get_recommended_tags(lineup: Lineup) -> list:
        result_tags = []
        punt_rule_result = LineupTagRules.check_punt_rule(lineup)
        if punt_rule_result[0]:
            result_tags.append({"category": "Punt", "value": punt_rule_result[1]})
        for composition in COMPOSITION_TYPES:
            if LineupTagRules.check_composition_rule(composition=composition,
                                                     lineup=lineup):
                result_tags.append(
                    {"category": "Build",
                     "value": f"{list(composition.values())[0]} {list(composition.keys())[0]}"}
                )
        stack_rule_result = LineupTagRules.check_stack_rule(lineup)
        if stack_rule_result:
            for stack in stack_rule_result:
                result_tags.append({"category": "Stack", "value": f"{stack[0]}x{stack[1]}"})
        return result_tags
