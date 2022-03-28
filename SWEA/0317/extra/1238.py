# 1238 contact
import sys
from collections import defaultdict, deque

sys.stdin = open("../../0316/extra/test.txt")

for tc in range(1, 11):
    given_data_length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = defaultdict(list)
    dist_map = [0 for _ in range(101)]
    for i in range(given_data_length // 2):
        a, b = arr[2 * i], arr[2 * i + 1]
        graph[a].append(b)

    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not dist_map[next_node]:
                q.append(next_node)
                dist_map[next_node] = dist_map[node] + 1

    # max 값 구하기
    max_dist = max(dist_map)
    for i in range(100,0,-1):  # 100~1 역순 탐색
        if dist_map[i] == max_dist:
            print(f'#{tc} {i}')
            break
