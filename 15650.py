# n과 m (2)

n,m = map(int,input().split())
# list_n = [i+1 for i in range(n)]
# print(list_n)
li =[]

def brute_force(x):
    if len(li) == m:
        print(*li, sep = ' ')
        return
    for i in range(x, n+1):#오름차순
        if i not in li:
            li.append(i)
            brute_force(i+1)#현재값보다 높은 것 기준
            li.pop()
    
brute_force(1)