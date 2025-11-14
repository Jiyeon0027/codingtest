import sys
sys.setrecursionlimit(1 << 25)

class SegmentTree:
    """
    세그먼트 트리에 담는 값은 앞으로 뽑아야 할 개수이다.
    세그먼트 트리의 자식 노드에는 앞으로 뽑아야 할 개수의 부분합을 넣는다.
    """
    def __init__(self, size):
        self.N = 1
        while self.N < size:
            self.N <<= 1# 2배씩 늘려서 size 이상인 최소 2의 제곱수 찾음
        
        # 전체 트리 배열 (0-based index, 크기는 2N)
        self.tree = [0] * (2 * self.N)
        
        for i in range(size):
            self.tree[self.N + i] = 1  # 초기엔 모두 살아있음

         # 내부 노드 채우기 (하위 노드들의 합)
        for i in range(self.N - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
        print(self.tree)

    def update(self, idx, value):
        # idx번째 사람의 생존 상태를 업데이트 (0이면 제거)
        idx += self.N  # 실제 리프 노드 위치로 이동
        self.tree[idx] = value  # 해당 위치에 값 변경(제거)
        print(self.tree)
        while idx > 1:
            idx >>= 1  # 부모 노드로 이동
            # 부모는 자식 두 개의 합으로 갱신
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, k):
        """
        세그먼트 트리를 이용해 k번째 살아있는 사람의 인덱스를 찾는 함수
        예: k = 3 이면, 살아있는 사람 중 3번째 사람의 번호를 찾아줌
        """
        idx = 1  # 트리의 루트에서 시작
        while idx < self.N:  # 리프 노드에 도달할 때까지 반복
            # 왼쪽 자식이 k개 이상이면, 왼쪽으로 내려감
            if self.tree[2 * idx] >= k:
                idx = 2 * idx
            else:
                # 아니면 왼쪽엔 부족하니, 오른쪽으로 감
                k -= self.tree[2 * idx]  # 왼쪽에 있는 개수만큼 k 줄임
                idx = 2 * idx + 1
        return idx - self.N  # 원래 사람 번호로 변환 (0-based)

def josephus_segment_tree(n, k):
    tree = SegmentTree(n)
    result = []
    pos = 0  # 현재 순서 위치
    for _ in range(n):
        alive = tree.tree[1] #현재 남아있는 사람 수 (루트노드에 저장)
        pos = (pos + k - 1) % alive 
        # 다음 제거할 사람 위치: 현재 위치에서 k-1만큼 더함 (mod로 원형 순회)
        idx = tree.query(pos + 1)  # k번째 사람 위치 찾기
        result.append(idx + 1)     # 사람 번호는 1-based 이므로 +1
        tree.update(idx, 0)        # 제거
    return result


result = josephus_segment_tree(7, 3)
print(result)