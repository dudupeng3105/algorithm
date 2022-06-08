import sys
import math
input = sys.stdin.readline


def cal_slope_intercept(x_1, y_1, x_2, y_2):
    vertical_x = 0.1  # 정수만 들어오니까 이걸로 y축 수평여부 판단 가능
    slope = 0
    intercept = 0
    if x_2 == x_1:  # x=4 같은 상황
        vertical_x = x_1
    else:
        slope = (y_2 - y_1) / (x_2 - x_1)
        intercept = -slope * x_1 + y_1

    return slope, intercept, vertical_x


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# ax + b = cx + d
a, b, v1 = cal_slope_intercept(x1, y1, x2, y2)
c, d, v2 = cal_slope_intercept(x3, y3, x4, y4)
line1_x_smaller = min(x1, x2)
line1_x_bigger = max(x1, x2)
line2_x_smaller = min(x3, x4)
line2_x_bigger = max(x3, x4)
second_smaller = max(line1_x_smaller, line2_x_smaller)  # 덜 작은거
second_bigger = min(line1_x_bigger, line2_x_bigger)  # 덜 큰거

if v1 != 0.1 or v2 != 0.1:  # 하나라도 y축에 평행한 직선
    line1_y_smaller = min(y1, y2)
    line1_y_bigger = max(y1, y2)
    line2_y_smaller = min(y3, y4)
    line2_y_bigger = max(y3, y4)
    second_smaller = max(line1_y_smaller, line2_y_smaller)  # 덜 작은거
    second_bigger = min(line1_y_bigger, line2_y_bigger)  # 덜 큰거
    if v1 != 0.1 and v2 != 0.1:  # 둘다 평행한 직선
        if v1 == v2:  # 둘다 평행
            if second_smaller <= second_bigger:
                print(1)
            else:
                print(0)
        else:
            print(0)

    elif v1 != 0.1:  # line 1이 y축에 평행
        if line2_x_smaller <= x1 <= line2_x_bigger:  # 이 사이에 있어야 만날 수 있음
            cross_y = c * x1 + d
            # print(cross_y)
            if line1_y_smaller <= cross_y <= line1_y_bigger:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:  # v2 != 0.1
        if line1_x_smaller <= x3 <= line1_x_bigger:  # 이 사이에 있어야 만날 수 있음
            cross_y = a * x3 + b
            # print(cross_y)
            line2_y_smaller = min(y3, y4)
            line2_y_bigger = max(y3, y4)
            if line2_y_smaller <= cross_y <= line2_y_bigger:
                print(1)
            else:
                print(0)
        else:
            print(0)

elif a == c:  # 기울기 같음
    if b == d:  # 절편도 같다면..
        if second_smaller <= second_bigger:
            print(1)
        else:
            print(0)
    else:  # 절편 다르면 만날수가없음
        print(0)

else:
    x = (d - b) / (a - c)
    if line1_x_smaller <= x <= line1_x_bigger and \
            line2_x_smaller <= x <= line2_x_bigger:
        print(1)
    else:
        print(0)
