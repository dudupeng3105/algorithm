n, k = map(int, input().split())

coin_lst = []
for _ in range(n):
    coin_lst.append(int(input()))

cnt = 0
for coin in coin_lst[::-1]:
    if coin > k:
        continue
    else:
        cnt += (k // coin)
        k -= coin * (k // coin)

    if k == 0:
        break

print(cnt)
