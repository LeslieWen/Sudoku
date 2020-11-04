from helpers import *
from bruteForce import *

#input: 9 x 9 Array of Arrays representing sudoku board 0-9, b representing blank
farr=[
[1,2,3,4,5,6,7,'b',9],
[1,2,'b',4,5,'b',7,8,9],
[1,2,3,4,5,'b',7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9]]

farr2=[
[1,2,3,4,5,6,7,9,9],
[1,2,9,4,5,9,7,8,9],
[1,2,3,4,5,9,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9]]

boardPrinter(farr2)
#print("\n")
#input two coordinate pairs row num [1-9] and col num [1-9]
#printSquare(1,5,farr)
#print(solved(farr))
print(solved(farr2))
