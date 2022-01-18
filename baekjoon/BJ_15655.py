# 15655번
# 수열이 사전 순으로 증가하는 순서여야 함, 그리고 수열 하나하나가 오름차순
# input 4 2 / 9 8 7 1(list)
# 17 18 19 78 79 89

def dfs(elements):
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    for e in elements:
        next_elements = [x for x in elements if x >= e]
        next_elements.remove(e)

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()

    return


N, M = map(int, input().split(' '))
num_list = list(map(int, input().split(' ')))
num_list = sorted(num_list)
prev_elements = []
nums = num_list
dfs(nums)

