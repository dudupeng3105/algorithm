import sys
input = sys.stdin.readline

n = int(input())

arr1 = list(map(int, input().rstrip()))
arr1_copy = arr1[::]
arr2 = list(map(int, input().rstrip()))


# 첫자리 toggle 한 경우
cnt = 0
for dx in [0, 1]:
    arr1[dx] = 1 - arr1[dx]
cnt += 1

for i in range(1, n-1):
    if arr1[i-1] != arr2[i-1]:
        for dx in [-1, 0, 1]:
            arr1[i + dx] = 1 - arr1[i + dx]
        cnt += 1

if arr1 != arr2:
    # 다르면 마지막 자리 토글해봄
    for dx in [-1, 0]:
        arr1[n-1+dx] = 1 - arr1[n-1+dx]
    cnt += 1

    if arr1 != arr2:
        cnt = 180000


# 첫자리 toggle 안 한 경우
cnt2 = 0
for i in range(1, n - 1):
    if arr1_copy[i-1] != arr2[i-1]:
        for dx in [-1, 0, 1]:
            arr1_copy[i + dx] = 1 - arr1_copy[i + dx]
        cnt2 += 1

if arr1_copy != arr2:
    # 다르면 마지막 자리 토글해봄
    for dx in [-1, 0]:
        arr1_copy[n - 1 + dx] = 1 - arr1_copy[n - 1 + dx]
    cnt2 += 1

    if arr1_copy != arr2:
        cnt2 = 200000

#print(cnt, cnt2)
ans = min(cnt, cnt2)
if ans == 180000:
    print(-1)
else:
    print(ans)
