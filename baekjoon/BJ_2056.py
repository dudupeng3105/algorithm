# 2056 작업
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[]] + [[] for _ in range(n)]
inner_arrows = [0] + [0 for _ in range(n)]
time = [0] + [0 for _ in range(n)]
for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    inner_arrows[i] = info[1]
    for j in range(2, 2 + info[1]):
        graph[info[j]].append(i)

# print(graph)
# print(inner_arrows)
# print(time)

# inner_arrows = 0 찾기
# bfs 1시간 단위
q = deque()
for i in range(1, n + 1):
    if inner_arrows[i] == 0:
        q.append((i, time[i]))

total_time = 0
while q:
    total_time += 1  # 1시간 단위로 함
    for _ in range(len(q)):  # 현재 시간에 들어있는 q길이만큼만 q.pop함
        # 왜냐하면 중간에 작업이 끝나고 다음 일을 q에 담는데 이거는 +1 시간에
        # 할 것이기 때문
        work_num, time_left = q.popleft()
        if time_left == 1:  # 이번이 마지막 time임
            for next_work in graph[work_num]:
                inner_arrows[next_work] -= 1
                if not inner_arrows[next_work]:
                    q.append((next_work, time[next_work]))
        else:
            q.append((work_num, time_left - 1))

print(total_time)
