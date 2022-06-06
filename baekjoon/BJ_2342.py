import sys

input = sys.stdin.readline

next_pos = list(map(int, input().split()))
# 5 * 5 - (0,0), (1,1)... = 20개
before_foots = [[999999 for _ in range(5)] for _ in range(5)]

# 처음 한 번 실행 (0,0) 이라서
pos = next_pos[0]
now_l = 0
now_r = 0
# 왼발 선택
next_l = pos
next_r = now_r
before_foots[next_l][next_r] \
    = min(before_foots[next_l][next_r], 2)
# 오른발 선택
next_l = now_l
next_r = pos
before_foots[next_l][next_r] \
    = min(before_foots[next_l][next_r], 2)

# print(before_foots)
# 반복
after_foots = [[999999 for _ in range(5)] for _ in range(5)]
for i in range(1, len(next_pos)-1):
    pos = next_pos[i]
    for l in range(5):  # 왼발
        for r in range(5):  # 오른발
            if l == r:
                continue
            if before_foots[l][r] == 999999:
                continue
            now_l = l
            now_r = r
            now_power = before_foots[now_l][now_r]
            # 왼발 선택
            next_l = pos
            next_r = now_r
            if next_l == next_r:  # 발 위치 같으면 안됨
                pass
            else:
                if now_l == 0:  #
                    add_power = 2
                elif now_l == next_l:
                    add_power = 1
                elif (now_l + next_l) % 2 == 0:  # 반대 위치로감
                    add_power = 4
                else:
                    add_power = 3
                after_foots[next_l][next_r] = min(after_foots[next_l][next_r], now_power+add_power)
            # 오른발 선택
            next_l = now_l
            next_r = pos
            if next_l == next_r:  # 발 위치 같으면 안됨
                pass
            else:
                if now_r == 0:  #
                    add_power = 2
                elif now_r == next_r:
                    add_power = 1
                elif (now_r + next_r) % 2 == 0:  # 반대 위치로감
                    add_power = 4
                else:
                    add_power = 3
                after_foots[next_l][next_r] = min(after_foots[next_l][next_r], now_power+add_power)

    # after->before, after 초기화
    # print(after_foots)
    before_foots = after_foots
    after_foots = [[999999 for _ in range(5)] for _ in range(5)]

result = 999999
for i in range(1, 5):
    result = min(min(before_foots[i]), result)
print(result)

