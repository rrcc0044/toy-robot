# Toy Robot Simulator

### Assumptions
  - Initial Coordinates will never be out of the 5x5 table
  - Commands are either PLACE, MOVE, LEFT, RIGHT, REPORT.
  - Inputs are from standard input

### Installation

Toy Robot Simulator requires [Python](https://www.python.org/) v3+ and [Pipenv](https://github.com/pypa/pipenv) to run.

Install the dependencies and dev dependencies then activate the virtual shell.

```sh
$ cd toy-robot
$ pipenv install --dev
$ pipenv shell
(toy-robot-xxxx) $ python3 robot.py
Enter command:
```

### Running Tests

Toy Robot Simulator uses [Pytest](https://docs.pytest.org/en/latest/) to run the test suites

Inside the virtual shell

```sh
(toy-robot-xxxx) $ pytest 
```
