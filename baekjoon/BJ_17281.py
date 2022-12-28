import sys
import itertools

input = sys.stdin.readline

def calScore(hit_res):
    global base_state


inning = int(input())

arr_inning = [list(map(int, input().split())) for _ in range(inning)]


ans = 0
for n in range(inning):

    lineup = arr_inning[n][1:]
    inning_tmp = 0
    for combi in itertools.permutations(lineup, 8):
        combi_lineup = list(combi[:3])+ [arr_inning[n][0]] + list(combi[3:])
        combi_tmp = 0
        base_state = [False, False, True]
        out_cnt = 3
        for i in range(50):
            add_score, add_out = calScore(combi_lineup[])
            out_cnt += add_out
            combi_tmp += add_score


        if combi_tmp > inning_tmp:
            inning_tmp = combi_tmp

    print(inning_tmp)
    ans += inning_tmp

print(ans)



