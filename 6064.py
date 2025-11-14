#카잉 달력
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M,N,x,y= map(int,input().split())

    #앞 기준으로 먼저 찾기
    year = 0
    k=0
    flag =0
    while k<N*M:
        k = year * M + x
        # print(k)
        if (k - y)%N==0:
            print(k)
            flag =1
            break
        else:
            year +=1
        
    if flag == 0 :
        print(-1)