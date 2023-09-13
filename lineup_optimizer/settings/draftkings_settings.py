from .default_settings import DefaultSettings


class DraftKings(DefaultSettings):
    NAME = "DRAFTKINGS"
    MODES = {
        "FULL_ROSTER": {
            "SALARY_CAP": 50000,
            "POSITIONS": {
                "QB": {
                    "ELIGIBLE_POSITIONS": ["QB"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "RB1": {
                    "ELIGIBLE_POSITIONS": ["RB"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "RB2": {
                    "ELIGIBLE_POSITIONS": ["RB"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "WR1": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "WR2": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "WR3": {
                    "ELIGIBLE_POSITIONS": ["WR"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "TE": {
                    "ELIGIBLE_POSITIONS": ["TE"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "FLEX": {
                    "ELIGIBLE_POSITIONS": ["RB", "WR", "TE"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                },
                "DST": {
                    "ELIGIBLE_POSITIONS": ["DST"],
                    "SALARY_MULTIPLIER": 1,
                    "PTS_MULTIPLIER": 1
                }
            }
        },
        "MVP": {
            "SALARY_CAP": 50000,
            "POSITIONS": {
                "CPT": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DST"],
                    "SALARY_MULTIPLIER": 1.5,
                    "PTS_MULTIPLIER": 1.5
                },
                "FLEX1": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DST"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX2": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DST"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX3": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DST"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
                "FLEX4": {
                    "ELIGIBLE_POSITIONS": ["QB", "RB", "WR", "TE", "DST"],
                    "PTS_MULTIPLIER": 1,
                    "SALARY_MULTIPLIER": 1
                },
            }
        }
    }
