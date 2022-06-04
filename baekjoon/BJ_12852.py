import sys
from collections import deque

input = sys.stdin.readline


def bfs(num):
    q = deque()
    q.append((num, [num]))  # num, cnt, path
    visited[num] = 0
    while q:
        old_num, path = q.popleft()
        for i in range(3):
            if i == 0:  # //3
                if not old_num % 3:  # 3으로 나누어지면
                    next_num = old_num // 3
                    if visited[next_num] > visited[old_num] + 1:
                        visited[next_num] = visited[old_num] + 1
                        q.append((next_num, path + [next_num]))
                        if next_num == 1:
                            return visited[next_num], path + [next_num]
                    continue

            elif i == 1:  # //2
                if not old_num % 2:  # 3으로 나누어지면
                    next_num = old_num // 2
                    if visited[next_num] > visited[old_num] + 1:
                        visited[next_num] = visited[old_num] + 1
                        q.append((next_num, path + [next_num]))
                        if next_num == 1:
                            return visited[next_num], path + [next_num]
                    continue

            else:  # -1
                next_num = old_num - 1
                if visited[next_num] > visited[old_num] + 1:
                    visited[next_num] = visited[old_num] + 1
                    q.append((next_num, path + [next_num]))
                    if next_num == 1:
                        return visited[next_num], path + [next_num]
                continue


n = int(input())
visited = [100 for _ in range(n+1)]
if n == 1:
    print(0)
    print(1)
else:
    cnt, ans_path = bfs(n)
    print(cnt)
    print(*ans_path)
