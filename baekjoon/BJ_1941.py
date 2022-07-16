# 칠공주
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


# 조합에 도연팀이 4명 이상있으면 안됨
# 그걸 체크
def cal_yeon(el):
    num_y = 0
    for x, y in el:
        if graph[x][y] == 'Y':
            num_y += 1

    if num_y > 3:
        return False
    else:
        return True


# 조합이 인접한 사람들로 이루어져있는지 bfs로 체크
def check(el):
    visited = [False for _ in range(7)]
    q = deque()
    q.append(el[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for d in dxy:
            n_x = x + d[0]
            n_y = y + d[1]
            # 현재 위치에서 인접한 점이 조합에 있다면
            # 인덱스를 찾아서 방문처리해줌
            # 조합에 없으면 다음으로 넘어감
            if (n_x, n_y) in el:
                next_idx = el.index((n_x, n_y))
                if not visited[next_idx]:
                    q.append((n_x, n_y))
                    visited[next_idx] = True

    # bfs 탐색을 다했는데 조합에 있는 점을 모두 방문했으면 인접해있음
    # 아니면 False
    if False in visited:
        return False
    else:
        return True


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = [(i, j) for i in range(5) for j in range(5)]
combi = list(combinations(positions, 7))
graph = [input().rstrip() for _ in range(5)]
ans = 0

# 조합을 돌면서
# 40만개
# 1. 도연팀멤버의 수 체크 4명이상이면 볼 필요없음
# 2. 인접한지 체크해서 인접하면 ans ++
for combi_el in combi:
    if cal_yeon(combi_el):
        if check(combi_el):
            ans += 1

print(ans)
