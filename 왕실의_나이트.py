

if __name__ == "__main__":
    cur = input()
    cnt = 0
    
    dir = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    
    x = int(cur[1]) - 1
    y = ord(cur[0]) - ord('a')
    
    for dx, dy in dir:
        cx = x+dx
        cy = y+dy
        
        if 0<=cx<8 and 0<=cy<8:
            cnt += 1
    
    print(cnt)