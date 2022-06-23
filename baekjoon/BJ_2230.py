import sys
input = sys.stdin.readline
# 수고르기
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
s = 0
e = 1

ans = 2*(10**9) + 1
# 투포인타
while s < n and e < n:
    # 1, 3, 5 ㅇ ㅗ름차순
    diff = arr[e] - arr[s]

    # 차이가 원하는거보다 작으면 늘려야
    if diff < m:
        e += 1
        continue

    # 차이가 원하는 거랑 같으면 답
    if diff == m:
        ans = m
        break

    # diff > m
    # 차이가 원하는거보다 크면 줄여야
    ans = min(ans, diff)
    s += 1

print(ans)