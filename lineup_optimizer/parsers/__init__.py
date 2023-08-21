from .draftkings_parser import DraftKingsParser
from .fanduel_parser import FanduelParser


def parse_csv(filepath: str):
    filename = filepath.split('/')[-1]
    if filename.startswith('DK'):
        return DraftKingsParser(filepath)
    if filename.startswith('FanDuel'):
        return FanduelParser(filepath)
