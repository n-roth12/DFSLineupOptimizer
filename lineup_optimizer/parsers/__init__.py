from .draftkings_parser import DraftKingsParser
from .fanduel_parser import FanduelParser
from .yahoo_parser import YahooParser

PARSERS = {
    DraftKingsParser.SITE: DraftKingsParser,
    FanduelParser.SITE: FanduelParser,
    YahooParser.SITE: YahooParser
}


def get_site_from_filepath(filepath: str) -> str:
    filepath = filepath.split("/")[-1]
    if filepath.startswith("DK"):
        return DraftKingsParser.SITE
    if filepath.startswith("FanDuel"):
        return FanduelParser.SITE
    if filepath.startswith("Yahoo"):
        return YahooParser.SITE


def parse_csv(filepath: str):
    site = get_site_from_filepath(filepath)
    if site not in PARSERS.keys():
        print("Error: Unable to identify site from CSV. \
              Do not change CSV filename before uploading.")
    return PARSERS[site](filepath)
