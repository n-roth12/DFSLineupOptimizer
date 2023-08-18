# DFSLineupOptimizer [![n-roth12](https://circleci.com/gh/n-roth12/DFSLineupOptimizer.svg?style=shield)](https://app.circleci.com/pipelines/github/n-roth12/DFSLineupOptimizer)
A Python project for generating NFL daily fantasy contest lineups.

### Installation
Clone the repository onto your machine to get started. Ensure you have Python and pip installed, then set up the virtual environment using:
```.
pipenv install -r "requirements.txt"
pipenv shell
```
This project currently only uses built-in Python modules, so this step is actually not required.
### Usage
To generate an optimized lineup for a chosen DFS contest, go to the contest webpage and download the players list as a CSV, which is an option on almost all DFS sites. Then, place the CSV file into the root directory of the project. You can then call `optimize` on that file, specifying the site. For example:
```
python optimize.py DRAFTKINGS DKSalaries.csv
```
This will output the lineup to the console. 
### About 
Lineups are able to be generated following certain constraints called "Tags". In addition, TagsController can confirm whether a given Lineup conforms 
to the rules of specific tags, as well as output the list of Tags that the Lineup conforms to. Examples of such Tags are: "Stack: 4x2", 
"Build: 3 RB", "Punt: TE".
