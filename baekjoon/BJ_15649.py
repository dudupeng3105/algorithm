# 15649 N과 M(1)
# 백트래킹(보통 재귀로 구현, DFS)

def dfs(elements):
    # 리프 노드일 때 결과 추가 --> 트리 맨 밑에 노드 leaf node
    if len(elements) == (N - M):
        print(' '.join(map(str, prev_elements)))

    # 순열 생성 재귀 호출
    for e in elements:  # e = 1
        next_elements = elements[:]  # n_e = 1,2,3
        next_elements.remove(e)  # n_e = 2, 3

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()

    return


N, M = map(int, input().split())
results = []
prev_elements = []
nums = list(range(1, N + 1))
dfs(nums)
