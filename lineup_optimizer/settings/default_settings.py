class DefaultSettings:
    INJURED_STATUSES = ["IR", "O", "SUSP", "PUP", "NA", "D"]

    # exclustion constant refers to the top percent of players that we wish
    # to consider for lineups if they are sorted by salary. Any players not
    # above this percentile will not be considered
    EXCLUSION_CONSTANTS = {"QB": 0.3, "DEFAULT": 0.3, "RB": 0.4, "TE": 0.2,
                           "DST": 1, "D": 1, "DEF": 1, "K": 1}
