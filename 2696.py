#중앙값 구하기

import sys
input= sys.stdin.readline

from heapq import heappop, heappush
#우선순위큐,.,,

tc = int(input())
for t in range(tc): # 1000
    m = int(input())
    sorted_data =[] #최소힙... 만들기
    result =[]
    idx =0
    for _ in range(m//10+1):
        for x in map(int,input().strip().split()):
            j =idx #x보다 앞부분 탐색
            # print(idx)
            sorted_data.append(x)
            # print(sorted_data)
            
            while sorted_data[j-1] > x:
                # print(j, x)
                #swap
                sorted_data[j], sorted_data[j-1] = sorted_data[j-1],  sorted_data[j]
                # print(sorted_data)
                j-=1
                if j ==0 :
                    break
            
            idx+=1
            if idx %2 ==1:
                result.append(sorted_data[idx//2])
            
    print(len(result))
    kklen= len(result)//10
    for i in range(kklen):
        print(*result[i*10:(i+1)*10],sep=' ')
    print(*result[kklen*10:],sep=' ')