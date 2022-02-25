c, r = map(int, input().split())
shop_num = int(input())
shop = [[0, 0] for _ in range(shop_num+1)]
for i in range(shop_num + 1):
    shop[i][0], shop[i][1] = map(int, input().split())

pos, length = shop[shop_num][0], shop[shop_num][1]
map_length = 2 * (c + r)  # 맵 둘레 30
result = 0
for i in range(shop_num):
    direction, dist = shop[i][0], shop[i][1]

    if pos == 1:  # 북쪽에 동근
        if direction == 1:  # 북
            result += abs(length-dist)
        elif direction == 2:  # 남
            result += min(length + r + dist, map_length - (length + r + dist))
        elif direction == 3:  # 서
            result += length + dist
        elif direction == 4:  # 동
            result += (c-length) + dist

    elif pos == 2:  # 남쪽에 동근
        if direction == 1:  # 북
            result += min(length + r + dist, map_length - (length + r + dist))
        elif direction == 2:  # 남
            result += abs(length-dist)
        elif direction == 3:  # 서
            result += length + (r-dist)
        elif direction == 4:  # 동
            result += (c - length) + (r-dist)

    elif pos == 3:  # 서쪽에 동근
        if direction == 1:  # 북
            result += length + dist
        elif direction == 2:  # 남
            result += (c-length) + dist
        elif direction == 3:  # 서
            result += abs(length-dist)
        elif direction == 4:  # 동
            result += min(length + c + dist, map_length - (length + c + dist))

    elif pos ==4:  # 동쪽에 동근
        if direction == 1:  # 북
            result += length + (c-dist)
        elif direction == 2:  # 남
            result += (c - length) + (c-dist)
        elif direction == 3:  # 서
            result += min(length + c + dist, map_length - (length + c + dist))
        elif direction == 4:  # 동
            result += abs(length - dist)


print(result)

