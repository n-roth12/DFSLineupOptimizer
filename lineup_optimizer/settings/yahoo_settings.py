from .default_settings import DefaultSettings


class Yahoo(DefaultSettings):
    NAME = "YAHOO"
    MODES = {
        "FULL_ROSTER": {
            "SALARY_CAP": 200,
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
                    "SALARY_MULTIPLIER": 1
                },
                "WR2": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "WR3": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
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
                "DEF": {
                    "ELIGIBLE_POSITIONS": ["DEF"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                }
            }
        },
        "MVP": {
            "SALARY_CAP": 125,
            "POSITIONS": {
                "CPT": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DEF"],
                    "PTS_MULTIPLIER": 1.5,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX1": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DEF"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX2": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DEF"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX3": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DEF"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX4": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DEF"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                }
            }
        }
    }
