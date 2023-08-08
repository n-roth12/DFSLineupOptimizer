import csv


class DraftKingsParser:
    def __init__(self, csv_filepath: str):
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            rows = []
            for row in csv_reader:
                rows.append({
                    "position": row["Position"],
                    "name": row["Name"],
                    "id": row["ID"],
                    "roster_position": row["Roster Position"],
                    "salary": row["Salary"],
                    "game": row["Game Info"],
                    "team_abbr": row["TeamAbbrev"],
                    "avg_points": row["AvgPointsPerGame"]
                })
            self.players = rows
            self.player_count = len(rows)
