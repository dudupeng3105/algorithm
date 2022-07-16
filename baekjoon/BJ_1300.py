
# cnt_lst = [0] + [0 for _ in range(min(10**9, n**2))]

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         num = i * j
#         if num > 10**6:
#             break   # j for 문 탈출
#         else:
#             cnt_lst[num] += 1
# 1300 k 번째 수
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

s, e = 1, k
while s <= e:
    mid = (s+e) // 2  # 기준수

    cnt = 0  # 기준이 되는 수보다 작거나 같은 수의 개수
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt >= k:
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)