import sys
from collections import deque

input = sys.stdin.readline


def move(red_r, red_c, blue_r, blue_c, moving_direction, time):
    # if time > 10:
    #     return red_r, red_c, blue_r, blue_c, -1, time
    if moving_direction == 1:  # 오른쪽 방향
        if red_r == blue_r:  # 같은 row
            if blue_c > red_c:  # 블루가 오른쪽에 있음
                blue_c += 1
                while arr[blue_r][blue_c] != '#':
                    if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_c += 1
                blue_c -= 1
                # 레드 움직임
                red_c += 1
                while arr[red_r][red_c] != '#' and red_c != blue_c:
                    if arr[red_r][red_c] == 'O':  # 성공
                        return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_c += 1
                red_c -= 1
                return red_r, red_c, blue_r, blue_c, 1, time + 1


            else:  # 레드가 오른쪽에 있음
                red_c += 1
                while arr[red_r][red_c] != '#':
                    if arr[red_r][red_c] == 'O':  # 레드는 일단 성공
                        # 블루도 빠지는 지 체크
                        flag = 0
                        blue_c += 1
                        while arr[blue_r][blue_c] != '#':
                            if arr[blue_r][blue_c] == 'O':
                                flag = 1
                                break
                            blue_c += 1
                        blue_c -= 1
                        if flag:  # 블루도 빠져버림
                            return red_r, red_c, blue_r, blue_c, -1, time + 1
                        else:
                            return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_c += 1
                red_c -= 1

                blue_c += 1
                while arr[blue_r][blue_c] != '#' and red_c != blue_c:
                    if arr[blue_r][blue_c] == 'O':  # 블루만 빠져버림 -> 실패
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_c += 1
                blue_c -= 1
                return red_r, red_c, blue_r, blue_c, 1, time + 1

        else:
            blue_c += 1
            while arr[blue_r][blue_c] != '#':
                if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                    return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                blue_c += 1
            blue_c -= 1

            red_c += 1
            while arr[red_r][red_c] != '#':
                if arr[red_r][red_c] == 'O':  # 성공
                    return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                red_c += 1
            red_c -= 1

            return red_r, red_c, blue_r, blue_c, 1, time + 1

    elif moving_direction == 2:
        if red_r == blue_r:  # 같은 row
            if blue_c < red_c:  # 블루가 왼쪽에 있음
                blue_c -= 1
                while arr[blue_r][blue_c] != '#':
                    if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_c -= 1
                blue_c += 1
                # 레드 움직임
                red_c -= 1
                while arr[red_r][red_c] != '#' and red_c != blue_c:
                    if arr[red_r][red_c] == 'O':  # 성공
                        return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_c -= 1
                red_c += 1
                return red_r, red_c, blue_r, blue_c, 2, time + 1


            else:  # 레드가 왼쪽에 있음
                red_c -= 1
                while arr[red_r][red_c] != '#':
                    if arr[red_r][red_c] == 'O':  # 성공
                        flag = 0
                        blue_c -= 1
                        while arr[blue_r][blue_c] != '#':
                            if arr[blue_r][blue_c] == 'O':
                                flag = 1
                                break
                            blue_c -= 1
                        blue_c += 1
                        if flag:  # 블루도 빠져버림
                            return red_r, red_c, blue_r, blue_c, -1, time + 1
                        else:
                            return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_c -= 1
                red_c += 1

                blue_c -= 1
                while arr[blue_r][blue_c] != '#' and red_c != blue_c:
                    if arr[blue_r][blue_c] == 'O':  # 블루만 빠져버림 -> 실패
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_c -= 1
                blue_c += 1
                return red_r, red_c, blue_r, blue_c, 2, time + 1

        else:
            blue_c -= 1
            while arr[blue_r][blue_c] != '#':
                if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                    return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                blue_c -= 1
            blue_c += 1

            red_c -= 1
            while arr[red_r][red_c] != '#':
                if arr[red_r][red_c] == 'O':  # 성공
                    return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                red_c -= 1
            red_c += 1

            return red_r, red_c, blue_r, blue_c, 2, time + 1

    elif moving_direction == 3:  # 북쪽
        if red_c == blue_c:  # 같은 col
            if blue_r < red_r:  # 블루가 위에 있음
                blue_r -= 1
                while arr[blue_r][blue_c] != '#':
                    if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_r -= 1
                blue_r += 1
                # 레드 움직임
                red_r -= 1
                while arr[red_r][red_c] != '#' and red_r != blue_r:
                    if arr[red_r][red_c] == 'O':  # 성공
                        return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_r -= 1
                red_r += 1
                return red_r, red_c, blue_r, blue_c, 3, time + 1

            else:  # 레드가 위쪽에 있음
                red_r -= 1
                while arr[red_r][red_c] != '#':
                    if arr[red_r][red_c] == 'O':  # 성공
                        flag = 0
                        blue_r -= 1
                        while arr[blue_r][blue_c] != '#':
                            if arr[blue_r][blue_c] == 'O':
                                flag = 1
                                break
                            blue_r -= 1
                        blue_r += 1
                        if flag:  # 블루도 빠져버림
                            return red_r, red_c, blue_r, blue_c, -1, time + 1
                        else:
                            return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_r -= 1
                red_r += 1

                blue_r -= 1
                while arr[blue_r][blue_c] != '#' and red_r != blue_r:
                    if arr[blue_r][blue_c] == 'O':  # 블루만 빠져버림 -> 실패
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_r -= 1
                blue_r += 1
                return red_r, red_c, blue_r, blue_c, 3, time + 1

        else:
            blue_r -= 1
            while arr[blue_r][blue_c] != '#':
                if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                    return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                blue_r -= 1
            blue_r += 1

            red_r -= 1
            while arr[red_r][red_c] != '#':
                if arr[red_r][red_c] == 'O':  # 성공
                    return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                red_r -= 1
            red_r += 1

            return red_r, red_c, blue_r, blue_c, 3, time + 1

    else:  # 4남쪽
        if red_c == blue_c:  # 같은 col
            if blue_r > red_r:  # 블루가 아래에 있음
                blue_r += 1
                while arr[blue_r][blue_c] != '#':
                    if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_r += 1
                blue_r -= 1
                # 레드 움직임
                red_r += 1
                while arr[red_r][red_c] != '#' and red_r != blue_r:
                    if arr[red_r][red_c] == 'O':  # 성공
                        return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_r += 1
                red_r -= 1
                return red_r, red_c, blue_r, blue_c, 4, time + 1

            else:  # 레드가 아래쪽에 있음
                red_r += 1
                while arr[red_r][red_c] != '#':
                    if arr[red_r][red_c] == 'O':  # 성공
                        flag = 0
                        blue_r += 1
                        while arr[blue_r][blue_c] != '#':
                            if arr[blue_r][blue_c] == 'O':
                                flag = 1
                                break
                            blue_r += 1
                        blue_r -= 1
                        if flag:  # 블루도 빠져버림
                            return red_r, red_c, blue_r, blue_c, -1, time + 1
                        else:
                            return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                    red_r += 1
                red_r -= 1

                blue_r += 1
                while arr[blue_r][blue_c] != '#' and red_r != blue_r:
                    if arr[blue_r][blue_c] == 'O':  # 블루만 빠져버림 -> 실패
                        return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                    blue_r += 1
                blue_r -= 1
                return red_r, red_c, blue_r, blue_c, 4, time + 1

        else:
            blue_r += 1
            while arr[blue_r][blue_c] != '#':
                if arr[blue_r][blue_c] == 'O':  # 먼저 빠져버림
                    return red_r, red_c, blue_r, blue_c, -1, time + 1  # -1은 실패표시
                blue_r += 1
            blue_r -= 1

            red_r += 1
            while arr[red_r][red_c] != '#':
                if arr[red_r][red_c] == 'O':  # 성공
                    return red_r, red_c, blue_r, blue_c, -2, time + 1  # -2는 성공표시
                red_r += 1
            red_r -= 1

            return red_r, red_c, blue_r, blue_c, 4, time + 1


