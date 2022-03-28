import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().split())
arr = [[0 for _ in range(col)] for __ in range(row)]
value_map = [[0 for _ in range(col)] for __ in range(row)]
for i in range(row):
    k = list(map(int, input().split()))
    arr[i] = k
    value_map[i] = k

print(value_map)

q = deque()
q.append((0, 0, arr[0][0], -1))  # r, c, sum_value
value_map[0][0] = arr[0][0]
dr = [1, 0, 0]
dc = [0, -1, 1]


def bfs():
    max_value = 0
    while q:
        r, c, sum_value, before_direction = q.popleft()
        print(r,c)
        if r == row - 1 and c == col - 1:
            if sum_value > max_value:
                max_value = sum_value
            continue

        for i in range(3):
            if i != before_direction:
                n_r, n_c = r + dr[i], c + dc[i]
                if 0 <= n_r < row and 0 <= n_c < col:
                    new_value = sum_value + arr[n_r][n_c]
                    q.append((n_r, n_c, new_value, i))

    return max_value
bfs()
print(value_map)