n, k = map(int, input().split())
cnt = [0 for _ in range(12)]  # 1여, 1남, 2여, 2남 ....
for _ in range(n):
    s, y = map(int, input().split())
    cnt[2 * (y - 1) + s] += 1

result = 0
for i in range(12):
    result += (cnt[i] + k - 1) // k
print(result)