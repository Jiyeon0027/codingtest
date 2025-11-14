
#트리순회
import sys
input= sys.stdin.readline

graph = {}
n = int(input())
for i in range(n):
    x, l ,r = input().strip().split()
    graph[x] = (l,r)

def preorder(x):
    if x == '.':
        return
    print(x,end='')
    preorder(graph[x][0])
    preorder(graph[x][1])
    
def inorder(x):
    if x == '.':
        return
    
    inorder(graph[x][0])
    print(x,end='')
    inorder(graph[x][1])
    
def postorder(x):
    if x == '.':
        return
    
    postorder(graph[x][0])
    postorder(graph[x][1])
    print(x,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')