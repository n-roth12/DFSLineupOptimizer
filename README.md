# DFSLineupOptimizer [![n-roth12](https://circleci.com/gh/n-roth12/DFSLineupOptimizer.svg?style=shield)](https://app.circleci.com/pipelines/github/n-roth12/DFSLineupOptimizer)
A Python project for generating NFL daily fantasy contest lineups.

### Installation
#### As Package
To install and use as a Python package:
```
pip install lineup-optimizer
```
#### Repo
Clone the repository onto your machine to get started. Ensure you have Python and pip installed, then set up the virtual environment using:
```
pipenv install -r "requirements.txt"
pipenv shell
```
This project currently only uses built-in Python modules, so this step is actually not required.
### Usage
To generate an optimized lineup for a chosen DFS contest, go to the contest webpage and download the players list as a CSV, an option on almost all DFS sites. Then, place the CSV file into the root directory of the project. The examples below will use the name 'DKSalaries_example.csv' as a placeholder for one such CSV file.
You can choose to generate lineups from the command line, or from within a Python script:
#### Import Package
```
from lineup_optimizer import optimize_lineup

lineup = optimize_lineup('DRAFTKINGS', 'DKSalaries_example.csv')
print(lineup)
```
#### Command Line
```
python optimize.py DRAFTKINGS DKSalaries_example.csv
```
These will output the lineup to the console.
### About 
Lineups are able to be generated following certain constraints called "Tags". In addition, TagsController can confirm whether a given Lineup conforms 
to the rules of specific tags, as well as output the list of Tags that the Lineup conforms to. Examples of such Tags are: "Stack: 4x2", 
"Build: 3 RB", "Punt: TE".
