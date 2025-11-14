import sys
sys.setrecursionlimit(10 ** 6)

def cantore(start, end, array):
    length = end - start
    if length < 3:
        return

    third = length // 3
    
    for i in range(start + third, start + 2 * third):
        array[i] = 0
        
    # print(array)
    cantore(start, start + third, array)
    cantore(start + 2 * third, end, array)

while True:
    try:
    c = input()
    if c == '' or c is None:
        break
    n = int(c)
    
    size = 3 ** n
    arr = [1 for _ in range(size)]
    cantore(0, size, arr)

    # 출력: 1은 '-', 0은 ' ' 로 출력
    print(''.join(['-' if x == 1 else ' ' for x in arr]))