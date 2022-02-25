c, r = map(int, input().split())
shop_num = int(input())
shop = [[0, 0] for _ in range(shop_num+1)]
clockwise = []
for i in range(shop_num + 1):
    direction, dist = map(int, input().split())
    if direction == 1:  # 북
        shop[i] = [0, dist]
    elif direction == 2:  # 남쪽
        shop[i] = [r, dist]
    elif direction == 3:  # 서쪽
        shop[i] = [dist, 0]
    else:  # 동쪽
        shop[i] = [dist, c]


# 왼쪽으로 돔 clockwise
cnt = 0
row, col = shop[shop_num][0], shop[shop_num][1]
map_length = 2 * (c + r)  # 맵 둘레 30
while cnt < map_length:
    clockwise.append((row, col))

    if row == r:  # 현재 아랫변
        if col == 0:  # 북쪽으로 가야함
            row = row - 1
        else:
            col = col - 1

    elif col == 0:  # 현재 왼쪽 변
        if row == 0:  # 동쪽으로 가야함
            col += 1
        else:
            row -= 1

    elif row == 0:  # 현재 윗 변
        if col == c:  # 남쪽으로 가야함
            row += 1
        else:
            col += 1

    elif col == c:  # 현재 우변
        if row == r:  # 서쪽으로 가야함
            col = col - 1
        else:
            row += 1

    cnt += 1

result = 0
for i in range(shop_num):
    shop_r, shop_c = shop[i]
    for j in range(map_length):
        if shop_r == clockwise[j][0] and shop_c == clockwise[j][1]:
            if j >= map_length // 2:
                result += (map_length - j)
            else:
                result += j

print(result)
