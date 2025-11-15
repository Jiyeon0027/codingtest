import sys
input = sys.stdin.readline

n, m = map(int,input().split())
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
        
edges = []
for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))

edges.sort(key = lambda x: x[0])
dist_sum = 0
seperate = 0

for edge in edges:
    c,a,b = edge
    if find_parent(a)== find_parent(b):
        continue
    else:
        union(a,b)
        dist_sum  += c
        seperate = max(seperate, c)

print(dist_sum - seperate)
    
    
