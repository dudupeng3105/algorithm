import sys

def dfs(depth, r1, c1, r2, c2, button):
    global temp
    r1, c1, r2, c2 = r1+dr[button], c1+dc[button], r2+dr[button], c2+dc[button]
    # 종료조건 or 백 조건
    # 0. 조작 10번 이상
    if depth > temp or depth > 10:
        return
    # 1. 둘 다 같은 자리
    if (r1, c1) == (r2, c2):
        return
    # 2. 둘 다 떨어짐
    if (r1 > row_size-1 or r1 < 0 or c1 > col_size-1 or c1 < 0)\
        and (r2 > row_size-1 or r2 < 0 or c2 > col_size-1 or c2 < 0):    
        return    

    #3. 개수 체크 조건 -> 하나만 떨어짐 -> 체크 -> return
    if (r1 > row_size-1 or r1 < 0 or c1 > col_size-1 or c1 < 0):
        if depth < temp:            
            temp = depth
        return
    
    if (r2 > row_size-1 or r2 < 0 or c2 > col_size-1 or c2 < 0):
        if depth < temp:            
            temp = depth
        return

    # 3. 둘 다 벽쪽 진행    
    if arr[r1][c1] == '#' and arr[r2][c2] == '#':
        return

    if arr[r1][c1] == '#': # coin 1만 벽임
        r1, c1 = r1-dr[button], c1-dc[button]
    
    if arr[r2][c2] == '#': # coin 2만 벽임
        r2, c2 = r2-dr[button], c2-dc[button]
        
    
    for button in range(4):
        dfs(depth+1, r1, c1, r2, c2, button)


row_size, col_size = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(col_size)] for __ in range(row_size)]
for i in range(row_size):
    arr[i] = list(sys.stdin.readline().rstrip())


coin_pos = []
for i in range(row_size):
    for j in range(col_size):
        if arr[i][j] == 'o':
            coin_pos.append((i, j))

dr = [1,0,-1,0,0]
dc = [0,1,0,-1,0]

temp = 100
row_1, col_1 = coin_pos[0]
row_2, col_2 = coin_pos[1]
dfs(0, row_1, col_1, row_2, col_2, 4)
if temp == 100:
    print(-1)
else:
    print(temp)



