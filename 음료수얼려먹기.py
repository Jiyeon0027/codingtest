

if __name__ == '__main__':
    graph =[]
    for i in range(4):
        graph.append(list(input()))
    
    print(graph)
        
    visited = [[False]*5 for _ in range(4)]
    cnt = 0
    
    def dfs(i,j):
        print(f"i = {i}, j = {j}")
        visited[i][j] = True

        dir = [(1,0), (-1,0), (0,1), (0, -1)]
        for dx, dy in dir:
            cx = i + dx
            cy = j + dy
            if 0> cx or cx >= 4 or 0> cy or cy >=5 :
                continue
            if graph[cx][cy] == '0' and visited[cx][cy] == False:
                dfs(cx, cy)
            
                
    for i in range(4):
        for j in range(5):
            if graph[i][j] == '0' and visited[i][j] == False:
                cnt += 1
                dfs(i,j)
                print(f"cnt = {cnt}")