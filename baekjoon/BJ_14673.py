import sys
from collections import deque

# from pprint import pprint

input = sys.stdin.readline


# 크러쉬 피버

# bfs + dfs
# arr(격자), score(점수), remain(남은 퍼즐 수), depth(클릭 횟수)
def dfs(arr, score, remain, depth):
    global ans

    # print(depth, remain)
    # 3턴 안에 남는 게 없을 수도 있으니까
    if not remain:
        ans = max(ans, score)
        return

    # 3번 클릭했으면 끝난거임
    if depth == 3:
        ans = max(ans, score)
        return

    # visited 를 사용함으로써 이번 클릭을 모두 하지 않아도 됨(6*3 배열의 경우 원래 18번 해야하지만)
    # visited 사용해서 (bfs로 탐색한 곳은 모두 같은 결과를 반환하므로 문제예시에서 보면 4번으로 줄일 수 있음)
    visited = [[False for _ in range(C)] for __ in range(R)]
    # BFS
    for i in range(R):
        for j in range(C):
            if arr[i][j] and not visited[i][j]:
                # print("i, j", i, j)
                q = deque()
                ref = arr[i][j]  # 퍼즐 조각 종류(퍼즐에 몇 번이 적혀있는지)
                broken_lst = []  # 이번에 파괴될 퍼즐들을 담는 list
                q.append((i, j))
                visited[i][j] = True
                while q:
                    r, c = q.popleft()
                    broken_lst.append((r, c))
                    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        n_r, n_c = r + dr, c + dc
                        if 0 <= n_r < R and 0 <= n_c < C and not visited[n_r][n_c]:
                            if arr[n_r][n_c] == ref:  # 번호만 같은거만
                                visited[n_r][n_c] = True
                                q.append((n_r, n_c))

                # print(broken_lst)

                # bfs 끝나고 들어감
                # 배열을 복사함
                new_arr = [arr[i][::] for i in range(R)]

                ######################
                print("변경 전(뎁스: ", depth, ")")
                for index in range(R):
                    print(new_arr[index])
                ######################

                # 파괴된 퍼즐 0으로 바꿈
                for r, c in broken_lst:
                    new_arr[r][c] = 0

                ######################
                print("비운 후")
                for index in range(R):
                    print(new_arr[index])
                ######################

                # 격자 수정(구현)
                for c in range(C):
                    for r in range(R - 1, -1, -1):
                        if not new_arr[r][c]:  # 비어있는 자리면
                            n_r = r - 1
                            while n_r >= 0:
                                if new_arr[n_r][c]:
                                    new_arr[n_r][c], new_arr[r][c] = new_arr[r][c], new_arr[n_r][c]
                                    break
                                else:
                                    n_r = n_r - 1
                                    continue

                ######################
                print("격자 수정 후")
                for index in range(R):
                    print(new_arr[index])
                print()
                ######################

                # dfs (다음 턴 진행)
                dfs(new_arr, score + len(broken_lst) ** 2, remain - len(broken_lst), depth + 1)


C, R = map(int, input().split())
given_arr = [list(map(int, input().split())) for _ in range(R)]
puzzle_num = C * R
ans = 0
dfs(given_arr, 0, puzzle_num, 0)
print(ans)
