#체스판 다시 칠하기
import sys
input = sys.stdin.readline

n,m,k = map(int,input().strip().split())

boards = []
for i in range(n):
    boards.append(list(input().strip()))
# print(boards)

#제한 1< n,m < 2000

start_white=[[0]*m for _ in range(n)]
start_black=[[0]*m for _ in range(n)]

#2000*2000
for i in range(n):
    for j in range(m):
        if i%2==0: #세로 0,2,4,8
            if j%2 ==0:
                if boards[i][j] == 'W':
                    start_black[i][j] = 1
                else:
                    start_white[i][j] = 1
            else:
                if boards[i][j] == 'B':
                    start_black[i][j] = 1
                else:
                    start_white[i][j] = 1
        else:#세로 1,3,5,7
            if j%2 ==0:
                if boards[i][j] == 'B':
                    start_black[i][j] = 1
                else:
                    start_white[i][j] = 1
            else:
                if boards[i][j] == 'W':
                    start_black[i][j] = 1
                else:
                    start_white[i][j] = 1
print(*start_black, sep='\n')
print()
print(*start_white, sep = '\n')

for i in range(n):
    for j in range(m-k+1):
        start_black[i][j] = sum(start_black[i][j:j+k])
        start_white[i][j] = sum(start_white[i][j:j+k])
# print()
# print(*start_black, sep='\n')
# print()
# print(*start_white, sep ='\n')

# print()

for i in range(n-k+1):
    for j in range(m-k+1):
        start_black[i][j] = sum([start_black[x][j] for x in range(i,i+k)])
        start_white[i][j] = sum([start_white[x][j] for x in range(i,i+k)])
        
minimun = 1000000
for i in range(n-k+1):
    for j in range(m-k+1):
        minimun = min(minimun, min(start_black[i][j], start_white[i][j]))

print(minimun)