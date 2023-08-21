import csv


class FanduelParser:
    def __init__(self, csv_filepath):
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            rows = []
            for row in csv_reader:
                rows.append({
                    "position": row["Position"],
                    "name": row["Nickname"],
                    "id": row["Id"],
                    "roster_position": row["Roster Position"],
                    "salary": row["Salary"],
                    "game": row["Game"],
                    "team_abbr": row["Team"],
                    "avg_points": row["FPPG"]
                })
            self.players = rows
            self.player_count = len(rows)
