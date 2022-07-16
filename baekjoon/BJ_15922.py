n = int(input())
end = -2000000000
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y < end:
        continue
    elif x < end:
        ans += (y - end)
    else:
        ans += (y - x)

    end = y

print(ans)