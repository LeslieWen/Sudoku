from helpers import *
#Backtracking Alg
def backTrack(arr):
    foundEmpty=findEmpty(arr) #an empty cell in the board
    if foundEmpty == None:
        return True
    else:
        row,col=(foundEmpty)
    for i in range(1,10):
        


