#별자리 만들기

import sys
import math
from itertools import combinations as cb
input = sys.stdin.readline

def find_root(arr, a):
    if arr[a] == a:
        return a
    arr[a] = find_root(arr,arr[a])
    return arr[a]

n = int(input())
graph = [[] for _ in range(n)]
weight_gh =[]
for i in range(n):
    x, y = map(float, input().split())
    graph[i] = [x,y]
    # weight_gh[i] = []
# print(graph)

for a,b in cb(range(n),2):#n(n-1)//2 = > o(n^2)
    weight = math.sqrt((graph[a][0]- graph[b][0])**2 + (graph[a][1] - graph[b][1])**2)
    weight_gh.append((weight, a,b))
    # weight_gh[a].append((weight_gh,b))
    # weight_gh[b].append((weight_gh,a))

weight_gh.sort(key= lambda x : x[0])
INF = sys.maxsize
visited = [i for i in range(n)]
result_w = 0

for w,a,b in weight_gh:
    root_a = find_root(visited, a)
    root_b = find_root(visited,b)
    if root_a != root_b : 
        visited[root_a] = root_b
        result_w += w #다른 노드라면 결과값을 더해줌(가중치 정렬이 되어있으므로 항상 작은 가중치 부터 가능)
    #같은 노드일 경우 결과값을 뛰어넘음
    # print(visited, result_w)

print(f'{result_w:.2f}')



