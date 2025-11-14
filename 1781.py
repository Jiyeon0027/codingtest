# 컵라면

import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n = int(input())
deadlineCups =[]
for i in range(n):
    a = list(map(int,input().split()))
    deadlineCups.append(a)

# print(deadlineCups)
deadlineCups.sort(key= lambda x : [x[0], -x[1]])
print(deadlineCups)

cnt = 0
hq =[]
for deadline, ramen in deadlineCups:
    heappush(hq,ramen)
    print(hq)
    if len(hq) > deadline:
        heappop(hq)
        print(f'remove : {hq}')
print(sum(hq))
    
# now = 1
# for deadline, ramen in deadlineCups:
    
#     if now <= deadline:
#         cnt += ramen
#         now+=1
#         # print(cnt, deadline, ramen ,n)
#         # now = deadline
# print(cnt)