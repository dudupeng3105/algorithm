import sys
import math
input = sys.stdin.readline

# x in (1, 1000)
# 0.301 * x              0.301 * 106
# round(0.301 * x)    31.906(32)
# 32 / 106 = 0.30188 => 0.301 ok...


n = int(input())
avgs = []
for _ in range(n):
    avgs.append(float(input()))

for num in range(1, 10000):
    cnt = 0
    for i in range(n):
        avg = avgs[i]
        if avg == 0.000:
            cnt += 1
            continue

        total_score = round(avg * num)

        # 맞는지 체크..
        cal_avg = (math.floor((total_score*1000/num))/1000)
        if cal_avg == avg:
            cnt += 1
            continue

    if cnt == n:
        print(num)
        break

# print(ans)
# print(max(ans))
