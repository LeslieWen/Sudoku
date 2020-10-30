from helpers import boardPrinter
from helpers import getRow
from helpers import getColumn

#input: 9 x 9 Array of Arrays representing sudoku board 0-9, 0 representing blank

#Brute force
#Recursive

farr=[[1,2,3,4,5,6,7,'b',9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]

print(getColumn(farr,2))
