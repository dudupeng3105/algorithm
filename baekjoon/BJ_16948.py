import sys
from collections import deque
import time

# bfs 인자 하나 추가될때마다 시간이 많이 걸린다. -> 최대한 적게 사용 2개정도까지

def bfs(start_row, start_col):
    q = deque()
    q.append((start_row, start_col))  # row, col, num
    chess_board[start_row][start_col] = 0
    while q:
        row, col = q.popleft()
        for i in range(6):  # 주사위
            new_row = row + dr[i]
            new_col = col + dc[i]

            if new_row < 0 or new_row > n-1 or new_col < 0 or new_col > n-1:
                continue

            if chess_board[new_row][new_col] != -1:  # 이미왔으면
                continue

            chess_board[new_row][new_col] = chess_board[row][col] + 1
            q.append((new_row, new_col))


dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

start = time.time()
n = int(sys.stdin.readline().rstrip())
chess_board = [[-1 for _ in range(n)] for __ in range(n)]
start_r, start_c, end_r, end_c = map(int, sys.stdin.readline().split())
bfs(start_r, start_c)
print(chess_board[end_r][end_c])
print("time:", time.time()-start)
