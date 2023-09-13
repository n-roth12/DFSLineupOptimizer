from .default_settings import DefaultSettings


class FanDuel(DefaultSettings):
    NAME = "FANDUEL"
    MODES = {
        "FULL_ROSTER": {
            "SALARY_CAP": 60000,
            "CSV_COLS": ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DEF"],
            "POSITIONS": {
                "QB": {
                    "ELIGIBLE_POSITIONS": ["QB"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "RB1": {
                    "ELIGIBLE_POSITIONS": ["RB"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "RB2": {
                    "ELIGIBLE_POSITIONS": ["RB"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "WR1": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTPLIER": 1
                },
                "WR2": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "WR3": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MUTLIPLIER": 1
                },
                "TE": {
                    "ELIGIBLE_POSITIONS": ["TE"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX": {
                    "ELIGIBLE_POSITIONS": ["RB", "WR", "TE"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "D": {
                    "ELIGIBLE_POSITIONS": ["D"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                }
            }
        },
        "MVP": {
            "SALARY_CAP": 60000,
            "POSITIONS": {
                "MVP - 1.5X Points": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "D"],
                    "PTS_MULTIPLIER": 1.5,
                    "SALARY_MULTIPLIER": 1
                },
                "AnyFLEX1": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "D"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "AnyFLEX2": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "D"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "AnyFLEX3": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "D"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "AnyFLEX4": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "D"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
            }
        }
    }
