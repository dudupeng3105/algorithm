import sys
import itertools

input = sys.stdin.readline


def calScore(hit_res):
    # return add_score, add_out
    global base_state

    tmp_add_score = 0
    tmp_add_out = 0
    # 아웃
    if hit_res == 0:
        tmp_add_score = 0
        tmp_add_out = -1

        # 1루타
    elif hit_res == 1:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            base_state[1] = False
            base_state[2] = True
        if base_state[0]:
            base_state[0] = False
            base_state[1] = True
        base_state[0] = True

    # 2루타
    elif hit_res == 2:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            base_state[0] = False
            base_state[2] = True
        base_state[1] = True

    # 3루타
    elif hit_res == 3:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            tmp_add_score += 1
            base_state[0] = False
        base_state[2] = True

    # 홈런
    elif hit_res == 4:
        if base_state[2]:
            tmp_add_score += 1
            base_state[2] = False
        if base_state[1]:
            tmp_add_score += 1
            base_state[1] = False
        if base_state[0]:
            tmp_add_score += 1
            base_state[0] = False
        tmp_add_score += 1

    return tmp_add_score, tmp_add_out


INNING_NUM = int(input())

arr_inning = [list(map(int, input().split())) for _ in range(INNING_NUM)]

ans = 0
# [1,2,3,4,5,6,7,8] # 0 제외 1번놈(0)이 무조건 4번타자니까
for combi in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8], 8):
    tmp_order = list(combi)
    batter_order = tmp_order[:3] + [0] + tmp_order[3:]
    score_tmp = 0
    batter_num = 0
    for inning in range(INNING_NUM):
        # state_init
        base_state = [False, False, False]
        out_cnt = 3
        # 경기 진행
        while out_cnt:
            this_res = arr_inning[inning][batter_order[batter_num]]
            add_score, add_out = calScore(this_res)
            score_tmp += add_score
            out_cnt += add_out
            batter_num = (batter_num + 1) % 9

    if score_tmp > ans:
        ans = score_tmp

print(ans)
