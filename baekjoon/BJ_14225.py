import sys


def dfs(start, result):
    sum_lst.append(sum(result))

    for i in range(start, n):
        result.append(num_seq[i])
        dfs(i + 1, result)
        result.pop()


n = int(sys.stdin.readline())
num_seq = list(map(int, sys.stdin.readline().split()))
nums_sum = sum(num_seq)
sum_lst = []
dfs(0, [])
sum_lst.sort()
sum_lst = list(set(sum_lst))

for i in range(1, nums_sum + 1):
    if sum_lst[i] != i:
        break

if i == nums_sum:
    print(nums_sum + 1)
else:
    print(i)
