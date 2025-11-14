#통계학
import heapq

n= int(input())
x_list = []
x_dict ={}

for _ in range(n):
    num = int(input())
    x_list.append(num)
    if num not in x_dict:
        x_dict[num] = 0
    x_dict[num] += 1

x_list = sorted(x_list)
# print(x_list)
sum(x_list)//n
print(round(sum(x_list)/n))
print(x_list[n//2])

max_freq = max(x_dict.values())
x_tuple = [k for k, v in x_dict.items() if v == max_freq] #filtered

x_tuple.sort()
if len(x_tuple)>1:
    print(x_tuple[1])
else:
    print(x_tuple[0])
    
print(x_list[-1]-x_list[0])
