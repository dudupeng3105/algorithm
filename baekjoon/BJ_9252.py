import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

len_a = len(a)
len_b = len(b)

arr = [[0 for _ in range(len_a + 1)] for __ in range(len_b + 1)]

for i in range(1, len_b + 1):
    for j in range(1, len_a + 1):
        if a[j - 1] == b[i - 1]:  # 문자 같으면
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])

# for i in range(len_b + 1):
#     print(arr[i])

# 문자열 구하기
i = len_b
j = len_a
if not arr[i][j]:  # not lcs
    print(0)
else:
    ans = ''
    now = arr[i][j]
    while now != 0:
        if arr[i][j - 1] == now - 1 and arr[i - 1][j] == now - 1:
            ans = a[j - 1] + ans
            now -= 1
            i -= 1
            j -= 1
        else:
            if arr[i - 1][j] > arr[i][j - 1]:
                i -= 1
            else:
                j -= 1

    print(len(ans))
    print(ans)
