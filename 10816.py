
N = int(input())
num_card = list(map(int,input().split()))
M = int(input())
m_card = list(map(int,input().split()))

num_card.sort() # nlogn

def find_left(target, num_card):
    start = 0
    end = N-1
    result = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if num_card[mid] <= target:
            start = mid + 1
            if num_card[mid] == target:
                result = mid
        else:
            end = mid -1
    return result     

def find_right(target, num_card):
    start = 0
    end = N-1
    result = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if num_card[mid] >= target:
            end = mid -1
            if num_card[mid] == target:
                result = mid
        else:
            start = mid + 1
    return result
  
# print(num_card)
for i in m_card: #500,000
    target = i
    
    left = find_left(target=target, num_card=num_card)
    right = find_right(target=target, num_card=num_card)
    if left == -1 or right == -1:
        print(0, end=' ')
    else:
        print(left-right+1, end=' ')

    
    