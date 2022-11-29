import sys

input = sys.stdin.readline


def det(ref_r, ref_c, row, col):
    diff_r = ref_r - row
    diff_c = ref_c - col
    if diff_c == 0:  # 같은 열
        if diff_r > 0:
            return 2  # 아래쪽 방향
        else:
            return 8  # 위쪽 방향
    elif diff_r == 0:
        if diff_c > 0:
            return 6  # 오른쪽 방향
        else:
            return 4  # 왼쪽 방향
    else:
        if diff_c > 0:  # 오른
            if diff_r > 0:  # 아래
                return 3
            else:  # diff_r < 0:  # 위로
                return 9

        else:  # diff_c < 0  # 왼쪽
            if diff_r > 0:  # 아래
                return 1
            else:  # diff_r < 0:  # 위로
                return 7


r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
jongsu = list(map(int, input().rstrip()))
mad_arduino = []

# where is a jongsu's arduino..
j_r, j_c = 0, 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'I':
            j_r, j_c = i, j
        elif arr[i][j] == 'R':
            mad_arduino.append((i, j))

drc = [(0, 0), (1, -1), (1, 0), (1, 1), (0, -1), \
       (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

bomb = []
for turn in range(len(jongsu)):
    # 1. 종수 아두이노 이동
    move = jongsu[turn]
    dr, dc = drc[move]
    j_r, j_c = j_r + dr, j_c + dc
    # 이동한 칸에 아두이노 있으면 게임 종료
    if (j_r, j_c) in mad_arduino:
        if (j_r, j_c) not in bomb:
            print('kraj', turn+1)
            sys.exit(0)

    # 2. 미친 아두이노 이동
    # 그 자리에 미친 또다른 아두이노가 있었으면
    # 그 칸을 기록해놨다가 미친 아두이노 다 하면 터트림
    # 종수있는칸으로 가면 게임 종료
    new_mad_arduino = []
    new_bomb = []
    for arduino in mad_arduino:
        i, j = arduino
        if (i, j) in bomb:  # bomb면 이미 터진거
            continue
        direction = det(j_r, j_c, i, j)
        dr, dc = drc[direction]
        n_i, n_j = i + dr, j + dc
        if n_i == j_r and n_j == j_c:
            print('kraj', turn+1)
            sys.exit(0)

        elif (n_i, n_j) in new_mad_arduino:  # 있으면 터진거
            new_bomb.append((n_i, n_j))
            continue

        else:
            new_mad_arduino.append((n_i, n_j))

    bomb = [new_bomb[i][::] for i in range(len(new_bomb))]
    mad_arduino = [new_mad_arduino[i][::] for i in range(len(new_mad_arduino))]

# print("결과")

ans = [['.' for _ in range(c)] for __ in range(r)]

for arduino in mad_arduino:
    i, j = arduino
    # 폭탄처리
    if (i, j) not in bomb:
        ans[i][j] = 'R'

ans[j_r][j_c] = 'I'
for i in range(r):
    print(*ans[i], sep='')

