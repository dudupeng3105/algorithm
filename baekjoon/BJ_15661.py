# 1. 조합 만들기(N = 6의 경우 시작이 1~3까지 경우만 구하면 절반은 자동임)
# 2. 14889와 달리 인원수가 동일하지 않아도됨(최소 한 명 이상)
# N이 짝수도 아님

from itertools import combinations
import sys
def ability_calculator(start_team, link_team, cnt):
    ability = 0
    length_start = cnt
    length_link = N-cnt

    for i in range(length_start):
        for j in range(i + 1, length_start):
            ability += ability_arr[start_team[i]][start_team[j]] \
                       + ability_arr[start_team[j]][start_team[i]]

    for i in range(length_link):
        for j in range(i + 1, length_link):
            ability -= ability_arr[link_team[i]][link_team[j]] \
                       + ability_arr[link_team[j]][link_team[i]]

    return ability


def dfs(start, cnt, n):
    global min_ability_difference
    # 어빌리티 계산
    if cnt == n:
        link_team = list(set(num_list)-set(start_team))
        ability = ability_calculator(start_team, link_team, cnt)
        min_ability_difference = min(min_ability_difference, abs(ability))
        return

    for i in range(start, N):
        start_team.append(i)
        dfs(i + 1, cnt + 1, n)
        start_team.pop()


N = int(sys.stdin.readline())
ability_arr = [[0 for _ in range(N)] for __ in range(N)]
for i in range(0, N):
    ability_arr[i] = list(map(int, sys.stdin.readline().split()))

start_team = []
num_list = list(range(N))
min_ability_difference = 10000
# 1~3(0~2)에서 시작
for i in range(1, N//2 + 1): # 스타트팀의 사람 수 ex) N= 7 1~3명까지 탐색
    dfs(0, 0, i)

print(min_ability_difference)

# row_sums, col_sums를 이용한 방법도 있음 --> 10배정도 빠름
# 처음에 python으로 제출했는데 계속 시간초과라 pypy로 냈더니 합격했음