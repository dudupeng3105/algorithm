n, m = map(int, input().split())

s = []
for _ in range(n):
    s.append(input())

ans = 0
for _ in range(m):
    test_str = input()
    if test_str in s:
        ans += 1

print(ans)