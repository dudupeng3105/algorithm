# 9763 마을의 친밀도
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y, z = map(int, input().split())
    arr.append((x, y, z))

# ? -- center -- ? / min 1, min 2
ans = 10010
for center in range(n):
    min_1 = 5000
    min_2 = 5010
    for j in range(n):
        if not j == center:  # 자기자신은 할 필요 없다
            dist = abs(arr[center][0] - arr[j][0]) \
                   + abs(arr[center][1] - arr[j][1]) + abs(arr[center][2] - arr[j][2])
            if dist >= min_2:
                continue
            elif dist <= min_1:
                # min_1 <-dist, min_2 <-min_1
                min_1, min_2 = min_2, min_1
                min_1 = dist
            else:  # min_1 < dist < min_2
                min_2 = dist
    temp = min_1 + min_2
    if temp < ans:
        ans = temp

print(ans)
