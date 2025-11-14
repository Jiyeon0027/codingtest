from collections import deque

chess = []
wall = []
for i in range(8):
    k = list(input())
    chess.append(k)
    for j, block in enumerate(k):
        if block == '#':
            wall.append([i, j])

sx, sy = 7, 0
ex, ey = 0, 7

direction = [(0,0),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1),(-1,0),(-1,-1)]

def bfs(x, y, ex, ey):
    q = deque()
    q.append([x, y])
    time = 0

    while q:
        visited = [[False] * 8 for _ in range(8)]  # 매 레벨마다 새로
        for _ in range(len(q)):
            cur_x, cur_y = q.popleft()

            # 현재 위치가 벽이면 못 움직임
            if [cur_x, cur_y] in wall:
                continue
            # 도착 성공
            if cur_x == ex and cur_y == ey:
                return 1

            for i, j in direction:
                nx, ny = cur_x + i, cur_y + j
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if [nx, ny] not in wall and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])

        # 벽 이동 (레벨 끝난 뒤에만 한 번)
        new_wall = []
        for wx, wy in wall:
            if wx + 1 < 8:   # 보드 안에 있으면만 남김
                new_wall.append([wx + 1, wy])
        wall[:] = new_wall

        time += 1
        if time >= 8:  # 8턴 지나면 벽 사라짐 → 탈출 가능
            return 1

    return 0

print(bfs(sx, sy, ex, ey))
