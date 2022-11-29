import sys
from collections import deque

input = sys.stdin.readline

'''
N, M, K

N 배열의 값

M 나무의 정보 x, y, z(나이)

봄 : 양분 먹고 나이 증가, 못먹으면 죽음
여름: 죽은 나무가 양분으로 변함 나이//2
가을: 나무 번식, 나이가 5의 배수인거만, 인접 8칸에 1인 나무 생김
겨울: a 배열값 만큼 양분 추가해줌
'''
N, M, K = map(int, input().split())
s2d2 = [list(map(int, input().split())) for _ in range(N)]  # 겨울용
nutrition = [[5 for _ in range(N)] for __ in range(N)]  # 처음 양분 5
tree = [[deque() for _ in range(N)] for __ in range(N)]
for _ in range(M):
    x, y, old = map(int, input().split())
    # 입력으로 주어지는 나무의 위치는 모두 서로 다름
    tree[x - 1][y - 1].append(old)

for _ in range(K):  # K년 진행
    # 봄 - 여름
    for i in range(N):
        for j in range(N):
            tree_num = len(tree[i][j])
            for k in range(tree_num):
                # 1. 봄 - 양분 먹고 나이 증가, 못먹으면 죽음
                if tree[i][j][k] <= nutrition[i][j]:
                    nutrition[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
                else:
                    # 양분 부족 죽음, 2. 여름 같이 처리
                    for _ in range(k, tree_num):
                        nutrition[i][j] += (tree[i][j].pop() // 2)
                    break

    # 가을
    # 3. 가을 - 나무 번식, 나이가 5의 배수인거만, 인접 8칸에 1인 나무 생김
    for i in range(N):
        for j in range(N):
            tree_num = len(tree[i][j])
            for k in range(tree_num):
                if tree[i][j][k] % 5 == 0:  # 5로 나누어 떨어짐
                    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                        n_r, n_c = i + dr, j + dc
                        if 0 <= n_r < N and 0 <= n_c < N:
                            tree[n_r][n_c].appendleft(1)

    # 4. 겨울 - 로봇이 양분을 뿌리고 다님
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += s2d2[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)
