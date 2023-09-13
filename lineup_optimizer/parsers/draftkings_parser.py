import csv


class DraftKingsParser:
    SITE = "DRAFTKINGS"

    def __init__(self, csv_filepath: str):
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            rows = []
            for row in csv_reader:
                rows.append({
                    "position": row["Position"],
                    "name": row["Name"],
                    "id": row["ID"],
                    "salary": int(row["Salary"]),
                    "game": row["Game Info"].split(" ")[0],
                    "team_abbr": row["TeamAbbrev"],
                    "fppg": float(row["AvgPointsPerGame"]),
                    "status": ""
                })
            self.players = rows
            self.player_count = len(rows)
