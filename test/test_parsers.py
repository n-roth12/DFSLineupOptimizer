import unittest
from lineup_optimizer.parsers import parse_csv


class TestParser(unittest.TestCase):
    def test_draftkings_parser(self):
        draftkings_parser = parse_csv('test/test_player_pools/DKSalaries (1).csv')
        self.assertEqual(draftkings_parser.player_count, 770)
        self.assertEqual(len(draftkings_parser.players), 770)

    def test_fanduel_parser(self):
        fanduel_parser = parse_csv(
            'test/test_player_pools/FanDuel-NFL-2023 ET-08 ET-10 ET-92650-players-list.csv'
        )
        self.assertEqual(fanduel_parser.player_count, 127)
        self.assertEqual(len(fanduel_parser.players), 127)

    def test_yahoo_parser(self):
        yahoo_parser = parse_csv(
            'test/test_player_pools/Yahoo_DF_player_export.csv'
        )
        self.assertEqual(yahoo_parser.player_count, 759)
        self.assertEqual(len(yahoo_parser.players), 759)


if __name__ == "__main__":
    unittest.main()
