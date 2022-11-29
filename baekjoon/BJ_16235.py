import sys
import heapq

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
tree = []
for _ in range(M):
    x, y, old = map(int, input().split())
    heapq.heappush(tree, (old, x - 1, y - 1))

for _ in range(K):  # K년 진행
    # 1. 봄 - 양분 먹고 나이 증가, 못먹으면 죽음
    summer_tree = []  # 봄이 지난 후 트리들
    # print("tree", tree, len(tree))
    while tree:
        tree_old, r, c = heapq.heappop(tree)
        # print("나무 나이", tree_old, nutrition[r][c])
        if tree_old <= nutrition[r][c]:
            nutrition[r][c] -= tree_old
            heapq.heappush(summer_tree, (tree_old + 1 , r, c))

        else:  # 양분 못먹고 뒤짐 -로 죽음을 표시함
            heapq.heappush(summer_tree, (-tree_old, r, c))

    # 2. 여름 - 죽은 나무가 양분으로 변함 나이//2

    while summer_tree and summer_tree[0][0] < 0:  # 죽은 나무에 대해서만 진행
        tree_old, r, c = heapq.heappop(summer_tree)
        nutrition[r][c] += (-tree_old // 2)

    if not summer_tree:  # 나무가 없음
        break

    # 3. 가을 - 나무 번식, 나이가 5의 배수인거만, 인접 8칸에 1인 나무 생김
    tree = []  # 윈터트리
    while summer_tree:
        tree_old, r, c = heapq.heappop(summer_tree)
        if tree_old % 5 == 0:  # 5로 나누어 떨어짐
            heapq.heappush(tree, (tree_old, r, c))  # 그대로 일단 하나 넣고
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                n_r, n_c = r + dr, c + dc
                if 0 <= n_r < N and 0 <= n_c < N:
                    heapq.heappush(tree, (1, n_r, n_c))

        else:  # 그냥 다시 넣어줌
            heapq.heappush(tree, (tree_old, r, c))

    # 4. 겨울 - 로봇이 양분을 뿌리고 다님
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += s2d2[i][j]

print(len(tree))
