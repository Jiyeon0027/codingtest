
def find_three(n) -> int:
    cnt = 0
    for i in range(n+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(input())
    
    print(find_three(n))