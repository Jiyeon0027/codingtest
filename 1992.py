#쿼드 트리
import sys
input = sys.stdin.readline

n = int(input().strip())
graph=[]
for _ in range(n):
    graph.append(list(input().strip()))
result=''

# def merge(lup:str,rup:str,ldown:str, rdown:str):
#     if lup == '1' and rup == '1' and ldown =='1' and rdown =='1':
#         return '1'
#     elif lup == '0' and rup =='0' and ldown =='0' and rdown =='0':
#         return '0'
#     else:
#         return '('+lup+rup+ldown+rdown+')'

    
def devide(x,y,size):
    tmp = graph[x][y]
    global result
    for i in range(x,x+size):
        for j in range(y, y+size):
            if graph[i][j] != tmp:
                result += '('
                devide(x,y,size//2)
                devide(x,y+size//2,size//2)
                devide(x+size//2,y,size//2)
                devide(x+size//2,y+size//2,size//2)
                result +=')'
                return
    result += tmp
    return

devide(0,0,n)
print(result)
                   
                