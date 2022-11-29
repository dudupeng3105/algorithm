# 함께 블록 쌓기
import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

cnt = [0 for _ in range(h + 1)]

for i in range(n):   # 1번학생.. 2번학생.. 3번학생..
    new_cnt = cnt[::]   # 새로운 배열을 만들어서 업데이트 하는 방식으로 함

    for num in arr[i]:
        new_cnt[num] += 1   # 일단 1 +

        for j in range(h - num):   # h-num을 더하면 h가 되므로 그 이상은 할 필요가 없다
            if cnt[j + 1]:
                new_cnt[num + j + 1] = new_cnt[num + j + 1] + cnt[j + 1]  # (j + 1) + num => num + j + 1

    cnt = new_cnt[::]

print(cnt[-1] % 10007)  # 마지막이 h임

# # dfs 실패!
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
