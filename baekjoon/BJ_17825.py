import sys

# 윷놀이
input = sys.stdin.readline

# 입력 받기
dice_nums = list(map(int, input().split()))
# 4가지 path
location = [x for x in range(37)]
value = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 26, 27,
         28, 30, 35]
# 경로마다 location 집합
path = [[x for x in range(21)] + [32, 33, 34, 35, 36], [5, 21, 22, 23, 24, 30, 31, 20] + [32, 33, 34, 35, 36], \
        [10, 25, 26, 24, 30, 31, 20] + [32, 33, 34, 35, 36],
        [15, 29, 28, 27, 24, 30, 31, 20] + [32, 33, 34, 35, 36]]

existed = [False for _ in range(37)]  # 32~36은 도착점
goal = [False for _ in range(4)]  # 도착 여부
using_path = [0 for _ in range(4)]  # 어떤 경로 사용 중인지..
position = [0 for _ in range(4)]  # 말이 어딨는지..
idx = [0 for _ in range(4)]  # path에서 몇 번째 위치인지


# print(path)


def dfs(turn, score):
    # print(turn, score, position, goal)
    global max_score
    if turn == 10:
        if score > max_score:
            max_score = score

        return

    # dfs
    for horse in range(4):  # 1 ~ 4 번 중 택 1
        if goal[horse]:  # 이미 도착한 말이면 사용 못함
            continue

        if position[horse] == 5:  # loc(5), value(10), 경로 1로 바꿔야함
            now_pos = path[using_path[horse]][idx[horse]]
            now_idx = idx[horse]
            # 경로 1로 변경
            using_path[horse] = 1
            next_idx = 0 + dice_nums[turn]
            next_pos = path[using_path[horse]][next_idx]
            if not existed[next_pos]:  # 갈 곳에 말이 없어야함
                existed[now_pos] = False  # 여길 뜬다
                existed[next_pos] = True  # 여기로 간다
                next_score = score + value[next_pos]
                position[horse] = next_pos
                idx[horse] = next_idx
                #
                dfs(turn + 1, next_score)
                #
                existed[now_pos] = True
                existed[next_pos] = False
                position[horse] = now_pos
                idx[horse] = now_idx
            using_path[horse] = 0

        elif position[horse] == 10:  # loc(10), value(20), 경로 2로 바꿔야함
            now_pos = path[using_path[horse]][idx[horse]]
            now_idx = idx[horse]
            # 경로 2로 변경
            using_path[horse] = 2
            next_idx = 0 + dice_nums[turn]
            next_pos = path[using_path[horse]][next_idx]
            if not existed[next_pos]:  # 갈 곳에 말이 없어야함
                existed[now_pos] = False  # 여길 뜬다
                existed[next_pos] = True  # 여기로 간다
                next_score = score + value[next_pos]
                position[horse] = next_pos
                idx[horse] = next_idx
                #
                dfs(turn + 1, next_score)
                #
                existed[now_pos] = True
                existed[next_pos] = False
                position[horse] = now_pos
                idx[horse] = now_idx
            using_path[horse] = 0

        elif position[horse] == 15:  # loc(15), value(30), 경로 3로 바꿔야함
            now_pos = path[using_path[horse]][idx[horse]]
            now_idx = idx[horse]
            # 경로 3로 변경
            using_path[horse] = 3
            next_idx = 0 + dice_nums[turn]
            next_pos = path[using_path[horse]][next_idx]

            if not existed[next_pos]:  # 갈 곳에 말이 없어야함
                existed[now_pos] = False  # 여길 뜬다
                existed[next_pos] = True  # 여기로 간다
                next_score = score + value[next_pos]
                position[horse] = next_pos
                idx[horse] = next_idx
                #
                dfs(turn + 1, next_score)
                #
                existed[now_pos] = True
                existed[next_pos] = False
                position[horse] = now_pos
                idx[horse] = now_idx
            using_path[horse] = 0

        else:  # 일반적인 상황
            now_pos = path[using_path[horse]][idx[horse]]
            now_idx = idx[horse]
            next_idx = idx[horse] + dice_nums[turn]
            next_pos = path[using_path[horse]][next_idx]
            if next_pos > 31:  # 32~36은 도착점임
                existed[now_pos] = False  # 여길 뜬다
                goal[horse] = True  # 도착했다.
                next_score = score + 0  # 도착점 점수 0
                position[horse] = 32
                idx[horse] = next_idx
                #
                dfs(turn + 1, next_score)
                #
                existed[now_pos] = True
                goal[horse] = False
                position[horse] = now_pos
                idx[horse] = now_idx

            else:  # 일반적인 진행
                if not existed[next_pos]:  # 갈 곳에 말이 없어야함
                    existed[now_pos] = False  # 여길 뜬다
                    existed[next_pos] = True  # 여기로 간다
                    next_score = score + value[next_pos]
                    position[horse] = next_pos
                    idx[horse] = next_idx
                    #
                    dfs(turn + 1, next_score)
                    #
                    existed[now_pos] = True
                    existed[next_pos] = False
                    position[horse] = now_pos
                    idx[horse] = now_idx


# main
max_score = 0
# 처음에 1번 말로 시작(경로 0)
pos = path[using_path[0]][dice_nums[0]]
idx[0] = dice_nums[0]
existed[pos] = True
temp_score = value[pos]
position[0] = pos
dfs(1, temp_score)
print(max_score)
