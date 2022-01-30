# 1. 조합 만들기(N = 6의 경우 시작이 1~3까지 경우만 구하면 절반은 자동임)
# 2. 길이 3일 때 어빌리티 계산
def dfs(start, start_team):
    global min_ability_difference
    # 어빌리티 계산
    if len(start_team) == N//2:
        # 스타트팀 어빌리티
        ability = 0
        for i in range(N//2):
            for j in range(i + 1, N//2):
                ability += ability_arr[start_team[i]][start_team[j]]\
                           + ability_arr[start_team[j]][start_team[i]]
        # 링크 팀 어빌리티
        link_team = list(set(num_list) - set(start_team))
        for i in range(N//2):
            for j in range(i + 1, N//2):
                ability -= ability_arr[link_team[i]][link_team[j]] \
                           + ability_arr[link_team[j]][link_team[i]]

        min_ability_difference = min(min_ability_difference, abs(ability))
        return

    for i in range(start, N):
        start_team.append(i)
        dfs(i + 1, start_team)
        start_team.pop()


N = int(input())
ability_arr = [[0 for _ in range(N)] for __ in range(N)]
for i in range(0, N):
    ability_arr[i] = list(map(int, input().split()))
start_team = []
num_list = list(range(N))
min_ability_difference = 10000
# 1~3(0~2)에서 시작
for i in range(3):
    start_team.append(i)
    dfs(i + 1, start_team)
    start_team.pop()

print(min_ability_difference)