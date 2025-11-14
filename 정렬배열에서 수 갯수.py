import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num = list(map(int, input().split()))

def find_left(arr, target):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid - 1
            if arr[mid] == target:
                result = mid
        else:
            start = mid + 1
    return result

def find_right(arr, target):
    start, end = 0, len(arr) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
            if arr[mid] == target:
                result = mid
        else:
            end = mid - 1
    return result


left = find_left(num, x)
right = find_right(num, x)

if left == -1 or right == -1:
    print(0)  # 존재하지 않음
else:
    print(f"왼쪽 인덱스: {left}, 오른쪽 인덱스: {right}")
    print(f"개수: {right - left + 1}")
