# DFSLineupOptimizer [![n-roth12](https://circleci.com/gh/n-roth12/DFSLineupOptimizer.svg?style=shield)](https://app.circleci.com/pipelines/github/n-roth12/DFSLineupOptimizer)  [![PyPI version](https://badge.fury.io/py/lineup-optimizer.svg)](https://badge.fury.io/py/lineup-optimizer)
A Python project for generating NFL daily fantasy contest lineups.  

### Installation
#### As Package
To install and use as a Python package:
```
python3 -m pip install lineup-optimizer
```
### Support
This project supports the following NFL DFS formats:
| Site | Optimize Lineup | Generate Lineups | Export Lineups | 
| --- | --- | --- | -- |
| DraftKings Full Roster | ✔️ | ✔️ | ✔️ |
| FanDuel Full Roster | ✔️ | ✔️ | ✔️ |
| Yahoo Full Roster | ✔️ | ✔️ | ✔️ |
| DraftKings Captain | ✔️ | ✔️ | ✔️ |
| FanDuel MVP | ✔️ | ✔️ | ✔️ |
| Yahoo Captain | ✔️ | ✔️ | ✔️ |
#### Repo
Clone the repository onto your machine to get started. Ensure you have Python and pip installed, then set up the virtual environment using:
```
pipenv install -r "requirements.txt"
pipenv shell
```
This project currently only uses built-in Python modules, so this step is actually not required.
### Usage
Place the CSV file containing the player pool for the contest you would like to enter into the root directory of the project.   

DraftKings or FanDuel: Go to the contest webpage for the contest you would like to enter, or any contest that has the same player pool and format as the contest you would like to enter, and download the players list as a CSV.   

Yahoo: Go to the [Multiple Contest Entry Tool Page](https://sports.yahoo.com/dailyfantasy/contest/csv/create), and download the CSV template for your chosen contest type.   

The examples below will use the name "DKSalaries_example.csv" as a placeholder for one such CSV file.
You can choose to generate lineups from the command line, or from within a Python script:

#### Command Line
To create a single optimized lineup:
```
python optimize.py DRAFTKINGS "DKSalaries_example.csv"
```
This will output the lineup to the console:
```
QB: Jared Goff 
RB1: Austin Ekeler 
RB2: J.K. Dobbins 
WR1: Tutu Atwell 
WR2: Jakobi Meyers 
WR3: DeAndre Hopkins 
TE: Sam LaPorta 
FLEX: Evan Engram 
DST: Colts  
SALARY: 47700
```

To create a CSV file with multiple lineups:
```
python3 generate.py FULL_ROSTER 3 "FanDuel_full_roster_example.csv"
```
This will create a new file with 3 lineups in the directory with a name like "FANDUEL_FULL_ROSTER_export.csv".

#### Python Module  
You can also import the tool for use in your Python project:  
```
from lineup_optimizer import optimize_lineup

lineup = optimize_lineup("FULL_ROSTER", "DKSalaries_example.csv")
print(lineup)
```

