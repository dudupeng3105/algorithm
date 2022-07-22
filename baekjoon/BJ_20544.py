import sys

input = sys.stdin.readline

n = int(input())
# N = 3
# 0, 1, 2 행렬
arr = [1, 0, 1, 2]  # [0으로끝남, 01, 02, 2자리 꽉참]
# 1,0 으로만 있는 행렬
arr_zero_one = [[0, 0, 0] for _ in range(1001)]  # [a, b, c] a = 10, 00, b = 01 c = 11
arr_zero_one[1] = [0, 0, 0]
arr_zero_one[2] = [2, 0, 0]
arr_zero_one[3] = [2, 1, 1]
for i in range(4, 1001):
    a, b, c = arr_zero_one[i - 1]
    arr_zero_one[i] = [a + b + c, a, b]

# print(arr_zero_one[:10])

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    for i in range(n - 3):
        new_arr = [0, 0, 0, 0]

        new_arr[0] = sum(arr) % 1000000007  # a + b + c + d
        new_arr[1] = arr[0] % 1000000007  # a
        new_arr[2] = (arr[0] + arr_zero_one[i + 3][0]) % 1000000007  # a + zero_one_two
        new_arr[3] = (arr[1] * 2 + arr[2] + arr_zero_one[i + 3][1]) % 1000000007  # 2 * b + c + zero_one_two

        arr = new_arr[::]

    print(sum(arr) % 1000000007)
