#방번호

import sys
import math
input = sys.stdin.readline


n = int(input())

arr_num = [0 for _ in range(10)]
cnt = 1

for i in str(n):
    num = int(i)
    arr_num[num] += 1

#check set
max_cnt = max(arr_num)
if arr_num.index(max_cnt) == 6 or arr_num.index(max_cnt) == 9:
    val = math.ceil((arr_num[6] + arr_num[9])/2)
    arr_num[6] = val
    arr_num[9] = val
print(max(arr_num))