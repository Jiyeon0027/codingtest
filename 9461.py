#파도반 수열
import sys
input = sys.stdin.readline

p =[0 for _ in range(101)]
p[1] = 1 
p[2] = 1
p[3] = 1
p[4] = 2
p[5] = 2
# p[6] = p[5] + p[1]
# p[7] = p[6] + p[2]
# p[8] = p[7] + p[3]

for i in range(6,101):
    p[i] = p[i-1]+p[i-5]

T = int(input().strip())
for t in range(T):
    x = int(input().strip())
    print(p[x])

