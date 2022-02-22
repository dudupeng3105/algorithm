import sys
from collections import deque


def bfs():
    q = deque()
    q.append((7, 0, 0))  # row, col, time
    while q:
        row, col, time = q.popleft()
        n_time = time + 1
        for i in range(8):
            n_row, n_col = row + dr[i], col + dc[i]
            if 0 <= n_row < 8 and 0 <= n_col < 8:
                if arr[n_row - time][n_col] == '#' or arr[n_row - n_time][n_col] == '#':
                    continue
                else:
                    if n_row - n_time < 1:  # 내 위치 보다 벽위치가 같거나 아래면 이제 프리패스임                        p
                        return 1
                    q.append((n_row, n_col, n_time))  # row, col, time

        # 대기 할 때
        if arr[row - n_time][col] == '#':
            continue
        else:
            q.append((row, col, n_time))

    return 0


arr = [sys.stdin.readline().strip() for _ in range(8)]
# 8 방향
dr = (1, 0, -1, 0, -1, -1, 1, 1)
dc = (0, 1, 0, -1, -1, 1, 1, -1)
print(bfs())
