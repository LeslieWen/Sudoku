from helpers import *
#Backtracking Alg
def backTrack(arr):
    foundEmpty=findEmpty(arr) #an empty cell in the board
    if foundEmpty == None and solved(arr) == True:
        return True
    else:

