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
#input two coordinate pairs row and col
def getSquare(row,col,arr):
    row=row-1
    col=col-1
    squareArr=[]
    if (0<=row<=2):
        squareArr=arr[0:3]
    elif(3<=row<=5):
        squareArr=arr[3:6]
    elif(6<=row<=8):
        squareArr=arr[6:9]
    if (0<=col<=2):    
        for i in range(len(squareArr)):
            squareArr[i]=(squareArr[i][:3])
    elif (3<=col<=5):
        for i in range(len(squareArr)):
            squareArr[i]=(squareArr[i][3:6])
    elif (6<=col<=8):
        for i in range(len(squareArr)):
            squareArr[i]=(squareArr[i][6:9])
    return(squareArr)

def printSquare(row,col,arr):
    content=getSquare(row,col,arr)
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j]=="b":
                content[i][j]="."
    print("|=======|")
    print("| "+str(content[0][0])+" "+str(content[0][1])+" "+str(content[0][2])+" |")
    print("| "+str(content[1][0])+" "+str(content[1][1])+" "+str(content[2][2])+" |")
    print("| "+str(content[2][0])+" "+str(content[2][1])+" "+str(content[2][2])+" |")
    print("|=======|")  

#list of list array flattener
def arrayFlattener(arr):
    for i in range(arr):


def solved(arr):
    flag=False
    tempArr=[]
    for i in range(len(arr)):
        if "b" in arr[i]:
            return flag
        elif arr[i].sort()!=[1,2,3,4,5,6,7,8,9]:
            return flag
    tempArr=getSquare(2,2,arr)
    tempArr=getSquare(2,5,arr)
    tempArr=getSquare(2,8,arr)

    tempArr=getSquare(2,2,arr)
    tempArr=getSquare(2,5,arr)
    tempArr=getSquare(2,8,arr)

        tempArr=getSquare(2,2,arr)
    tempArr=getSquare(2,5,arr)
    tempArr=getSquare(2,8,arr)
 