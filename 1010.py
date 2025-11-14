#다리놓기
import math

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    x = 1
    for i in range(n):
        x*=m
        m-=1
    print(x//math.factorial(n))