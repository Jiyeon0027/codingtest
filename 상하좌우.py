def solution(plan: list[str], n: int) -> tuple[int, int]:
    x, y = 1, 1

    moves: dict[str, tuple[int, int]] = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0),
    }

    for p in plan:
        dx, dy = moves[p]
        nx, ny = x + dx, y + dy

        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny

        print(x, y)

    return x, y

if __name__== "__main__":
    n = int(input())
    plan = input().split()
    
    x,y = solution(plan, n)
    print("-------------")
    print(x,y)