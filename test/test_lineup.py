import unittest
from lineup_optimizer.Lineup import Lineup


class TestLineupMethods(unittest.TestCase):
    def test_get_empty_lineup_as_list(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        for player in empty_draftkings_lineup.get_lineup_as_list():
            self.assertEqual({}, player)

    def test_get_empty_lineup_as_dict(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        lineup_dict = empty_draftkings_lineup.get_lineup_as_dict()
        for lineup_slot in list(lineup_dict.keys()):
            self.assertEqual({}, lineup_dict[lineup_slot])

    def test_is_slot_empty_empty_slot(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        for lineup_slot in self.get_all_draftkings_lineup_slots():
            self.assertTrue(empty_draftkings_lineup.is_slot_empty(lineup_slot))

    def test_has_empty_slots_empty_lineup(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertTrue(empty_draftkings_lineup.has_empty_slots()) 

    def test_get_empty_slots_empty_lineup(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        empty_lineup_slots = empty_draftkings_lineup.get_empty_slots()
        self.assertEqual(empty_lineup_slots, self.get_all_draftkings_lineup_slots())

    def test_get_lineup_proj_points_empty_lineup(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertEqual(0.0, empty_draftkings_lineup.get_lineup_projected_points())

    def test_get_lineup_salary_empty_lineup(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertEqual(0, empty_draftkings_lineup.get_lineup_salary())

    def test_get_player_ids_empty_lineup(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        player_ids = empty_draftkings_lineup.get_player_ids()
        self.assertEqual([], player_ids)

    def test_te_eligible_for_flex_slot_returns_true(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertTrue(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="TE", lineup_slot="FLEX"))

    def test_wr_eligible_for_flex_slot_returns_true(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertTrue(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="WR", lineup_slot="FLEX"))

    def test_qb_eligible_for_flex_slot_returns_false(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertFalse(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="QB", lineup_slot="FLEX"))

    def test_rb_eligible_for_rb2_slot_returns_true2(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertTrue(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="RB", lineup_slot="RB2"))

    def test_te_eligible_for_te_slot_returns_true3(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertTrue(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="TE", lineup_slot="TE"))

    def test_position_eligible_for_wr_slot_returns_false2(self):
        empty_draftkings_lineup = self.empty_draftkings_lineup()
        self.assertFalse(empty_draftkings_lineup.is_position_eligible_for_slot(
            position="WR", lineup_slot="RB"))

    def test_create_lineup_from_positions(self):
        lineup = self.empty_draftkings_lineup()
        self.assertDictEqual(lineup.lineup, {"QB": {}, "RB1": {}, "RB2": {}, "WR1": {},
                                             "WR2": {}, "WR3": {}, "TE": {}, "FLEX": {},
                                             "DST": {}})

    # HELPER METHODS #
    def empty_draftkings_lineup(self):
        return Lineup.create_lineup_with_positions(self.get_all_draftkings_lineup_slots(),
                                                   "DRAFTKINGS")

    def get_all_draftkings_lineup_slots(self):
        return ["QB", "RB1", "RB2", "WR1", "WR2", "WR3", "TE", "FLEX", "DST"]


if __name__ == "__main__":
    unittest.main()
