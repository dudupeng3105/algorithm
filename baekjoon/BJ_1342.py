1import sys
from collections import defaultdict

input = sys.stdin.readline


def dfs(pre, depth):
    global length_s, cnt, dict_keys

    if depth == length_s:
        cnt += 1
        return

    for char in dict_keys:
        if pre == char:
            continue
        if not cnt_dict[char]:
            continue

        cnt_dict[char] -= 1
        dfs(char, depth + 1)
        cnt_dict[char] += 1


given_str = list(input().rstrip())
cnt_dict = defaultdict(int)
for char in given_str:
    cnt_dict[char] += 1

# global var
cnt = 0
length_s = len(given_str)
dict_keys = cnt_dict.keys()
#
dfs('', 0)
print(cnt)
