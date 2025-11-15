#사이클을 찾는 union_find

import sys
input = sys.stdin.readline

def find_parents(x):
    if parent[x] != x:
        parent[x] = find_parents(parent[x])
    return parent[x]

def union(a,b) : 
    a = find_parents(a)
    b = find_parents(b)

    if a < b : 
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
cycle = False

for _ in range(e):
    print(parent)
    m,n = map(int,input().split())
    if find_parents(m) == find_parents(n) :
        cycle = True
        break
    else:
        union(m,n)

print(parent, cycle)