# Suduko-Kit
A highly efficient Sudoku solver written in Python.  
It uses a basic backtracking algorithm with a minimum-remaining-values heuristic. While the algorithm is simple, it's still extremely fast, and can solve any common puzzle in a few hundredths of a second.  

## Usage
Enter the known clues into a text file. Place each row on its own line, and use periods for blank spaces.  
(Examples of clue files are provided in the repository.)
Then, run  
```
python sudoku.py cluefilename.txt
```
