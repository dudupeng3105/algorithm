# 2600 구슬게임
import sys
input = sys.stdin.readline

b = list(map(int, input().split()))
dp = [[0 for _ in range(501)] for __ in range(501)]  # 0이면 a가 진다. 1이면 a가 이긴다


# dp 계산 하기
def who_win(x, y):
    for i in range(x+1):
        for j in range(y+1):

            flag = 0
            for idx in range(3):
                # 내가 공을 뽑고 난 후에 상태가 원래는 내가 지는 상태면 나는 이긴거임 ㅋㅋ
                # 내가 지는 상황을 상대에게 토스~
                # 총 6가지 경우 중 하나의 상황이라도 내가 이기는 상황이 나오면
                # 현태 i, j 상태에서는 내가 무조건 이길 수 있음
                if (j - b[idx] >= 0) and (dp[i][j-b[idx]] == 0):
                    flag = 1
                if (i - b[idx] >= 0) and (dp[i-b[idx]][j] == 0):
                    flag = 1

            dp[i][j] = flag


games_x = []
games_y = []
for _ in range(5):
    temp_x, temp_y = map(int, input().split())
    games_x.append(temp_x)
    games_y.append(temp_y)

max_x = max(games_x)
max_y = max(games_y)
who_win(max_x, max_y)

for i in range(5):
    result = dp[games_x[i]][games_y[i]]
    if result:
        print('A')
    else:
        print('B')