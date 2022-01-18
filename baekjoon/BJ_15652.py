# 15652번
# 같은 수 가능, 비내림차순 --> 2 2는 되지만, 2 1은 안된다는 뜻 인듯
# 11 12 13 14 22 23 24 32 33 34 41 42 43 44

def dfs(elements):
    # if - else 문으로 지옥까지 안내려가게 했음
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    else:
        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = [x for x in elements if x >= e]

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    return


N, M = map(int, input().split())
prev_elements = []
nums = list(range(1, N + 1))
dfs(nums)