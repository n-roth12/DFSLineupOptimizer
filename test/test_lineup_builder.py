import unittest
from lineup_optimizer.LineupBuilder import LineupBuilder
from test.test_draftables import test_draftables
from lineup_optimizer.Lineup import Lineup


class LineupBuilderTests(unittest.TestCase):

    def test_lineup_builder_get(self):
        lineup_builder = LineupBuilder(positions=["QB", "RB1", "RB2", "WR1",
                                                  "WR2", "WR3", "TE", "FLEX", "DST"],
                                       site="DRAFTKINGS",
                                       draftables=test_draftables)
        self.assertIsNone(lineup_builder.get("TE2"))
        self.assertTrue(lineup_builder.get("WR3").title == "WR3")

    def test_with_punt_rule(self):
        lineup_builder = LineupBuilder(positions=["QB", "RB1", "RB2", "WR1",
                                                  "WR2", "WR3", "TE", "FLEX", "DST"],
                                       site="DRAFTKINGS",
                                       draftables=test_draftables) \
            .with_punt_rule("TE", 4000) \
            .with_punt_rule("WR2", 3500)
        self.assertEqual(4000, lineup_builder.get("TE").max_salary)
        self.assertEqual(3500, lineup_builder.get("WR2").max_salary)

    def test_with_valid_composition_rule(self):
        lineup_builder = self.default_draftkings_builder().with_composition_rule(
            position="RB", num_players=3)
        self.assertEqual(["RB"], lineup_builder.get("FLEX").eligible_positions)
        lineup_builder = self.default_draftkings_builder().with_composition_rule(
            position="WR", num_players=4)
        self.assertEqual(["WR"], lineup_builder.get("FLEX").eligible_positions)
        lineup_builder = self.default_draftkings_builder().with_composition_rule(
            position="TE", num_players=2)
        self.assertEqual(["TE"], lineup_builder.get("FLEX").eligible_positions)

    def test_with_invalid_composition_rule(self):
        self.assertIsNone(self.default_draftkings_builder().with_composition_rule(
            position="RB", num_players=4))
        self.assertIsNone(self.default_draftkings_builder().with_composition_rule(
            position="WR", num_players=5))
        self.assertIsNone(self.default_draftkings_builder().with_composition_rule(
            position="TE", num_players=3))
        self.assertIsNone(self.default_draftkings_builder().with_composition_rule(
            position="QB", num_players=2))

    def test_with_valid_stack_rule_3_1(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 3, "JAX", 1)
        self.assertTrue(lineup_builder.get("QB").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR1").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR2").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("WR3").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("FLEX").eligible_team is None)

    def test_with_valid_stack_rule_1_3(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 1, "JAX", 3)
        self.assertTrue(lineup_builder.get("QB").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR1").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("WR2").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("WR3").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("FLEX").eligible_team is None)

    def test_with_valid_stack_rule_2_2(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 2, "JAX", 2)
        self.assertTrue(lineup_builder.get("QB").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR1").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR2").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("WR3").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("FLEX").eligible_team is None)

    def test_with_valid_stack_rule_3_0(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 3, "JAX", 0)
        self.assertTrue(lineup_builder.get("QB").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR1").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR2").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR3").eligible_team is None)

    def test_with_valid_stack_rule_4_3(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 4, "JAX", 3)
        self.assertTrue(lineup_builder.get("QB").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR1").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("WR2").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("WR3").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("FLEX").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("TE").eligible_team == "KC")
        self.assertTrue(lineup_builder.get("RB1").eligible_team == "JAX")
        self.assertTrue(lineup_builder.get("RB2").eligible_team is None)

    def test_with_valid_stack_rule_0_0(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 0, "JAX", 0)
        self.assertTrue(lineup_builder.get("QB").eligible_team is None)

    def test_with_invalid_stack_rule_5_5(self):
        lineup_builder = self.default_draftkings_builder().with_stack_rule(
            "KC", 5, "JAX", 5)
        self.assertIsNone(lineup_builder)

    def test_pick_valid_player_1(self):
        lineup_builder = self.default_draftkings_builder()
        player = lineup_builder.pick_player(position="WR",
                                            team_abbr="JAX", max_salary=4000)
        self.assertEqual("WR", player.get("position"))
        self.assertEqual("JAX", player.get("team"))
        self.assertGreaterEqual(4000, player.get("salary"))

    def test_pick_valid_player_2(self):
        lineup_builder = self.default_draftkings_builder()
        player = lineup_builder.pick_player(position="TE", team_abbr="KC")
        self.assertEqual("TE", player.get("position"))
        self.assertEqual("KC", player.get("team"))

    def test_pick_valid_player_3(self):
        lineup_builder = self.default_draftkings_builder()
        player = lineup_builder.pick_player(position="RB")
        self.assertEqual("RB", player.get("position"))

    def test_pick_invalid_player(self):
        self.assertIsNone(self.default_draftkings_builder().pick_player(
            position="WR", team_abbr="KI", max_salary=4000))

    def test_build(self):
        lineup = self.default_draftkings_builder().build()
        self.assertEqual(0, len(lineup.get_empty_slots()))

    def test_build_1(self):
        lineup = self.default_draftkings_builder() \
            .with_stack_rule("KC", 5, "JAX", 4) \
            .with_composition_rule("RB", 3) \
            .with_punt_rule("TE", 3700) \
            .build()
        self.assertEqual("KC", lineup.get("QB")["team"])
        self.assertEqual("KC", lineup.get("WR1")["team"])
        self.assertEqual("JAX", lineup.get("WR2")["team"])
        self.assertEqual("KC", lineup.get("WR3")["team"])
        self.assertEqual("JAX", lineup.get("FLEX")["team"])
        self.assertEqual("KC", lineup.get("TE")["team"])
        self.assertEqual("JAX", lineup.get("RB1")["team"])
        self.assertEqual("KC", lineup.get("RB2")["team"])
        self.assertEqual("JAX", lineup.get("DST")["team"])
        self.assertEqual("RB", lineup.get("FLEX")["position"])
        self.assertGreaterEqual(3700, lineup.get("TE")["salary"])

    def test_fill_empty_lineup_with_positions(self):
        empty_lineup = self.empty_lineup()
        lineup = self.default_draftkings_builder().fill(empty_lineup)
        self.assertEqual(0, len(lineup.get_empty_slots()))

    def test_fill_empty_lineup_without_positions(self):
        lineup = self.default_draftkings_builder().fill(Lineup(lineup={},
                                                        site="DRAFTKINGS"))
        self.assertEqual(0, len(lineup.get_empty_slots()))

    def test_fill_non_empty_lineup_1(self):
        empty_lineup = self.empty_lineup()
        builder = self.default_draftkings_builder()
        player1 = builder.pick_player(position="WR")
        empty_lineup.add_player_at_position(lineup_slot="WR2", player=player1)
        lineup = builder.fill(empty_lineup)
        self.assertEqual(player1, lineup.get("WR2"))

    def test_fill_non_empty_lineup_2(self):
        builder = self.default_draftkings_builder()
        player1 = builder.pick_player(position="QB")
        player2 = builder.pick_player(position="RB")
        player3 = builder.pick_player(position="WR")
        player4 = builder.pick_player(position="TE")
        player5 = builder.pick_player(position="DST")
        lineup = Lineup(lineup={"QB": player1, "RB1": player2, "WR1": player3,
                                "TE": player4, "DST": player5}, site="DRAFTKINGS")
        result = builder.fill(lineup=lineup)
        self.assertEqual(player1, result.get("QB"))
        self.assertEqual(player2, result.get("RB1"))
        self.assertEqual(player3, result.get("WR1"))
        self.assertEqual(player4, result.get("TE"))
        self.assertEqual(player5, result.get("DST"))
        self.assertEqual(0, len(result.get_empty_slots()))
        self.assertEqual(["QB", "RB1", "RB2", "WR1", "WR2", "WR3", "TE", "FLEX", "DST"],
                         list(result.lineup.keys()))

    # this will fail a rare number of times of the time because optimize() is not
    # deterministic, it is not gauranteed that a lineup under the salary cap will
    # be found within 100 tries
    def test_optimizer(self):
        empty_lineup = self.empty_lineup()
        lineup = self.default_draftkings_builder().optimize(empty_lineup, strictness=1)
        self.assertEqual(["QB", "RB1", "RB2", "WR1", "WR2", "WR3", "TE", "FLEX", "DST"],
                         list(lineup.lineup.keys()))

    def default_draftkings_builder(self):
        return LineupBuilder(positions=["QB", "RB1", "RB2", "WR1", "WR2",
                                        "WR3", "TE", "FLEX", "DST"],
                             site="DRAFTKINGS", draftables=test_draftables)

    def empty_lineup(self):
        return Lineup({"QB": {}, "RB1": {}, "RB2": {}, "WR1": {}, "WR2": {},
                       "WR3": {}, "TE": {}, "FLEX": {}, "DST": {}},
                      site="DRAFTKINGS")
