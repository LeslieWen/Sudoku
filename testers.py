from bruteForce import *
from helpers import * 

arr=[
[0,3,9,2,0,8,7,1,5],
[6,0,8,0,0,1,0,0,0],
[0,5,0,9,3,0,8,4,6],
[7,0,4,0,1,0,0,5,8],
[8,1,0,6,4,0,3,7,0],
[0,2,0,8,0,5,1,0,4],
[5,0,3,0,9,0,0,2,1],
[0,4,1,5,0,3,0,0,7],
[9,0,0,1,2,0,5,8,0]]

def test1():
    boardPrinter(arr)
    print("----------------------------------------------")
    print(str(backTrack(arr))+", the puzzle has been solved")
    print("----------------------------------------------")
    boardPrinter(arr)
test1()