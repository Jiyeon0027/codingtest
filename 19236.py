#청소년 상어

import sys
import copy
input = sys.stdin.readline

directions= [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

maps=[[] for _ in range(4)]
maps_hash = {}

for i in range(4):
    li = list(map(int,input().split()))
    for j in range(0,8,2):
        
        num  = li[j]
        dir_0 = li[j+1]-1
        maps[i].append([num, dir_0])
        # print(i,j)
        maps_hash[li[j]] = [i, j//2, dir_0]
        # print(maps_hash)

sk_x, sk_y = [0,0]
# print(maps)
# print(maps_hash)
    
#     shark_dir = maps[sk_x][sk_y][1]
#     shark_num = maps[sk_x][sk_y][0]
#     #상어가 잡아먹은 물고기 삭제
#     maps_hash[shark_num] = [-1,-1,-1]
#     maps[sk_x][sk_y] = [-1,-1]
def move_fish(maps,maps_hash, sk_x, sk_y):  
    for i in range(1,17):
        cur_x, cur_y, d = maps_hash[i]
        # print(i)
        if cur_x == -1:
            continue

        for _ in range(8):
            #이동시작
            nx, ny = [cur_x+directions[d][0], cur_y+directions[d][1]]
        
            if nx<0 or nx>=4 or ny<0 or ny>=4 or (sk_x == nx and sk_y == ny):
                #45도 반시계
                d= (d+1)%8  
                continue
            
            else:
                target_num, target_dir = maps[nx][ny]
                
                maps[nx][ny] = [i, d]  # 현재 물고기 i가 새 위치로 이동
                maps[cur_x][cur_y] = [target_num, target_dir]
                
                maps_hash[i] = [nx, ny, d]
                
                if target_num != -1:
                    maps_hash[target_num] = [cur_x, cur_y, target_dir]

                break  # 이동 성공 시 반복 종료
        # print(*maps,sep='\n')
        
def dfs(maps, maps_hash, sk_x, sk_y, total):
    global answer 
    
    shark_dir = maps[sk_x][sk_y][1]
    shark_num = maps[sk_x][sk_y][0]
    #상어가 잡아먹은 물고기 삭제
    maps_hash[shark_num] = [-1,-1,-1]
    maps[sk_x][sk_y] = [-1,-1]
    
    total += shark_num
    # print(total)
    answer = max(answer, total)
    
    move_fish(maps, maps_hash, sk_x, sk_y)
    # print()
    
    for go in range(1,4):
        nx = sk_x + directions[shark_dir][0]* go
        ny = sk_y + directions[shark_dir][1] * go
        
        if 0 <= nx < 4 and 0 <= ny < 4 and maps[nx][ny][0] != -1:
            dfs(copy.copy(maps), copy.deepcopy(maps_hash), nx, ny, total)

answer = 0
dfs(maps, maps_hash, 0, 0, 0)
print(answer)