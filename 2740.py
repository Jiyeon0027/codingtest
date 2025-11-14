#행렬 곱셈

import sys
input = sys.stdin.readline

arr_A =[]
arr_B =[]
n,m = map(int,input().strip().split())
for i in range(n):
    arr_A.append(list(map(int,input().strip().split())))
    
m,k = map(int,input().strip().split())
for i in range(m):
    arr_B.append(list(map(int,input().strip().split())))

result = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):#a 행
    for j in range(k): # b 열
        for o in range(m): #a 열 , b 행
            result[i][j] += arr_A[i][o] * arr_B[o][j]#연산

for x in range((len(result))):
    print(*result[x], sep=' ')