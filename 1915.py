#가장 큰 정사각형

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,list(input().strip()))))

for i in range(1,n):
    for j in range(1,m):
        if graph[i][j]==1:
            graph[i][j] = min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j])+1

max_val =0
for i in range(n):
    max_val = max(max_val, max(graph[i])**2)
print(max_val)