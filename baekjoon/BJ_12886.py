import sys
from collections import deque


def bfs():
    q = deque()
    q.append((A, B))
    # 방문 체크
    truth_map[A][B] = True

    while q:
        x, y = q.popleft()
        z = max_stone - x - y

        if x == y == z:
            return 1
        for a, b in (x,y), (x,z), (y,z):  # [(0, 1), (0, 2), (1, 2)]
            if a == b:
                continue
            if a < b:
                b = b - a
                a = 2 * a
            elif a > b:
                a = a - b
                b = 2 * b

            c = max_stone - a - b
            min_num = max(a,b,c)
            max_num = min(a,b,c)
            if not truth_map[min_num][max_num]:
                truth_map[min_num][max_num] = True
                q.append((min_num, max_num))

    return 0


A, B, C = map(int, sys.stdin.readline().split())  # [A,B,C]
max_stone = A + B + C
truth_map = [[False for _ in range(max_stone)] for __ in range(max_stone)]

print(bfs())