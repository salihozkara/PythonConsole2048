
from random import randint
from copy import deepcopy
allRows = []
finish:bool=False
for i in range(4):
    allRows.append([0] * 4)


def printMatris(matris):
    for i in matris:
        print(i)


def newNumber():
    if randint(0,10)>2:
        return 2
    else:
        return 4


def randLocation(lenght):
    return randint(0, lenght-1), randint(0, lenght-1)


def addNewNumber(matris,number:int):
    column, row = randLocation(len(matris))
    while(matris[column][row] != 0):
        column, row = randLocation(len(matris))
    matris[column][row] = number

def moveRightLeftDownUp(matris,first:bool,secand:bool):
    c1,r1,c2,r2=0,0,0,0
    islem = False
    jValue=len(matris)-1
    jValueControle=0
    step=-1
    if first:
        jValue,jValueControle=jValueControle,jValue
        step=-step
    for i in range(0, len(matris)):
        j=jValue
        while (j>jValueControle and not first) or (j<jValueControle and first):
            c1,c2=i,i
            r1,r2=j,j+step
            if secand:
                c1,r1=r1,c1
                c2,r2=r2,c2
            if matris[c1][r1] == 0:
                matris[c1][r1] = matris[c2][r2]
                matris[c2][r2] = 0
                if matris[c1][r1]!=0:
                    j=jValue-step
            elif matris[c1][r1] == matris[c2][r2]:
                if islem:
                    islem = False
                else:
                    matris[c1][r1] += matris[c2][r2]
                    islem = True
                    matris[c2][r2] = 0
            else:
                islem=False
            j+=step

def sonuc(matris):
    gameOver=True
    for i in matris:
        for j in i:
            if j==2048:
                print("Won")
                return False
            elif j==0:
                gameOver=False
    if gameOver:
        print("Game Over")
        return False
    return True

def matrisEquals(matris1,matris2):
    for i in range(len(matris1)):
        for j in range(len(matris1)):
            if matris1[i][j]!=matris2[i][j]:
                return False
    return True
def StartGame():
    print("Commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    addNewNumber(allRows,2)
    addNewNumber(allRows,2)
    printMatris(allRows)
    while sonuc(allRows):
        secim = input("direction:")
        oldMatris=deepcopy(allRows)
        match secim:
             case 'w':
                 moveRightLeftDownUp(allRows,True,True)
             case 's':
                 moveRightLeftDownUp(allRows,False,True)
             case 'a':
                 moveRightLeftDownUp(allRows,True,False)
             case 'd':
                 moveRightLeftDownUp(allRows,False,False)
        if not matrisEquals(oldMatris,allRows):
            addNewNumber(allRows,newNumber())
        printMatris(allRows)
        print()
        


StartGame()
