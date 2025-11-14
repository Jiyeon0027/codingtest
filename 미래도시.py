#최단 거리 문제
import sys
input = sys.stdin.readline

INF = sys.maxsize
print(INF)
#플루이드 워셜

n, m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(m):
    i, j = map(int,input().split())
    graph[i][j] = 1
    graph[j][i] = 1
    
x,k = map(int,input().split())
    
for i in range (1, n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
            # print(*graph, sep= '\n')
    
dist = graph[1][k] + graph[k][x]
print(-1 if dist >= INF else dist)