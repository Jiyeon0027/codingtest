
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i ,0, -1):
        if array[j] < array[j-1]: #작으면 한칸씩 내리기
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        else:
            break

# 정렬된 상태라면 매우 빠르게 동작한다는 사실
