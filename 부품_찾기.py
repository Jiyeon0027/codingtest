# 이진 탐색

import sys
input = sys.stdin.readline

n = int(input())
shop_list = list(map(int,input().split()))
shop_list.sort()

m = int(input())
users = list(map(int,input().split()))

def binarySearch(t):
    start = 0 
    end = n-1
    
    while start<=end:
        mid = (start+end) // 2
        # print(start, mid, end)
        if shop_list[mid] < target:
            start = mid + 1
        elif shop_list[mid] == target:
            return True
        else:
            end = mid - 1
    return False
        

for target in users:
    if binarySearch(target):
        print("yes")
    else:
        print("no")