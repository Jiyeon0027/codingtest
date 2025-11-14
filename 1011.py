#fly me to the alpha centauri

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
mini_cnt = sys.maxsize

def dfs(start, dist, end, cnt):
    # print(f'start:{start}, end:{end}, dist:{dist}, cnt:{cnt}')
    global mini_cnt
    if start == end:
        mini_cnt = min(mini_cnt, cnt)
        return
    
    for nxt in (dist-1,dist,dist+1):
        if start+nxt > start and start+nxt<= end:
            dfs(start+nxt, dist+1, end,cnt+1)

tc = int(input())
for i in range(tc):
    x,y= map(int,input().split())
    # 현위치에서 k-1,k,k+1광년 만큼 이동 가능
    #최소한의 작동횟수
    mini_cnt = sys.maxsize
    dfs(x+1, 1,y-1, 1)
    
    print(mini_cnt+1)
    
    # 1-0,1,2 - 2,3,4, - 3,4,5 - 4,5,6 - 5,6,7

            
    
    