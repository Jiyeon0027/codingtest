
import sys
from collections import deque

input = sys.stdin.readline

q= deque()
n = int(input())
size =0

for i in range(n):
    cmds = input().split()
    if size ==0 and cmds[0] not in ['push','empty','size']:
        print(-1)
        continue
    
    if cmds[0] == 'push':
        q.append(cmds[1])
        size+=1
    elif cmds[0] == 'pop':
        if q:
            print(q.popleft())
            size-=1
    elif cmds[0] == 'front':
        if q:
            print(q[0])
    elif cmds[0] == 'back':
        if q:
            print(q[-1])
    elif cmds[0] == 'size':
        print(size)
    elif cmds[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
