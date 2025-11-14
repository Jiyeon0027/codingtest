#달빛 여우

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n,m= map(int,input().split())
INF = sys.maxsize
maps = [[] for _ in range(n+1)]
    
for i in range(m):
    a,b,d = map(int,input().split())
    maps[a].append([b,d])
    maps[b].append([a,d])
    
visited1 = [INF for _ in range(n+1)]  
#달빛여우 계산 먼저 1번부터 시작
hq1 =[]
heappush(hq1,[0,1]) #weight, num
visited1[1] = 0
while hq1:
    weight, cur = heappop(hq1)
    if visited1[cur] < weight:
        continue
    for nxt_i, nxt_w in maps[cur]:
        if visited1[nxt_i]> weight + nxt_w: 
            heappush(hq1, [weight + nxt_w, nxt_i])
            visited1[nxt_i]= weight+nxt_w
            # print(hq1)
            # print(visited1)

visited2 = [[INF,INF] for _ in range(n+1)] #달빛 늑대 (빠른, 느린)
hq2 =[]
heappush(hq2,[0,1,0.5]) #weight, num
visited2[1][0] = 0 

while hq2:
    weight, cur, flag = heappop(hq2)
    if flag == 0.5: #느리게 온 경우
        if weight > visited2[cur][1]:
            continue
        for nxt_i, nxt_w in maps[cur]:
            if visited2[nxt_i][0] > weight + nxt_w*flag: 
                heappush(hq2, [weight + nxt_w*flag, nxt_i, 2])
                visited2[nxt_i][0] = weight+nxt_w*flag
    else: #빠르게 온 경우
        if weight > visited2[cur][0]:
            continue
        for nxt_i, nxt_w in maps[cur]:
            if visited2[nxt_i][1] > weight + nxt_w*flag : 
                heappush(hq2,[weight+nxt_w*flag, nxt_i, 0.5])
                visited2[nxt_i][1] = weight+nxt_w*flag
cnt = 0
for i in range(2,n+1):
    if visited1[i] < visited2[i][0] and  visited1[i] < visited2[i][1]:
        # print (visited1[i], visited2[i])
        cnt += 1

print(cnt)