import unittest
from lineup_optimizer.Lineup import Lineup
from test.test_draftables import test_draftables
from lineup_optimizer.LineupTagRules import LineupTagRules


class TestTagsControllerMethods(unittest.TestCase):

    def test_all_tags(self):
        josh_allen = self.get_draftable_by_id(868199)
        stefon_diggs = self.get_draftable_by_id(694041)
        gabe_davis = self.get_draftable_by_id(976761)
        tyler_boyd = self.get_draftable_by_id(742387)
        george_kittle = self.get_draftable_by_id(733672)
        matt_breida = self.get_draftable_by_id(750097)
        giants = self.get_draftable_by_id(351)
        james_cook = self.get_draftable_by_id(1131012)
        tony_pollard = self.get_draftable_by_id(880398)
        lineup = Lineup(lineup={"QB": josh_allen, "RB1": james_cook, "RB2": tony_pollard,
                                "WR1": stefon_diggs, "WR2": gabe_davis, "WR3": tyler_boyd,
                                "TE": george_kittle, "FLEX": matt_breida, "DST": giants},
                        site="DRAFTKINGS")
        self.assertEqual((True, "DST"), LineupTagRules.check_punt_rule(lineup))
        self.assertTrue(LineupTagRules.check_composition_rule(composition={"RB": 3},
                        lineup=lineup))
        self.assertFalse(LineupTagRules.check_composition_rule(composition={"WR": 4},
                         lineup=lineup))
        self.assertEqual([(4, 1)], LineupTagRules.check_stack_rule(lineup))

# HELPER METHODS #
    def get_draftable_by_id(self, playerSiteId: int) -> dict:
        return next((player for player in test_draftables if (
            player.get("id") == playerSiteId)), None)


if __name__ == "__main__":
    unittest.main()
