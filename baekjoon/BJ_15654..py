# 15654번
# 수열이 사전 순으로 증가하는 순서여야 함
# input 4 2 / 9 8 7 1(list)
# 17 18 19 71 78 79 81 87 89 91 97 98

def dfs(elements):
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    for e in elements:
        next_elements = elements[:]
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