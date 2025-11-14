#이진 탐색

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

n_list.sort()
m_list.sort()

for mi in m_list:
    target = mi
    flag = False
    start = 0
    end = n-1
    while start <= end :
        mid = (start+ end)//2
        if n_list[mid] == target:
            flag = True
            break
        elif n_list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if flag:
        print("yes", end=' ')
    else:
        print("no", end = ' ')