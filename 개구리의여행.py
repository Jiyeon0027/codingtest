#삼성 상반기 오전 2번 문제
#개구리 여행
from heapq import heappop, heappush

#호수에 개구리 한마리~ n*n
#돌의 위치 1-n

#안전한 돌 : .
#미끄러운 돌 : s
#천적이 사는 돌 : #

n = int(input())
lake = []

for i in range(n):
    line = list(input())
    lake.append(line)
    
q = int(input())
INF = 1e9
        
for _ in range(q):
    r1,c1,r2,c2 = map(int,input().split())
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1 #0based 인덱스
    
    visited = [[[0, INF] for _ in range(n)] for _ in range(n)]
    
    hq =[]
    
    visited[r1][c1] = [1, 0]
    heappush(hq,(1,0,[r1,c1])) #jump, time, r1,c1
    
    print(hq)
    while hq:
        check_sharp =[True, True, True, True] 
        # '#'여부 확인해서 더 갈 수 있는곳인지 체크
        j, time , [cx,cy] = heappop(hq) #jump 1 로 시작
        time_for_plus = 0
        
        print(f"time : {time}, cx : {cx}, cy:{cy}")
        
        if visited[cx][cy][1] < time:
            continue
        
        print("debug --- 1")
        
        for k in range(1,6):
            print("--------------")
            print(f"k :{k} , j : {j}")
            print("--------------")
            if k<j: #점프력 증감 확인
                time_for_plus = 1
            elif k>j:
                time_for_plus = sum([i**2 in range(j+1,k+1)])
            else:
                time_for_plus = 0
            
            print(f"jump : {j} time_for_plus : {time_for_plus}")
            print("debug -- 2")
                
            for idx, [dx,dy] in enumerate([(k,0),(-k,0),(0,k),(0,-k)]):
                nxt_x = cx+dx
                nxt_y = cy+dy
                print(nxt_x, nxt_y)
                if nxt_x < 0 or nxt_x >= n or nxt_y < 0 or nxt_y>= n: #호수를 벗어나면
                    continue
                if lake[nxt_x][nxt_y] == 'S': #미끄러운 돌
                    continue
                # 천적이 사는 돌
                if lake[nxt_x][nxt_y] == '#' or not check_sharp[idx]:
                    check_sharp[idx] = False
                    continue
                
                if visited[nxt_x][nxt_y][1] > time + time_for_plus + 1:
                    visited[nxt_x][nxt_y] = [k, time + time_for_plus + 1]
                    heappush(hq,(k, time + time_for_plus + 1, [nxt_x, nxt_y]))
                    print(*visited, sep='\n')
            
        
    
    # 안될 경우에 점프력 감소 후 점프 시도
    
    # 안될 경우에 점프력 증가 후 점프 시도
    
    # 최대 짧은 거리를 만드는 것이므로 dp... 진행
    
# 1. 점프
# k 칸만큼 점프 이동 d= [(0,k), (0,-k), (k,0), (-k,0)]
# 미끄러운 돌로는 이동 불가/ 점프하면서 지나치는 경로에 천적이 살면 이동 불가
# 시간 1

# 2. 점프력 증가
# 증가 후 개구리의 최대 점프력은 5
# 점프력을 증가 시키는데 드는 시간 k^2

# 3. 점프력 감소
# k 보다 작은 어떤 것이든 점프력을 가질 수 있음
# 시간 1

