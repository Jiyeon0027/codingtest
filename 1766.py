#문제집
 
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

#4-2
#3-1
#쉬운 문제부터
#앞에 풀어야 하는 count 1
#list 배열 : 4번문제 풀린 후 

n,m= map(int,input().strip().split())
count=[0 for _ in range(n+1)]
dict_list = {}

for _ in range(m):
    a,b = map(int,input().strip().split())
    count[b] +=1
    if a not in dict_list:
        dict_list[a] = []
    dict_list[a].append(b)
    
result=[]
for i in range(1,n+1):
    if count[i] == 0:
        heappush(result, i)

while len(result) >0 : 
    x = heappop(result)
    print(x, end =' ')
    
    if x in dict_list:
        for y in dict_list[x]:
            count[y] -=1
            if count[y] == 0:
                heappush(result,y)
    # print(result)