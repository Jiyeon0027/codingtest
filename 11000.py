#강의실 배정

import sys
import heapq
input = sys.stdin.readline

n = int(input())
st=[]
for _ in range(n):
    st.append(list(map(int,input().split())))

st.sort(key=lambda x: (x[1],x[0]))
# print(st)

cnt = 0
hq = []

for s,e in st:
    if hq and hq[0] <= s:#제일 이른시간 끝나는 강의실
        heapq.heappop(hq)
    heapq.heappush(hq, e) #끝나는 시간 저장
    # print(hq)
print(len(hq))