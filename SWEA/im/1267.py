import sys
from collections import defaultdict, deque

sys.stdin = open("test.txt")

for tc in range(1, 11):
    v, e = map(int, input().split())
    cnt = [0 for _ in range(v + 1)]  # 자기한테 들어오는 화살표의 개수
    arr = defaultdict(list)
    edges_lst = list(map(int, input().split()))
    for i in range(e):  # a 출발, b 도착
        a, b = edges_lst[2 * i], edges_lst[2 * i + 1]
        arr[a].append(b)
        cnt[b] += 1

    # bfs 쓰기
    # 1. 출발점 --> 들어오는 화살표가 없는 정점
    q = deque()  # 큐 선언
    for j in range(1, v + 1):
        if cnt[j] == 0:  # 들어오는 화살표가 없는 정점
            q.append(j)

    visited = [False for _ in range(v + 1)]
    result = []
    # 2.bfs
    while q:
        work = q.popleft()
        result.append(work)

        for next_work in arr[work]:
            if not visited[next_work]:
                cnt[next_work] -= 1
                if cnt[next_work] < 1:
                    # cnt 가 0 되야 비로소 방문가능
                    visited[next_work] = True
                    q.append(next_work)
                else:  # cnt가 아직 남으면 안넣음
                    continue

    print(f'#{tc}', *result)
