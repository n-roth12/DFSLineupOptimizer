from .draftkings_settings import DraftKings
from .fanduel_settings import FanDuel
from .yahoo_settings import Yahoo

SITES = {
    DraftKings.NAME: DraftKings,
    FanDuel.NAME: FanDuel,
    Yahoo.NAME: Yahoo
}
