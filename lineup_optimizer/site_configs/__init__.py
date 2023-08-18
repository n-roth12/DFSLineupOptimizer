from .draftkings import DraftKings
from .fanduel import FanDuel

SITES = {
    DraftKings.NAME: DraftKings,
    FanDuel.NAME: FanDuel
}