def solution(n, build_frame):
    arr = [[[False, False] for _ in range(n + 1)] for __ in range(n + 1)]

    def pillar_safety_check(col, row):
        if not arr[col][row][0]:  # 없으면 안전체크 할 필요없고 True
            return True
        if row == 0:
            return True
        elif arr[col][row - 1][0] or arr[col - 1][row][1] or arr[col][row][1]:
            return True
        return False

    def beam_safety_check(col, row):
        if not arr[col][row][1]:  # 없으면 안전체크 할 필요없고 True
            return True
        if arr[col][row - 1][0] or arr[col + 1][row - 1][0]:
            return True
        elif arr[col - 1][row][1] and arr[col + 1][row][1]:
            return True
        return False

    for work in build_frame:
        # 가능한지 체크
        x, y, a, b = work
        if b == 1:  # 설치
            if a == 0:  # pillar
                arr[x][y][0] = True
                if not pillar_safety_check(x, y):
                    arr[x][y][0] = False  # 다시 되돌림(안전하지않으니까)

            else:  # a == 1(beam)
                arr[x][y][1] = True
                if not beam_safety_check(x, y):
                    arr[x][y][1] = False

        else:  # 삭제
            if a == 0:  # pillar  #
                arr[x][y][0] = False
                flag = pillar_safety_check(x, y + 1) and beam_safety_check(x, y + 1) and beam_safety_check(x - 1, y + 1)
                if not flag:  # 위험함, 지우면 안됨
                    arr[x][y][0] = True

            else:  # a == 1(beam)
                arr[x][y][1] = False
                flag = pillar_safety_check(x, y) and pillar_safety_check(x + 1, y) and beam_safety_check(x - 1, y) \
                       and beam_safety_check(x + 1, y)
                if not flag:  # 위험함, 지우면 안됨
                    arr[x][y][1] = True

    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            for el_type in range(2):
                if arr[x][y][el_type]:
                    answer.append([x, y, el_type])

    return answer
