# N-Queens
N-Queens is a command line program that implements backtracking to solve the N-Queens puzzle.
This program scales to any inputed board size and solves for either the first solution found
or every solution for that board size.

## Installation
Clone the respository and make sure you have Python3 installed on your computer.
```bash
git clone https://github.com/DSSzymanski/N-Queens.git
```

## Usage
This program is written as a module. Import the file and there are 2 main commands that can
be run to view the solutions.

```
from Main import all_solutions, find_solutions

#find a singular solution
find_solution(4)

#find all solutions
all_solutions(4)
```

find_solution() takes an integer n as an input which represents an nxn sized chess board.
This will either return the first found solution to the nxn sized board or a statement
saying there are no valid solutions to a board of size nxn.

all_solutions() does the same as find_solutions, but will return all the valid solutions
to an nxn sized chess board.

## Credits
Made exclusively by [Daniel Szymanski](https://github.com/DSSzymanski).

## License
[MIT](https://choosealicense.com/licenses/mit/)
