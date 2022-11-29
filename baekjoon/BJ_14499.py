import sys

input = sys.stdin.readline

R, C, r, c, op_num = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
op_lst = list(map(int, input().split()))

# 0~5번면 0,3 / 1,4 / 2,5 가 마주보고 있음
# 동 서 남 북
# top(윗면, 0), north(1), left(2), bottom(아랫면)(3), south(4), right(5)
# 동 : right -> bottom, left -> top, bottom -> left, top -> right
# 서 : left -> bottom, right -> top, bottom -> right,  top -> left
# 남 : top -> south, bottom -> north, north -> top, south -> bottom
# 북 : top -> north, bottom -> south, north -> bottom, south -> top
#
dice_moving_map = [[5, 1, 0, 2, 4, 3], [2, 1, 3, 5, 4, 0], [4, 0, 2, 1, 3, 5], [1, 3, 2, 4, 0, 5]]
dice_num = [0, 0, 0, 0, 0, 0]
for i in range(op_num):
    op = op_lst[i]
    if op == 1:  # 동
        r, c = r, c + 1
        if 0 <= r < R and 0 <= c < C:
            # 굴림
            new_dice_num = [0, 0, 0, 0, 0, 0]
            for k in range(6):
                new_dice_num[k] = dice_num[dice_moving_map[op-1][k]]
            dice_num = new_dice_num[::]
            map_num = arr[r][c]
            # 이동한 칸의 수가 0이면 주사위의 수가 복사
            if not map_num:
                arr[r][c] = dice_num[3]
            # 이동한 칸의 수가 0이 아니면 주사위로 복사되고, 칸의 수가 0이됨
            else:
                dice_num[3] = map_num
                arr[r][c] = 0
        else:
            # 아예 이동을 안함
            r, c = r, c - 1
            continue

    elif op == 2:  # 서
        r, c = r, c - 1
        if 0 <= r < R and 0 <= c < C:
            # 굴림
            new_dice_num = [0, 0, 0, 0, 0, 0]
            for k in range(6):
                new_dice_num[k] = dice_num[dice_moving_map[op - 1][k]]
            dice_num = new_dice_num[::]
            map_num = arr[r][c]
            # 이동한 칸의 수가 0이면 주사위의 수가 복사
            if not map_num:
                arr[r][c] = dice_num[3]
            # 이동한 칸의 수가 0이 아니면 주사위로 복사되고, 칸의 수가 0이됨
            else:
                dice_num[3] = map_num
                arr[r][c] = 0
        else:
            # 아예 이동을 안함
            r, c = r, c + 1
            continue

    elif op == 3:  # 북
        r, c = r - 1, c
        if 0 <= r < R and 0 <= c < C:
            # 굴림
            new_dice_num = [0, 0, 0, 0, 0, 0]
            for k in range(6):
                new_dice_num[k] = dice_num[dice_moving_map[op - 1][k]]
            dice_num = new_dice_num[::]
            map_num = arr[r][c]
            # 이동한 칸의 수가 0이면 주사위의 수가 복사
            if not map_num:
                arr[r][c] = dice_num[3]
            # 이동한 칸의 수가 0이 아니면 주사위로 복사되고, 칸의 수가 0이됨
            else:
                dice_num[3] = map_num
                arr[r][c] = 0
        else:
            # 아예 이동을 안함
            r, c = r + 1, c
            continue

    else:  # 4  # 남
        r, c = r + 1, c
        if 0 <= r < R and 0 <= c < C:
            # 굴림
            new_dice_num = [0, 0, 0, 0, 0, 0]
            for k in range(6):
                new_dice_num[k] = dice_num[dice_moving_map[op - 1][k]]
            dice_num = new_dice_num[::]
            map_num = arr[r][c]
            # 이동한 칸의 수가 0이면 주사위의 수가 복사
            if not map_num:
                arr[r][c] = dice_num[3]
            # 이동한 칸의 수가 0이 아니면 주사위로 복사되고, 칸의 수가 0이됨
            else:
                dice_num[3] = map_num
                arr[r][c] = 0
        else:
            # 아예 이동을 안함
            r, c = r - 1, c
            continue

    print(dice_num[0])
