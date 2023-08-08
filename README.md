# DFSLineupOptimizer ![(build status)](https://github.com/n-roth12/DFSLineupOptimizer/actions/workflows/python-app.yml/badge.svg)
A Python project for generating NFL daily fantasy contest lineups.

### Getting Started
Provided that you have Python installed on your system, all that's needed to get started is to navigate to the root directory ```/LineupOptimizer``` 
and run a test file, for example: ```python -m unittest tests/LineupBuilderTests.py```. You may choose to run the project inside of a virtual
environment, with:
```. 
pipenv shell
pipenv install -r "requirements.txt"
pipenv run python -m unittest tests/LineupBuilderTests.py 
```

### About 
The file ```tests/test_draftables.py``` includes a sample of players from a DraftKings DFS slate to get you started. This is also the file used 
in all the tests. If you would like to use a different set of players, please alter your file to follow the format of the list in 
```test_draftables.py```, otherwise the optimizer will not work.

Lineups are able to be generated following certain constraints called "Tags". In addition, TagsController can confirm whether a given Lineup conforms 
to the rules of specific tags, as well as ouput the list of Tags that the Lineup conforms to. Examples of such Tags are: "Stack: 4x2", 
"Build: 3 RB", "Punt: TE".
