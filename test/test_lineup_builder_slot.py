import unittest
from lineup_optimizer.LineupBuilderSlot import LineupBuilderSlot


class LineupBuilderSlotTests(unittest.TestCase):
    def test_default_position(self):
        self.assertEqual(["WR"],
                         LineupBuilderSlot("WR2", "DRAFTKINGS").eligible_positions)
        self.assertEqual(["RB", "WR", "TE"],
                         LineupBuilderSlot("FLEX", "DRAFTKINGS").eligible_positions)
