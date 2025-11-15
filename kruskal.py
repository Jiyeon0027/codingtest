# 최소 신장 트리 - 크루스칼 알고리즘
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
graph=[[] for _ in range(v+1)]
edges = []
parent = [i for i in range(v+1)]

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

for _ in range(e):
    a,b,d = map(int,input().split())
    edges.append([d,a,b])
    
edges.sort(key= lambda x: x[0])
sum_dist = 0

for edge in edges:
    d,a,b = edge
    if find_parent(a) == find_parent(b): # already cycle
        continue
    union(a,b)
    sum_dist += d 
        
print(sum_dist)