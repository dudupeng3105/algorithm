# 이분매칭을 활용한 풀이법 공부
import sys
# from pprint import pprint
input = sys.stdin.readline


def make_group(dir):
    numbering_map = [[0 for _ in range(n)] for __ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not chess_map[i][j]:
                continue
            if numbering_map[i][j]:
                continue
            r, c = i, j
            cnt += 1
            numbering_map[r][c] = cnt

            while True:
                r += dr[dir]
                c += dc[dir]
                if r < 0 or c < 0 or r > n - 1 or c > n - 1:
                    break
                if not chess_map[r][c]:
                    continue
                if numbering_map[r][c]:
                    break
                numbering_map[r][c] = cnt

    return numbering_map, cnt


def match(v, checked):
    for arrived in graph[v]:
        if checked[arrived]:
            continue
        checked[arrived] = True
        # 아직 arrived 연결된 출발점이 없거나 연결된 점이 있으면
        # 그 점을 arrived 연결되게 해서 성공하면 True 리턴 실패하면 Flase 리턴
        if par[arrived] == -1 or match(par[arrived], checked):
            par[arrived] = v
            return True  # 매칭 성공

    return False  # 매칭 실패


def bipartite_match():
    res = 0
    for i in range(1, ref_cnt+1):
        checked = [False for _ in range(2 * n)]
        k = match(i, checked)
        # print(i, k)
        res += k

    return res


n = int(input())
# cnt = [0, 0]
dr = [1, 1]
dc = [1, -1]
chess_map = [list(map(int, input().split())) for _ in range(n)]
# dir = 0 -> 오른쪽 아래방향, dir = 1 -> 왼쪽 아래방향 대각선
# 대각선맵 만듬
diagonal_numbering_1, cnt_1 = make_group(0)
diagonal_numbering_2, cnt_2 = make_group(1)
ref_cnt = cnt_1
graph = [[] for _ in range(2 * n)]
par = [-1 for _ in range(2 * n)]
# pprint(diagonal_numbering_1)
# pprint(diagonal_numbering_2)
for i in range(n):
    for j in range(n):
        if not chess_map[i][j]:
            continue
        else:
            right_downward = diagonal_numbering_1[i][j]
            left_downward = diagonal_numbering_2[i][j]
            # 이분 그래프 그리기
            if left_downward in graph[right_downward]:
                continue
            else:
                graph[right_downward].append(left_downward)

cnt = bipartite_match()
print(cnt)


