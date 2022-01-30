import sys


def dfs(elements, depth):
    if depth == N + 1:
        if sign[depth-2] == '<':
            if result[-2] >= result[-1]:
                return
        # if sign == '>':
        else:
            if result[-2] <= result[-1]:
                return

        total.append(''.join(map(str, result)))
        return

    elif depth < 2:
        pass

    else: # depth > 2
        if sign[depth-2] == '<':
            if result[-2] >= result[-1]:
                return
        # if sign == '>':
        else:
            if result[-2] <= result[-1]:
                return

    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        result.append(e)
        dfs(next_elements, depth + 1)
        result.pop()


N = int(sys.stdin.readline())
sign = list(map(str, sys.stdin.readline().split()))
nums = [x for x in range(10)]
result = []
total = []
dfs(nums, 0)
print(total[-1])
print(total[0])


