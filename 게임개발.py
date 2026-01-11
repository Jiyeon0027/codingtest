def check_4_direction(x, y, d):
    for i in range(1,5):
            d = (d+i) % 4
            dx, dy = dir[d]
            
            cx , cy = x+dx, y+dy
            if 0 > cx or cx >= n or 0> cy or cy >= m:
                continue
            
            #이동
            if graph[cx][cy] == 0 and visited[cx][cy] == False:
                visited[cx][cy] = True
                return x,y
            else:
                # 바다 이거나 방향을 유지
                continue
    return None

if __name__ == "__main__" :
    n, m = map(int,input().split())
    visited = [[False for i in range(m)] for _ in range(n)]
    
    x,y,d = map(int,input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    
    dir = [(0,1), (-1,0), (0,-1), (1,0)] #반시계방향으로 회전
    
    visited[x][y] = True
    cnt = 0
    
    #왼쪽에 가보지 않은 칸 존재
    while True
        ch
        

    #모두 이미 가본 칸이거나 바다로 되어있음
    # -> 방향을 유지한 채 한칸 뒤로 가고 1단계 -> 바다면 움직임 멈춤
    
    