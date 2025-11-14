#집합의 표현

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = [i for i in range(n+1)]

def find_root(arr, a):
    # print(arr, a)
    if arr[a] == a:
        return a
    
    arr[a] = find_root(arr, arr[a])
    return arr[a]
    
for _ in range(m):
    cmd, a, b = map(int,input().split())
    root_a = find_root(arr,a)
    root_b = find_root(arr,b)
    
    # print(root_a, root_b)
    if cmd == 0: #합집합
        #둘이 같은 집합이 아니면
        if root_a != root_b:
            arr[a] = b #a-b 연결
        # print(arr)
    else:
        if root_a == root_b:
            print('YES')
        else:
            print('NO')
        
        