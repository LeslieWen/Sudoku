from helpers import *
#Backtracking Alg
def backTrack(arr):
    foundEmpty=findEmpty(arr) #an empty cell in the board
    if foundEmpty == None:
        return True
    else:
        row,col=(foundEmpty)
    for i in range(1,10):
        if validate(arr,i,(row,col)):
            arr[row][col]=i
            backTrack(arr)            
            if solved(arr):
                return True
            arr[row][col]=0
    return False
        


