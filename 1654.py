#랜선 자르기

import sys
input =sys.stdin.readline

k,n = map(int,input().strip().split())
lan=[]
for _ in range(k):
    lan.append(int(input().strip()))

start =0
end = max(lan)

while start<end:
    # print(start, end)
    mid = (start+end)//2 +1
    count =0
    # print(f'mid:{mid}')
    for i in lan:
        count += i//mid
        # print(count)
        
    if count<n:#갯수 모자르면 더 작게 잘라야함
        end = mid-1
    else:#갯수가 충족되면 최대 길이를 구해야함
        start = mid
    
print(start)