import sys
from collections import deque
import time

def bfs(start_row, start_col):
    q = deque()
    q.append((start_row, start_col, 0))  # row, col, num
    while q:
        row, col, moved_num = q.popleft()

        chess_board[row][col] = True  # 방문 체크

        for i in range(6):  # 주사위
            new_row = row + dr[i]
            new_col = col + dc[i]

            if new_row < 0 or new_row > n-1 or new_col < 0 or new_col > n-1:
                continue

            if chess_board[new_row][new_col]:  # 이미왔으면
                continue

            q.append((new_row, new_col, moved_num + 1))


dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

start = time.time()
n = int(sys.stdin.readline().rstrip())
chess_board = [[False for _ in range(n)] for __ in range(n)]
start_r, start_c, end_r, end_c = map(int, sys.stdin.readline().split())
bfs(start_r, start_c)
print(chess_board[end_r][end_c])
print("time:", time.time()-start)