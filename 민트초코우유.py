from collections import deque

# n*n크기의 책상
# 민트 T ,초코 C, 우유 M 중 하나의 음식만을 신봉
# 다른 사람들에게 영향받아 여러개를 신봉 가능

N, T = map(int, input().split())
F = []
B = [[[0, 0] for _ in range(N)] for _ in range(N)]  # [신앙심, 간절함]
leader_group = []

for _ in range(N):
    F.append(list(input()))

for i in range(N):
    b_line = list(map(int, input().split()))
    for j in range(N):
        B[i][j][0] = b_line[j]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽
visited = [[False] * N for _ in range(N)]


def morning():
    # 아침 - 신앙심 +1
    for i in range(N):
        for j in range(N):
            B[i][j][0] += 1
            B[i][j][1] = 0


def inBound(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def bfs(start, favorite):
    # print(f"start : {start}")
    # print(f"favorite : { favorite}")
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = True
    B[start[0]][start[1]][0] -= 1
    grouped = []
    grouped.append([B[start[0]][start[1]][0], start[0], start[1]])

    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            # print(f"{cx+dx}, {cy+dy}---------")
            if not inBound(cx + dx, cy + dy):
                continue  # 벗어남
            if (
                not visited[cx + dx][cy + dy]
                and F[cx + dx][cy + dy] == favorite
            ):

                visited[cx + dx][cy + dy] = True
                # print(f"cnt : {cnt}")
                q.append([cx + dx, cy + dy])
                B[cx + dx][cy + dy][0] -= 1  # 신앙심 1 감소
                grouped.append([B[cx + dx][cy + dy][0], cx + dx, cy + dy])

    grouped.sort(key=lambda x: (-x[0], x[1], x[2]))
    leader = grouped[0]
    B[leader[1]][leader[2]][0] += len(grouped)
    return leader


def afternoon():
    # 점심
    #   - 인접 학생들과 신봉음식이 완전히 같으면 그룹 형성
    #   - 대표자 한명 선정 (신앙심 큰 사람, r, c 작은 사람 순)
    #   - 대표자 신앙심  += 그룹원수 -1, 그룹원 신앙심 -= 1

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                leader = bfs([i, j], F[i][j])
                leader_group.append(
                    [B[leader[1]][leader[2]][0], leader[1], leader[2]]
                )
                # 리더 그룹의 신앙, 리더 위치
            #  print(*visited, sep = '\n')


def leaders_sort(ld):
    ld_F = F[ld[1]][ld[2]]
    if ld_F in {"T", "C", "M"}:
        return 1
    elif ld_F in {"CM", "TM", "TC"}:
        return 2
    elif ld_F == "TCM":
        return 3

    return -1


def mix_FCM(a, b):
    mixed = a | b
    if "T" in mixed and "C" in mixed and "M" in mixed:
        return "TCM"
    elif "T" in mixed and "C" in mixed:
        return "TC"
    elif "T" in mixed and "M" in mixed:
        return "TM"
    elif "C" in mixed and "M" in mixed:
        return "CM"
    elif "C" in mixed:
        return "C"
    elif "M" in mixed:
        return "M"
    elif "T" in mixed:
        return "T"
    else:
        return None

def evening():
    # 저녁
    # print(leader_group)

    # 대표가 신앙 전파 - 단일(T,C,M) , 이중 (CM, TM, TC), 삼중(TCM)
    # 같은 그룹일 경우 : 대표자의 신앙심 > 동일 시 대표자의 행번호 > 열번호
    leader_group.sort(key=lambda x: (leaders_sort(x), -x[0], x[1], x[2]))
    # print(leader_group)

    for _, r, c in leader_group:
        defense = B[r][c][1]
        if defense:  # 전파 당하면 당일에는 전파하지 않음
            continue

        b = B[r][c][0]
        B[r][c][1] = 1
        x = b - 1
        dx, dy = direction[b % 4]

        sp_x = r
        sp_y = c
        fav = F[sp_x][sp_y]
        B[sp_x][sp_y][0] = 1

        while True:
            # print(f"간절함 : {x}")
            if x <= 0:
                break  # 간절함 = 0 전파 종료
            r += dx
            c += dy
            # print(dx, dy)
            # print(f"r:{r}, c:{c}, sp_x:{sp_x}, sp_y:{sp_y}")
            if not inBound(r, c):  # 격자 밖으로 전파 종료
                break
            if F[sp_x][sp_y] == F[r][c]:  # 다음으로 진행
                continue

            y = B[r][c][0]
            if x > y:  # 강한 전파
                F[r][c] = fav
                x -= y + 1
                B[r][c][0] += 1
                B[r][c][1] = 1  # 방어상태

            else:  # 약한 전파
                # print(F[r][c] , fav)
                mixed = mix_FCM(set(list(F[r][c])), set(list(fav)))
                # print(mixed)
                F[r][c] = mixed

                B[r][c][0] += x
                x = 0

                B[r][c][1] = 1  # 방어상태

        # print(*B, sep = '\n')
        # print("----------1-1-1-1-1-1-")


# 전파자는 신앙심중 1을 남기고 간절함 : B-1 로 바꿔 전파로 사용
# 전파 방향 : B%4 - (위, 아래, 왼쪽, 오른쪽) -
#   이동 및 간절함이 0 이되면 전파 종료
#    신봉음식 ==  continue
#   신봉음식 != 전파자 X > y = 강한 전파 - 동일 (간절함 -= y+1, 신앙심 +=1, ) 0이면 종료
#                       x<=y 약한 전파 - 섞임 (신앙심 += x)


def print_f_cnt():
    cnt_dict = {"TCM": 0, "TC": 0, "TM": 0, "CM": 0, "M": 0, "C": 0, "T": 0}
    for i in range(N):
        for j in range(N):
            cnt_dict[F[i][j]] += B[i][j][0]

    for key in cnt_dict.keys():
        print(cnt_dict[key], end=" ")


for i in range(T):
    leader_group = []
    visited = [[False] * N for _ in range(N)]
    morning()
    # print(*B, sep = '\n')
    # print('----------1-1-1---------')

    afternoon()
    # print(*B, sep = '\n')
    # print('-------------------')

    evening()

    print_f_cnt()
    print()
    # print(*B, sep='\n')
    # print(*F, sep='\n')
