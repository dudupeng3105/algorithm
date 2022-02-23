for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # dot_cnt 계산 dot_cnt -> 한 점의 x,y 중 하나라도 다른 직사각형의 점의 좌표와 같은 경우

    # d 공통없음
    if x2 > p1 or p2 < x1 or y2 > q1 or q2 < y1:
        print('d')

    # 점(dot_cnt ==2), 선분(dot_cnt ==1)
    elif ((x1, y1) == (p2, q2)) or ((p1, y1) == (x2, q2)) or ((p1, q1) == (x2, y2)) or \
                ((x1, q1) == (p2, y2)):
        print('c')

    elif y2 == q1 or y1 == q2 or p1 == x2 or x1 == p2:
        print('b')

        # 나머지 직사각형
    else:
        print('a')
