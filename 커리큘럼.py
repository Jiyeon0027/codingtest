import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
min_time = int(1e9)
inDegree = [0 for _ in range(n+1)]
time = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
q=deque()

for i in range(1, n+1):
    t, *li = map(int,input().split())
    
    for j in li[:len(li)-1]:
        graph[j].append(i)
    
    inDegree[i] = len(li) - 1
    if inDegree[i] == 0:
        q.append(i)
    
    time[i] = t

result = [0 for _ in range(n+1)]
while q:
    cur = q.popleft()
    result[cur] += time[cur]
    # print(f"cur : {cur} , result = {result}")
    
    for i in graph[cur]:
        # print(i ,end = ' ')
        inDegree[i] -= 1
        result[i] = result[cur]
        # print(result)
        
        if inDegree[i] ==0:
            q.append(i)

print(result)
    