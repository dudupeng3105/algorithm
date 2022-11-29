import sys
from collections import deque
input = sys.stdin.readline

# 다음 차가 못 들어갈때도 dummy를 넣어서 시뮬레이션 구현
# 트럭수, 다리길이, 최대하중
n, w, l = map(int, input().split())

trucks = list(map(int, input().split()))

# 다리길이 - 1 만큼 dummy 채워놈
q = deque()
for _ in range(w):
    q.append(0)

weight = 0
idx = 0
cnt = 0
while q:
    cnt += 1
    # 하나 뺌
    weight -= q.popleft()
    # print(q)

    if idx < n:
        truck = trucks[idx]
        if weight + truck <= l:
            q.append(truck)
            weight += truck
            idx += 1
        else:
            q.append(0)

print(cnt)