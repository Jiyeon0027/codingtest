#GCD 합
import sys
from itertools import combinations
inpuut = sys.stdin.readline

def find_gcd(x,y):
    if y==0 :
        return x
    return find_gcd(y,x%y)
        
tc= int(input())
for _ in  range(tc):
    x_list = list(map(int,input().split()))
    sums =0
    for x,y in combinations(x_list[1:],2):
        gcd= find_gcd(x,y)
        sums += gcd
    print(sums)