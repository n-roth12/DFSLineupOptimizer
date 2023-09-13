import csv


class YahooParser:
    SITE = "YAHOO"

    def __init__(self, csv_filepath):
        with open(csv_filepath) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            rows = []
            for row in csv_reader:
                if row["ID"].strip():
                    rows.append({
                        "position": row["Position"],
                        "name": f'{row["First Name"]} {row["Last Name"]}',
                        "id": row["ID"],
                        "salary": int(row["Salary"]),
                        "game": row["Game"],
                        "team_abbr": row["Team"],
                        "fppg": float(row["FPPG"]),
                        "status": row["Injury Status"] if len(row["Injury Status"]) else None
                    })
            self.players = rows
            self.player_count = len(rows)
