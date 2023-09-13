import unittest
from lineup_optimizer.parsers import parse_csv


class TestParser(unittest.TestCase):
    def test_draftkings_parser_full_roster(self):
        draftkings_parser = parse_csv(
            "test/test_csvs/DK_full_roster.csv")
        self.assertEqual(draftkings_parser.player_count, 770)
        self.assertEqual(len(draftkings_parser.players), 770)

    def test_draftkings_parser_captain(self):
        draftkings_parser = parse_csv(
            "test/test_csvs/DK_captain.csv")
        self.assertEqual(draftkings_parser.player_count, 148)
        self.assertEqual(len(draftkings_parser.players), 148)

    def test_fanduel_parser_full_roster(self):
        fanduel_parser = parse_csv(
            "test/test_csvs/FanDuel_mvp.csv"
        )
        self.assertEqual(fanduel_parser.player_count, 67)
        self.assertEqual(len(fanduel_parser.players), 67)

    def test_yahoo_parser_full_roster(self):
        yahoo_parser = parse_csv(
            "test/test_csvs/Yahoo_superstar.csv"
        )
        self.assertEqual(yahoo_parser.player_count, 60)
        self.assertEqual(len(yahoo_parser.players), 60)


if __name__ == "__main__":
    unittest.main()
