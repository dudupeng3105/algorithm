import sys
sys.setrecursionlimit(10**6)
def dfs(row, col):
    # 땅이 아니면 return    
    if row < 0 or row > h-1 or col <0 or col > w-1\
    or arr[row][col] == 0:
        return
    
    arr[row][col] = 0 # 체크했으니 빈칸으로 만들어버림
    # 8방향 탐색(상하좌우, 대각)
    dfs(row-1, col-1) # 10시 방향
    dfs(row-1, col) # 12시
    dfs(row-1, col+1) # 2시 방향
    dfs(row, col-1) # 9시 방향
    dfs(row, col+1) # 3시 방향
    dfs(row+1, col+1) # 7시 방향
    dfs(row+1, col) # 6시 방향
    dfs(row+1, col+1) # 5시 방향


# width(col), height(row)
while(1):
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [[0 for _ in range(w)] for __ in range(h)]

        for i in range(h):
            arr[i] = list(map(int, sys.stdin.readline().rstrip().split()))
       
        # arr 탐색
        island_num = 0 # 단지 수

        for i in range(h):
            for j in range(w):
                if arr[i][j] == 1:            
                    dfs(i, j)            
                    island_num += 1

        print(island_num)