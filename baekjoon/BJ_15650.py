# 15650번 N과 M (2)
# 수열이 오름차순 이어야함

def dfs(elements):
    # 리프 노드일 때 결과 추가 --> 트리 맨 밑에 노드 leaf node
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    # 순열 생성 재귀 호출
    for e in elements:
        next_elements = [x for x in elements if x >= e]
        next_elements.remove(e)

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()

    return


N, M = map(int, input().split())
results = []
prev_elements = []
nums = list(range(1, N + 1))
dfs(nums)
