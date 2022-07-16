import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

cnt = [0 for _ in range(h + 1)]

for i in range(n):
    new_cnt = cnt[::]

    for num in arr[i]:
        new_cnt[num] += 1

        for j in range(h - num):
            if cnt[j + 1]:
                new_cnt[num + j + 1] = new_cnt[num + j + 1] + cnt[j + 1]

    cnt = new_cnt[::]

print(cnt[-1] % 10007)

# # dfs쓸거임
# def dfs(summ, depth):
#
#     global cnt, h
#
#     if summ == h:
#         cnt += 1
#         return
#
#     if depth > n-1:
#         return
#
#     if summ > h:
#         return
#
#     for num in arr[depth]:
#         dfs(summ + num, depth+1)
#
# cnt = 0
# dfs(0, 0)
# print(cnt % 10007)
