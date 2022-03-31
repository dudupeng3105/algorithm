'''
그림 그리면서 이해하시는게 좋습니다.

랑이가 조작을 할 수 없다고 해보겠습니다.
1중에 제일 긴 것의 길이가 답일겁니다.
이건 1이 있는지 없는지로 아래, 오른쪽, 오른쪽 아래, 왼쪽 아래 방향으로 누적합을 각각 구해주면 그 누적합 배열에서 가장 큰 값이 정답이 될겁니다.

이제 랑이가 조작하는 경우를 봅시다.
각 2마다 이걸 랑이가 1로 바꾸면 몇점이 되는지 생각해봅시다.
어떤 위치의 2를 1로 바꾸면 이 위치 때문에 생기는 가로방향 점수는 이 왼쪽칸이 몇개째 연속인지 + 이 오른쪽 칸부터 몇개 연속으로 있는지 + 1이 될겁니다. 이걸 네 방향 모두 해주면 그중 가장 큰 값이 이 위치를 1로 바꿀 때의 점수입니다.
prefix 배열 구한것처럼 방향이 정반대인 suffix 배열을 만들어줍시다. 이제 2를 보면서 이 위치를 1로 바꿀 때의 점수를 prefix[i][j - 1] + suffix[i][j + 1] + 1 처럼 계산해주면 그중 최대값이 답입니다.
'''

n = int(input())
arr = [[0 for i in range(n + 1)]] + [[0] + list(map(int, input().split())) for i in range(n)]
for i in range(n):
    print(arr[i])

prefix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]
for s in range(4):
    print(s)
    for t in range(n):
        print(prefix[s][t])

suffix = [[[0 for i in range(n + 2)] for j in range(n + 2)] for k in range(4)]
dx = [[-1, -1, -1, 0], [1, 1, 1, 0]]
dy = [[-1, 0, 1, -1], [1, 0, -1, 1]]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == 1:
            for k in range(4):
                prefix[k][i][j] = prefix[k][i + dx[0][k]][j + dy[0][k]] + 1
            for s in range(4):
                if s == 3:
                    print('가로방향')
                    for t in range(n):
                        print(prefix[s][t])

for i in range(1, n + 1)[::-1]:
    for j in range(1, n + 1)[::-1]:
        if arr[i][j] == 1:
            for k in range(4):
                suffix[k][i][j] = suffix[k][i + dx[1][k]][j + dy[1][k]] + 1
            for s in range(4):
                if s == 3:
                    print('가로역방향')
                    for t in range(n):
                        print(suffix[s][t])

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(4):
            ans = max(ans, prefix[k][i][j])

            if arr[i][j] == 2:
                ans = max(ans, prefix[k][i + dx[0][k]][j + dy[0][k]] + suffix[k][i + dx[1][k]][j + dy[1][k]] + 1)

print(ans)