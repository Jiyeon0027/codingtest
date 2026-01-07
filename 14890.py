# 경사로
n,l = map(int,input().split())
#길은 총 2n
graph =[[0] * (n + 2*l ) for _ in range(n + 2*l )]
result = 2*n

for i in range(n):
    road1 = list(map(int,input().split()))
    
    for j in range(n):
        graph[i+l][j+l] = road1[j]
    #경사로의 길이에 따라서 
    # 112
    # 211

print(*graph, sep ='\n')
#-------가로에 대해서
for i in range(l, n+l):
    print(graph[i])
    # usd =set()
    for cur in range(l+1,l+n):
        before = graph[i][cur-1]
        current = graph[i][cur]
        print(f"before: {before}, current : {current}")
        if abs(before-current) >= 2:
            result -=1
            break
        
        elif before > current: #211
            print(graph[i][cur:cur+l])
            if sum(graph[i][cur:cur+l]) != current*l :
                result -=1
                break
            # else:
            #     usd.add()
                
        elif before < current: #112
            print(graph[i][cur-l:cur])
            if sum(graph[i][cur-l:cur]) != before*l :
                result -=1
                break
    print(result)

#---------세로에 대해서
for i in range(l, n+l):
    # print(graph[i])
    for cur in range(l+1,l+n):
        before = graph[cur-1][i]
        current = graph[cur][i]
        print(f"before: {before}, current : {current}")
        if abs(before-current) >= 2:
            result -=1
            break
        
        elif before > current:
            print([graph[k][i] for k in range(cur, cur+l)])
            if sum(graph[k][i] for k in range(cur, cur+l)) != current * l:
                result -=1
                break

        elif before < current:
            print([graph[k][i] for k in range(cur-l, cur)])
            if sum(graph[k][i] for k in range(cur-l, cur)) != before * l:
                result -=1
                break
    print(result)