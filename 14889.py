import sys
input = sys.stdin.readline

n = int(input()) # 항상 짝수

diff = 99999
st =[]
li =[]
score = []

for _ in range(n):
    score.append(list(map(int,input().split())))

find_st_all =[]

def brute(x):
    global diff
    if len(st) == n//2 :
        sum_st =0
        sum_link =0
        for x in range(n):
            for y in range(n):
                if x+1 in st and y+1 in st:
                    sum_st += score[x][y]
                elif x+1 not in st and y+1 not in st:
                    sum_link += score[x][y]
        diff = min(abs(sum_st-sum_link),diff)
        return
    for i in range(x, n+1):
        if i not in st:
            st.append(i)
            brute(i+1)
            st.pop()

brute(1)
print(diff)

# for st_i in find_st_all:
#     start = 0 
#     link = 0
#     li_i = [x+1 for x in range(n) if x+1 not in st_i]
#     for i in range(n):
#         for j in range(n):
#             if i+1 in st_i and j+1 in st_i:
#                 start += score[i][j]
#             elif i+1 in li_i and j+1 in li_i:
#                 link += score[i][j]
#     if diff>abs(start-link):
#         diff = abs(start-link)
# print(diff)