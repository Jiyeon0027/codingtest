#냅색문제
import sys
input = sys.stdin.readline

n, c = map(int,input().split())
maps = list(map(int,input().split()))
maps.sort()

# print(maps)

li1 = []
li2 = []

def combin(x,end,li):
    if end == n//2:
        li1.append(sum(li))
    else:
        li2.append(sum(li))
    for i in range(x+1, end):
        li.append(maps[i])
        combin(i,end,li)
        li.pop()

combin(-1,n//2,[])
combin(n//2-1,n,[])
li1.sort()
li2.sort()

# print(li1,li2)
cnt = 0
for i in li1:
    target = c-i
    st = 0
    end = len(li2)-1
    while st<=end:
        mid = (st+end)//2
        if li2[mid] <= target:
            st =mid+1
        else:
            end = mid -1
    cnt += st

print(cnt)