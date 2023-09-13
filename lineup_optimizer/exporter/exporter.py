import csv
from lineup_optimizer import SETTINGS


class LineupExporter:
    def export(site: str, mode: str, lineups: list):
        cols = SETTINGS[site].MODES.get(mode).get("CSV_COLS")
        filename = f"{site}_{mode}_export.csv"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(cols)
            for lineup in lineups:
                ids = [player.get("id") for player in lineup.values()]
                if site == "YAHOO":
                    ids.insert(0, "989821")
                csvwriter.writerow(ids)
