import unittest
from lineup_optimizer.multi_lineup_builder import MultiLineupBuilder
from .draftkings_draftables import draftkings_draftables


class LineupBuilderTests(unittest.TestCase):
    def test_with_exposures(self):
        multi_lineup_builder = MultiLineupBuilder(num_lineups=1, site="DRAFTKINGS",
                                                  draftables=draftkings_draftables).with_exposures([{
                                                      "id": "28792273",
                                                      "min_exposure": 100,
                                                      "max_exposure": 100
                                                  }, {
                                                      "id": "28792613",
                                                      "min_exposure": 0,
                                                      "max_exposure": 0
                                                  }, {
                                                      "id": "28792339",
                                                      "min_exposure": 0,
                                                      "max_exposure": 50
                                                  }])
