import unittest
from parsers import parse_csv


class TestParser(unittest.TestCase):
    def test_draftkings_parser(self):
        draftkings_parser = parse_csv('tests/test_player_pools/DKSalaries (1).csv')
        self.assertEqual(draftkings_parser.player_count, 770)
        self.assertEqual(len(draftkings_parser.players), 770)

    def test_fanduel_parser(self):
        fanduel_parser = parse_csv(
            'tests/test_player_pools/FanDuel-NFL-2023 ET-08 ET-10 ET-92650-players-list.csv'
        )
        self.assertEqual(fanduel_parser.player_count, 127)
        self.assertEqual(len(fanduel_parser.players), 127)


if __name__ == "__main__":
    unittest.main()
