from .DraftKingsParser import DraftKingsParser
from .FanduelParser import FanduelParser


def parse_csv(filepath: str):
    filename = filepath.split('/')[-1]
    if filename.startswith('DK'):
        return DraftKingsParser(filepath)
    if filename.startswith('FanDuel'):
        return FanduelParser(filepath)
