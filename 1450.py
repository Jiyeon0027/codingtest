#냅색문제

import sys
from itertools import combinations as cb
input = sys.stdin.readline

n,c = map(int,input().split())
#가방에 넣는 방법의 수 출력
INF = int(1e9)
w = list(map(int,input().strip().split()))

arr_1 = w[:n//2]
arr_2 = w[n//2:]
sum_1 =[]
sum_2 =[]

for i in range(0, len(arr_2)+1):
    sum_1.extend(list(map(sum,cb(arr_1,i))))
    sum_2.extend(list(map(sum,cb(arr_2,i))))
    # print(sum_1, sum_2)
  
sum_1.sort()
sum_2.sort()
# print(sum_1, sum_2)


count =0
for i in sum_1:
    target = c-i
    # print(f'target: ',target)
    a=0
    b=len(sum_2)-1
    while a<=b:
        mid = (a+b)//2
        # print(mid, sum_2[mid])
        if sum_2[mid] <= target:
            a= mid+1
        else:
            b= mid-1
    count += a
print(count)