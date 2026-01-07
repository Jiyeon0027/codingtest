"""
거스름돈 문제 - 그리디 알고리즘
시간복잡도: O(k) where k는 화폐 종류의 개수
공간복잡도: O(1)
"""


def solution(n):
    """
    Args:
        n: 거슬러줘야 할 금액

    Returns:
        필요한 동전의 최소 개수
    """
    # 1. 엣지 케이스 처리
    if n <= 0:
        return 0

    # 2. 화폐 단위를 큰 순서대로 정렬 (내림차순)
    coins = [500, 100, 50, 10]
    count = 0

    # 3. 그리디 알고리즘: 가장 큰 화폐부터 최대한 많이 사용
    for coin in coins:
        # 해당 화폐로 거슬러줄 수 있는 개수
        num_coins = n // coin
        count += num_coins
        n -= num_coins * coin  # 남은 금액 업데이트

        # 남은 금액이 0이면 조기 종료 (최적화)
        if n == 0:
            break

    return count


# 테스트 케이스
if __name__ == "__main__":
    # 기본 케이스
    print(solution(1260))  # 예상: 6 (500*2 + 100*2 + 50*1 + 10*1)

    # 엣지 케이스
    print(solution(0))  # 0
    print(
        solution(1)
    )  # 1 (10원이 없으므로 실제로는 거슬러줄 수 없지만, 문제에 따라 다름)
    print(solution(500))  # 1
    print(solution(10))  # 1
