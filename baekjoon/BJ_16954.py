import sys
from collections import deque


def bfs():
    q = deque()
    q.append((7, 0, 0))  # row, col, time
    while q:
        row, col, time = q.popleft()
        for i in range(9):
            n_row, n_col, n_time = row + dr[i], col + dc[i], time + 1
            if 0 <= n_row < 8 and 0 <= n_col < 8:
                # 앞에 비교는 가려는 자리에 이미 벽 있음, 뒤에는 이동하고 벽이 내려와버림
                if arr[n_row-time][n_col] == '#' or arr[n_row - n_time][n_col] == '#':
                    continue
                else:
                    if n_row - n_time < 1:  # 내 위치 보다 벽위치가 같거나 아래면 이제 프리패스임
                        print(n_row, time)
                        return 1
                    q.append((n_row, n_col, n_time))  # row, col, time

    return 0


arr = [sys.stdin.readline().strip() for _ in range(8)]
# 8 방향
dr = (1, 0, -1, 0, -1, -1, 1, 1, 0)
dc = (0, 1, 0, -1, -1, 1, 1, -1, 0)
print(bfs())

# visited가 92%에서 문제를 일으킨듯하다 위의 코드는 되는 코드임
# 더 빨리 탈출 가능함
