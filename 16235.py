#나무 재태크

import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
# nxn 크기의 땅
# m개의 나무
# k년이 지난후 살아있는 나무의 갯수

maps=[]#양분
for _ in range(n):
    maps.append(list(map(int,input().split())))
# print(maps)
nut = [[5 for i in range(n)] for j in range(n)]#deep copy
# print(f'nut: {nut}')

trees =[[[] for _ in range(n)] for _ in range(n)]#나무 위치 및 나이
for _ in range(m):
    x,y,z = map(int,input().split())
    trees[x-1][y-1].append(z)#나이
    
# print(*trees, sep='\n')
#봄 - 자신의 나이만큼 양분을 먹고 나이가 증가, 나이가 어린 나무부터 양분을 먹음, 나이만큼 양분을 먹을 수 없는 나부무는 양분을 먹지 못하고 즉시 사망

#여름 - 죽은 나무가 양분으로 (죽은나무 //2)

#가을 - 나무 번식 : 나이가 5의 배수 & 인접한 칸에 나이가 1인 나무가 생김

#겨울 - 땅에 양분 추가

direction = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for _ in range(k):
    
    #봄/여름
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) >0 : 
                trees[i][j].sort()
                # len_T = len(trees[i][j])
                alive = []
                dead = 0
                for tree_age in trees[i][j]:
                    # print(i,j)
                    # print(trees[i][j][t], nut[i][j])
                    # print(t, len(trees[i][j]))
                    if nut[i][j]>=tree_age:
                        nut[i][j] -= tree_age
                        alive.append(tree_age +1)
                    else:
                        dead += tree_age//2 #여름
                
                trees[i][j] = alive
                nut[i][j] += dead

    
    #가을겨울
    for i in range(n):
        for j in range(n):
            if len(trees[i][j]) >0 :
                trees[i][j].sort()
                for t in range(len(trees[i][j])):
                    if trees[i][j][t] %5 ==0 : #5의 배수일때
                        for x,y in direction:
                            cx = i+x
                            cy = j+y
                            if 0<=cx<n and 0<=cy<n :
                                trees[cx][cy].append(1)
    # print(maps)        
    for i in range(n):
        for j in range(n):
            nut[i][j] += maps[i][j]
    
    # print(*nut,sep='\n')
    # print(*trees, sep='\n')
    # print()
result =0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])

print(result)