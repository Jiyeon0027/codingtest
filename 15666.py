# n과 m(12)

import sys
input  = sys.stdin.readline

n,m= map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

#중복가능
#비내림차순
result =[]

def backTracking(i,li):
    # print(i, li)
    if len(li) == m:
        for res in result:
            if res == li:
                return
        result.append(li[:])
        return
    for x in range(i, n):
        li.append(arr[x])
        brute(x,li)
        li.pop()
# print(n,m)
# print(arr)

backTracking(0,[])
for res in result:
    print(*res, sep=' ')
# print(set(result))