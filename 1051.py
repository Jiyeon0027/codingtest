#숫자 정사각형

import sys

def main():
    input= sys.stdin.readline
    n,m = map(int,input().split())
    graph =[]
    for _ in range(n):
        graph.append(list(map(int,list(input().strip()))))

    max_sq = min(n,m)
    while max_sq>0:
        # print(max_sq)
        for i in range(n-max_sq):
            for j in range(m-max_sq):
                ul = graph[i][j]
                ur = graph[i][j+max_sq]
                dl = graph[i+max_sq][j]
                dr = graph[i+max_sq][j+max_sq]
                if ul==ur and ur ==dl and dl==dr and dr ==ul:
                    return (max_sq+1)**2
        max_sq-=1
    return 1
    
if __name__ == "__main__":
    print(main())