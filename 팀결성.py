# 팀 결성

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [i for i in range(n+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cmd, a,b = map(int,input().split())
    
    if cmd == 0:
        union(a,b)
    elif cmd == 1:
        if find_parent(a) == find_parent(b):
            print("yes")
        else:
            print("no")