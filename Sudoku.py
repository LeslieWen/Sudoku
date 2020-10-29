#input: 9 x 9 Array of Arrays representing sudoku board 0-9, 0 representing blank

#helper functions:
#getRow()
#getColumn()
#getSquare()
#solved()
#boardPrinter()


#brute force
#Recursive

farr=[[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]
def boardPrinter(arr):
    for i in range(len(arr)):
        print(arr[i])
boardPrinter(farr)