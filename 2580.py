#스도쿠

import sys
input = sys.stdin.readline

sudoku=[]
for _ in range(9):
    sudoku.append(list(map(int,input().split())))

# nine = [0 for _ in range(10)]
toFill = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            toFill.append([i,j,[]])

def find(x,y):
    result1 =set()
    result2 =set()
    result3 =set()
    fin=[]
    for i in range(9):
        result1.add(sudoku[i][y])
        result2.add(sudoku[x][i])
        
    def check_four(x,y):
        xx,yy=[0,0]
        if 0<=x<3:
            xx =0
        elif 3<=x<6:
            xx=1
        else:
            xx=2
        
        if 0<=y<3:
            yy =0
        elif 3<=y<6:
            yy=1
        else:
            yy=2
        return xx,yy
    
    check_x, check_y = check_four(x,y)
    for i in range(check_x*3, (check_x+1)*3):
        for j in range(check_y*3, (check_y+1)*3):
            result3.add(sudoku[i][j])
    print(result1)
    print(result2)
    print(result3)
        
    for i in range(1,10):
        if i not in result1 and i not in result2 and i not in result3:
            fin.append(i)
    return fin

for num in range(len(toFill)):
    x,y,_ = toFill[num]
    print(x,y)
    
    results = find(x,y)
    toFill[num][2] = results
    # sudoku[x][y] = results[0]
    print(toFill)
    print(results)
# print(*sudoku,sep ='\n')
# for i in range(9):
#     print(*sudoku[i], sep =' ')

for x,y,re in toFill:
    if len(re)== 1:
        sudoku[x][y] = re[0]
    
    