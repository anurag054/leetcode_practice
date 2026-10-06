# VALID SUDOKU   (`MEDIUM`)
## QUESTION:
Determine if a `9 x 9` Sudoku board is `valid`. Only the `filled` cells need to be `validated` according to the following rules:

- Each row must contain the digits `1-9` without repetition.
- Each column must contain the digits `1-9` without repetition.
- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.
  
Note:
A Sudoku board (partially filled) could be `valid` but is not `necessarily solvable`.
Only the `filled cells` need to be `validated` according to the mentioned rules.

`EXAMPLE 1:`
Input: board =   
[["5","3",".",".","7",".",".",".","."]  
,["6",".",".","1","9","5",".",".","."]  
,[".","9","8",".",".",".",".","6","."]  
,["8",".",".",".","6",".",".",".","3"]  
,["4",".",".","8",".","3",".",".","1"]  
,["7",".",".",".","2",".",".",".","6"]  
,[".","6",".",".",".",".","2","8","."]  
,[".",".",".","4","1","9",".",".","5"]  
,[".",".",".",".","8",".",".","7","9"]]  
Output: true  

`EXAMPLE 2:`  
Input: board =   
[["8","3",".",".","7",".",".",".","."]  
,["6",".",".","1","9","5",".",".","."]  
,[".","9","8",".",".",".",".","6","."]  
,["8",".",".",".","6",".",".",".","3"]  
,["4",".",".","8",".","3",".",".","1"]  
,["7",".",".",".","2",".",".",".","6"]  
,[".","6",".",".",".",".","2","8","."]  
,[".",".",".","4","1","9",".",".","5"]  
,[".",".",".",".","8",".",".","7","9"]]  
Output: false  
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.  

## MY SOLUTION:
The solution to this problem can be approached by the use of hashsets. Here, we use three hashsets to track the seen numbers.
- `rows[r]` for the numbers in row `r`
- `cols[c]` for the numbers in column `c`
- `squares[(r//3, c//3)]` for the numbers in `3*3` grid.

  For each cell:
  - `skip` if empty
  - return `False` if already in same row, column or grid.
  - else return `True`

 ```python
import collections
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = collections.defaultdict(set)       #declaring hashsets for all rows, columns and square grids respectively
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)     #key(r//3, c//3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":     #checking for empty condition which is denoted by .
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)] ):     #checking if already present or is duplicated
                    return False

                #adding to the hashmaps if not duplicate
                cols[c].add(board[r][c]) 
                rows[r].add(board[r][c]) 
                squares[(r//3, c//3)].add(board[r][c]) 

        return True
```
