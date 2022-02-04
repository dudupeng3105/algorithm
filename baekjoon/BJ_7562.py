import sys
from collections import deque

def bfs():    
    while queue:
        row, col = queue.popleft()        
        # 8가지 방향
        for i in range(8):
            n_row = row + dx[i]
            n_col = col + dy[i]
            if n_row < 0 or n_row > N - 1 or n_col < 0 or n_col > N - 1\
            or arr[n_row][n_col] != 0:
                continue # 체스 판 밖이거나 이미 전 레벨에서 갔을 때

            if arr[n_row][n_col] == 0: # 0 보다 클 때는 같은레벨의 다른 요소로 부터
                # 탐색됐거나 그 전 레벨에서 탐색했기 때문에 볼 필요가 없다
                # 무조건 같거나 더 적은 cost로 갔기 때문에
                arr[n_row][n_col] = arr[row][col] + 1
                queue.append((n_row, n_col))
                if (n_row, n_col) == (destn_row, destn_col):
                    return arr
    
    return arr


test_case = int(sys.stdin.readline())
#8방향
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(test_case):
    N = int(sys.stdin.readline())
    arr = [[0 for _ in range(N)] for __ in range(N)]
    start_row, start_col = map(int, sys.stdin.readline().split())
    destn_row, destn_col = map(int, sys.stdin.readline().split())    
    if (start_row, start_col) == (destn_row, destn_col):
        print(0)
        continue
    else:
        queue = deque()
        queue.append((start_row, start_col))
    
        bfs()        
        print(arr[destn_row][destn_col])