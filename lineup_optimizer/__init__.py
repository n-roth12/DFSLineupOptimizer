from lineup_optimizer.site_configs.draftkings import DraftKings
from lineup_optimizer.site_configs.fanduel import FanDuel

SITES = {
    DraftKings.NAME: DraftKings,
    FanDuel.NAME: FanDuel
}


def parse(filename):
    pass


def optimize(site, player_pool):
    pass
