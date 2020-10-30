def boardPrinter(arr):
    for i in range(len(arr)):
        print(arr[i])
def getRow(arr,rowNum):
    return(arr[rowNum])

def printRow():

def getColumn(arr,colNum):
    colArr=[]
    for i in range(len(arr)):
        colArr.append(arr[i][colNum])
    for i in range(len(colArr)):
        print(colArr[i])

#helper functions:
#getRow()
#getColumn()
#getSquare()
#solved()
#boardPrinter()