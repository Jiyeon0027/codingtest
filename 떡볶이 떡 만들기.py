#이진 탐색

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dduk = list(map(int,input().split()))

start = 0
end = max(dduk)

target = m

def check_target(dduk, height):
    customer = 0
    for i in dduk:
        if i > height:
            customer += i-height
    return customer

result = 0
while start < end:
    # print(f"start: {start}, end : {end}")
    mid = (start + end) // 2
    #적어도 m 만큼의 떡
    
    customer_dduk = check_target(dduk, mid)
    # print(f"customer_dduk : {customer_dduk}")
    if customer_dduk >= target: #조건을 충족하기는 했음...
        #더 작게 잘라야 함
        result = mid
        start = mid + 1
    else: #customer_dduk < target
        # 더 크게 잘라야 하므로 height 줄이기
        end = mid - 1
    
print(result)