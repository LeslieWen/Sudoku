def boardPrinter(arr):
    print("|=======|=======|=======|")
    for i in range(len(arr)):
        if i== 3 or i==6 or i==9:
            print("|=======|=======|=======|")
        tempStr="| "
        for j in range(len(arr[i])):
            if j == 2 or j ==5 or j==8:
                if arr[i][j] != "b":
                    tempStr=tempStr+str(arr[i][j])+" | "
                else:
                    tempStr=tempStr+". | "
            else:
                if arr[i][j] != "b":
                    tempStr=tempStr+str(arr[i][j])+" "
                else:
                    tempStr=tempStr+". "
        print(tempStr)

    print("|=======|=======|=======|")

def getRow(arr,rowNum):
    return(arr[rowNum-1])
def printRow(arr,rowNum):
    print(getRow(arr,rowNum))


def getColumn(arr,colNum):
    colArr=[]
    for i in range(len(arr)):
        colArr.append(arr[i][colNum-1])
    return(colArr)
def printColumn(arr,colNum):
    print(getColumn(arr,colNum))

#input two coordinate pairs
'''
def getSquare(row,col,arr):
    row=row-1
    col=col-1
    squareArr=[]
  
    if (0<=row<=2) and (0<=col<=2):
        squareArr=squareArr.append(arr[0:3][0:3])            
    else if(0<=row<=2) and (3<=col<=5):

    else if(0<=row<=2) and (6<=col<=8):
            
    #square 1 - row (0 to 2) to col (0 to 2)
    #square 2 - row (0 to 2) to col (3 to 5)
    #square 3 - row (0 to 2) to col (6 to 8)

    #square 4 - row (3 to 5) to col (0 to 2)
    #square 5 - row (3 to 5) to col (3 to 5)
    #square 6 - row (3 to 5) to col (6 to 8)

    #square 7 - row (6 to 8) to col (0 to 2)
    #square 8 - row (6 to 8) to col (3 to 5)
    #square 9 - row (6 to 8) to col (6 to 8)
'''
def solved(arr):    
    print("")
