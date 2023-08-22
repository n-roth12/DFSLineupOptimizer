from .draftkings import DraftKings
from .fanduel import FanDuel
from .yahoo import Yahoo

SITES = {
    DraftKings.NAME: DraftKings,
    FanDuel.NAME: FanDuel,
    Yahoo.NAME: Yahoo
}
