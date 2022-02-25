import sys
from collections import deque
sys.stdin = open("test.txt")

for tc in range(1, 11):
    tc = int(input())
    arr = list(map(int, input().split()))
    q = deque(arr)
    flag = 1
    while flag:
        for i in range(1, 6):  # 한 사이클
            q.append(q.popleft()-i)
            if q[-1] <= 0:
                q[-1] = 0
                flag = 0
                break

    print(f'#{tc}',*q)