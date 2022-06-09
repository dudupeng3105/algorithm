import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    # ab x ac = (0, 0, (x2-x1)(y3-y1) - (x3-x1)(y2-y1)
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def calculate():
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    # 평행
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        # 포함관계 체크
        if small_x1 <= bigger_x2 and small_x2 <= bigger_x1 and small_y1 <= bigger_y2 and small_y2 <= bigger_y1:
            return 1
    # 교차
    else:
        # 12를 기준으로 3 과 4의 위치가 정반대, 34를 기준으로 1과 2의 위치가 정반대(시계, 반시계)
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return 1

    return 0


x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))

small_x1, small_y1, bigger_x1, bigger_y1 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
small_x2, small_y2, bigger_x2, bigger_y2 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

print(calculate())