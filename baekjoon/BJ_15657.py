# 수열이 사전 순으로 증가하는 순서여야 함, 그리고 숫자 중복 가능, 비내림차순
# input 4 2 / 9 8 7 1(list)
# 11 17 18 19 77 78 79 88 89 99

def dfs(elements):
    if len(prev_elements) == M:
        print(' '.join(map(str, prev_elements)))

    else:
        for e in elements:
            next_elements = [x for x in elements if x >= e]

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