from collections import deque


def operation(op, n):
    if op == 1:  # +1
        n += 1
        return n
    elif op == 2:   # -1
        n -= 1
        return n
    elif op == 3:   # *2
        n = n * 2
        return n
    else:  # -10
        n = n - 10
        return n


def bfs(a):
    q = deque()
    q.append((a, 0))
    visited = [False for _ in range(-10, 2*b + 1)]
    visited[a] = True
    while q:
        num, cnt = q.popleft()
        for i in range(4):
            next_num = operation(i, num)
            if next_num == b:
                return cnt + 1
            if -10 <= next_num <= 2*b and not visited[next_num]:
                visited[next_num] = True
                q.append((next_num, cnt +1))

    return


test_case = int(input())
for tc in range(1, test_case+1):
    a, b = map(int, input().split())
    print(f'#{tc} {bfs(a)}')