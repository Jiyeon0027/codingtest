import sys

v, e = map(int,input().split())
parent = [i for i in range(v+1)]

def find_parents(x):
    print(x, end= ' ')
    if parent[x] == x: #root node
        return x
    
    parent[x] = find_parents(parent[x])
    return parent[x]

def union(a,b) :
    print("find a")
    rootA = find_parents(a)
    print("find b")
    rootB = find_parents(b)
    
    if rootA < rootB :
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
    

for _ in range(e):
    x,y = map(int,input().split())
    union(x,y)
    print(parent)