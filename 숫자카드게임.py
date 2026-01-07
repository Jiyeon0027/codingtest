import sys

input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int,input().split())
    max_val = -1
    for _ in range(n):
        li = list(map(int,input().split()))
        min_val_of_row = min(li)
        max_val = max(min_val_of_row, max_val)
    
    print(max_val)
        
    