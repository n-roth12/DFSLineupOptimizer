import csv


class FanduelParser:
    SITE = "FANDUEL"

    def __init__(self, csv_filepath):
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            rows = []
            for row in csv_reader:
                rows.append({
                    "position": row["Position"],
                    "name": row["Nickname"],
                    "id": row["Id"],
                    "salary": int(row["Salary"]),
                    "game": row["Game"],
                    "team_abbr": row["Team"],
                    "fppg": float(row["FPPG"]) if row["FPPG"] else 0.0,
                    "status": row["Injury Indicator"]
                })
            self.players = rows
            self.player_count = len(rows)
