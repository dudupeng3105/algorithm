# 7576 토마토
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def bfs():    
    global day_cnt
    while queue:
        row, col = queue.popleft()        
        # 4가지 방향
        for i in range(4):
            n_row = row + dx[i]
            n_col = col + dy[i]
            if n_row < 0 or n_row > r - 1 or n_col < 0 or n_col > c - 1\
            or arr[n_row][n_col] == -1:
                continue # 상자 범위 밖이거나 토마토 없을 때

            if arr[n_row][n_col] == 0: # 0 보다 클 때는 같은레벨의 다른 요소로 부터
                # 탐색됐거나 그 전 레벨에서 탐색했기 때문에 볼 필요가 없다
                # 무조건 같거나 더 적은 cost로 갔기 때문에
                arr[n_row][n_col] = arr[row][col] + 1
                queue.append((n_row, n_col))
    
    return arr

   
c, r = map(int, sys.stdin.readline().split()) # col(N), row(M)
arr = [[0 for _ in range(c)] for __ in range(r)]
for i in range(r):
    arr[i] = list(map(int, sys.stdin.readline().split()))


queue = deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:
            queue.append((i, j))
  
# 4방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = bfs()
max_num = 0
for lst in arr:
    for element in lst:
        if element == 0:
            print(-1)
            exit(0)
    max_num = max(max_num, max(lst))

print(max_num-1)
    

# 1000 * 1000 배열 찾아도 1000^2 인데
# O(n^2)알고리즘은 N= 40000번정도야 1초이므로
# O(n^3)알고리즘은 N= 2560정도부터 1초
# 1000 * 1000 정도로 시간을 걱정할 필요 없다.
