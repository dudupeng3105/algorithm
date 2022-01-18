# 15651번
# 같은 수를 여러번 선택할 수 있음
# 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

def dfs(elements):
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    else:  # 원하는 길이(prev_e ==M)됐으면 더 깊이 안들어가도록 if else문 썼음
        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    return


N, M = map(int, input().split())
prev_elements = []
nums = list(range(1, N + 1))
dfs(nums)