def bfs():
    while q:
        r_r, r_c, b_r, b_c, direction, t = q.popleft()

        if direction == 0:
            for i in range(1, 5):
                n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t = move(r_r, r_c, b_r, b_c, i, t)

                if n_d == -1:  # 실패
                    continue
                elif n_d == -2:  # 성공
                    return print(1)
                else:
                    if n_t == 10:
                        continue
                    else:
                        q.append((n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t))

        elif direction == 1 or direction == 2:  # 좌, 우
            for i in [3, 4]:
                n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t = move(r_r, r_c, b_r, b_c, i, t)
                if n_d == -1:  # 실패
                    continue
                elif n_d == -2:  # 성공
                    return print(1)
                else:
                    if n_t == 10:
                        continue
                    else:
                        q.append((n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t))

        else:  # 상, 하
            for i in [1, 2]:
                n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t = move(r_r, r_c, b_r, b_c, i, t)
                if n_d == -1:  # 실패
                    continue
                elif n_d == -2:  # 성공
                    return print(1)
                else:
                    if n_t == 10:
                        continue
                    else:
                        q.append((n_r_r, n_r_c, n_b_r, n_b_c, n_d, n_t))

    return print(0)


row, col = map(int, input().split())
arr = ['' for __ in range(row)]
for i in range(row):
    arr[i] = list(input().rstrip())

q = deque()
for i in range(row):
    for j in range(col):
        if arr[i][j] == 'R':
            red_r, red_c = i, j
        if arr[i][j] == 'B':
            blue_r, blue_c = i, j

q.append((red_r, red_c, blue_r, blue_c, 0, 0))
bfs()


