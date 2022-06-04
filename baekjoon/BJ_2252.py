import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inner_arrows = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inner_arrows[b] += 1

q = deque()
for i in range(1, n+1):
    if inner_arrows[i] == 0:
        q.append(i)

result = []
while q:
    student_num = q.popleft()
    result.append(student_num)
    for next_student_num in graph[student_num]:
        inner_arrows[next_student_num] -= 1
        if inner_arrows[next_student_num] == 0:
            q.append(next_student_num)

print(*result)