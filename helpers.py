#Prints the current state of the Sudoku board

def boardPrinter(arr):
    print("|=======|=======|=======|")
    for i in range(len(arr)):
        if i== 3 or i==6 or i==9:
            print("|=======|=======|=======|")
        tempStr="| "
        for j in range(len(arr[i])):
            if j == 2 or j ==5 or j==8:
                if arr[i][j] in list(range(1,10)):
                    tempStr=tempStr+str(arr[i][j])+" | "
                else:
                    tempStr=tempStr+". | "
            else:
                if arr[i][j] in list(range(1,10)):
                    tempStr=tempStr+str(arr[i][j])+" "
                else:
                    tempStr=tempStr+". "
        print(tempStr)
    print("|=======|=======|=======|")

#Returns specified row (1-9)

def getRow(arr,rowNum):
    return(arr[rowNum-1])
def printRow(arr,rowNum):
    print(getRow(arr,rowNum))

#Returns specified column (1-9)

def getColumn(arr,colNum):
    colArr=[]
    for i in range(len(arr)):
        colArr.append(arr[i][colNum-1])
    return(colArr)
def printColumn(arr,colNum):
    print(getColumn(arr,colNum))

#Input two coordinate pairs row and col, returns 
#the square that cell belongs to

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

#Prints the specified square that contains coordinate row and col

def printSquare(row,col,arr):
    content=getSquare(row,col,arr)
    for i in range(len(content)):
        for j in range(len(content[i])):
            if content[i][j] not in list(range(1,10)):
                content[i][j]="."
    print("|=======|")
    print("| "+str(content[0][0])+" "+str(content[0][1])+" "+str(content[0][2])+" |")
    print("| "+str(content[1][0])+" "+str(content[1][1])+" "+str(content[2][2])+" |")
    print("| "+str(content[2][0])+" "+str(content[2][1])+" "+str(content[2][2])+" |")
    print("|=======|")

#List of list array flattener

def arrayFlattener(arr):
    flatList=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            flatList.append(arr[i][j])
    return flatList
#Returns true or false based on whether sudoku board is solved

def solved(arr):
    flag=False
    tempArr=[]
    for i in range(len(arr)):
        if "b" in arr[i]:
            return flag
        if sorted(arr[i])!=list(range(1,10)):
            return flag
    for i in [2,5,8]:
        if sorted(arrayFlattener(getSquare(2,i,arr)))!=list(range(1,10)):
            return flag
        if sorted(arrayFlattener(getSquare(5,i,arr)))!=list(range(1,10)):
            return flag
        if sorted(arrayFlattener(getSquare(8,i,arr)))!=list(range(1,10)):
            return flag                
    return True

#Find the first empty cell in the board
    
def findEmpty(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] not in range(1,10):
                return(i,j)
    return None

#Given a coordinate, check if num is a legal choice

def validate(arr,num,pos):
    #row checker
    for i in range(len(arr[0])):
        if arr[pos[0]][i]==num and pos[1]!=i:
            return False
    #column checker
    for i in range(len(arr)):
        if arr[i][pos[1]]==num and pos[0]!=i:
            return False
    #square checker
    indexMap=[0,1,2,0,1,2,0,1,2]
    tempSqr=getSquare((int(pos[0])+1),(int(pos[1])+1),arr)
    for i in range(3):
        for j in range(3):
            if tempSqr[i][j] == num and (i,j)!=(indexMap[pos[0]],indexMap[pos[1]]):
                return False
    return True
