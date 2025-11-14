#효율적인 해킹
#union-find

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
trust = [[] for _ in range(n+1)]
cnt = [1 for _ in range(n+1)]
    
for _ in range(m):
    a,b = map(int,input().split())
    trust[b].append(a)
print(trust)
    
for i in range(1,n+1):
    if len(trust[i])==0:
        continue
    visited = [0 for _ in range(n+1)]
    q = deque()
    q.append(i)
    visited[i] = 1
    while q: 
        x = q.popleft()
        for y in trust[x]:
            if visited[y] == 0 :
                q.append(y)
                visited[y] = 1
                cnt[i] +=1
# print(cnt)
max_cnt = max(cnt)
# print(max_cnt)
for i in range(n+1):
    if cnt[i] == max_cnt:
        print(i, end=' ')
