import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs(row, col):
    # deque
    queue = deque()
    queue.append((row, col))
    while queue:
        row, col = queue.popleft()        
        # 4가지 방향
        for i in range(4):
            n_row = row + dx[i]
            n_col = col + dy[i]
            if n_row < 0 or n_row > r - 1 or n_col < 0 or n_col > c - 1\
            or arr[n_row][n_col] == 0:
                continue # 범위밖이거나 길 없을 때

            if arr[n_row][n_col] == 1: # 1 보다 클 때는 같은레벨의 다른 요소로 부터
                # 탐색됐거나 그 전 레벨에서 탐색했기 때문에 볼 필요가 없다
                # 무조건 같거나 더 적은 cost로 갔기 때문에
                arr[n_row][n_col] = arr[row][col] + 1
                queue.append((n_row, n_col))
                    
    return arr[r - 1][c - 1]

   
r, c = map(int, sys.stdin.readline().split()) # row(N), col(M)
arr = [[0 for _ in range(c)] for __ in range(r)]
for i in range(r):
    arr[i] = list(map(int, sys.stdin.readline().rstrip()))

# 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))




# 시간초과
# import sys
# sys.setrecursionlimit(10**6)

# def dfs(row, col, prev_cost):
#     # 길 없거나 , 돌아가는 길이면 바로 return(cost가 낮을때)
#     global cost_map    
#     if row < 0 or row > r - 1 or col <0 or col >c - 1\
#     or arr[row][col] == 0 or cost_map[row][col] < prev_cost + 1:        
#         return
    
#     cost_map[row][col] = prev_cost + 1
#     prev_cost = cost_map[row][col]
#     # 4방향 탐색(상하좌우)
#     dfs(row+1, col, prev_cost) # 아래쪽
#     dfs(row, col+1, prev_cost) # 오른쪽
#     dfs(row-1, col, prev_cost) # 위쪽
#     dfs(row, col-1, prev_cost) # 왼쪽    

# r, c = map(int, sys.stdin.readline().split()) # row(N), col(M)
# arr = [[0 for _ in range(c)] for __ in range(r)]
# cost_map = [[10001 for _ in range(c)] for __ in range(r)]
# for i in range(r):
#     arr[i] = list(map(int, sys.stdin.readline().rstrip()))

# dfs(0, 0, 0)
# print(cost_map[r-1][c-1])