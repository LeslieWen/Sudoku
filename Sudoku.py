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

farr3=[
[8,2,7,1,5,4,3,9,6],
[9,6,5,3,2,7,1,4,8],
[3,4,1,6,8,9,7,5,2],
[5,9,3,4,6,8,2,7,1],
[4,7,2,5,1,3,6,8,9],
[6,1,8,9,7,2,4,3,5],
[7,8,6,2,3,5,9,1,4],
[1,5,4,7,9,6,8,2,3],
[2,3,9,8,4,1,5,6,7]]


boardPrinter(farr)
print("\n")
#input two coordinate pairs row num [1-9] and col num [1-9]
printSquare(1,5,farr)
#print(solved(farr))
print(solved(farr))
