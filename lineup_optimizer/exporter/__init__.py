from .exporter import LineupExporter


def export_lineups(site: str, mode: str, lineups: list):
    LineupExporter.export(site, mode, lineups)
