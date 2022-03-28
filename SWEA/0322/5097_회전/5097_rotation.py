from collections import deque


def work(q):
    a = q.popleft()
    q.append(a)
    return q


test_case = int(input())
for tc in range(1, test_case+1):
    n, m = map(int, input().split())
    que = deque(list(map(int, input().split())))
    for _ in range(m):
        que = work(que)

    print(f'#{tc} {que[0]}')