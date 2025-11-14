#스타트와 링크

import sys
from collections import deque  
input= sys.stdin.readline

f,s,g,u,d = map(int,input().split())
# print(f'{f}층 건물 {s} -> {g}로 이동 {u} 위로 , {d} 아래로')
check = [0 for _ in range(f + 1)]  


def bfs():  
    queue = deque()  
    queue.append(s)  

    check[s] = 1  

    while queue:  
        y = queue.popleft()  

        if y == g:  
            return check[y] - 1  
        else:  
            for x in (y + u, y - d):  
                if (0 < x <= f) and check[x] == 0:  
                    check[x] = check[y] + 1  
                    queue.append(x)  

    return "use the stairs"  


print(bfs())