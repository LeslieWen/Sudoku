#need to refactor boardPrinter to be prettier, also print grid
def boardPrinter(arr):
    for i in range(len(arr)):
        print(arr[i])
def getRow(arr,rowNum):
    return(arr[rowNum])
def getColumn(arr,colNum):
    colArr=[]
    for i in range(len(arr)):
        colArr.append(arr[i][colNum])
    return(colArr)
def printRow(arr,rowNum):
    print(getRow(arr,rowNum))
def printColumn():
    print("")
def getSquare(row,col):
    print("")
def solved(arr):
    print("")
