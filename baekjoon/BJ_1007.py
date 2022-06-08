import sys
from itertools import combinations

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    nums = [i for i in range(n)]
    vectors = []
    for _ in range(n):
        a, b = map(int, input().split())
        vectors.append([a, b])
    # print(vectors)
    plus_set = combinations(nums, n // 2)  # 20 C 10
    length = 9999999999
    for plus in plus_set:
        total_x = 0
        total_y = 0
        for i in range(n):
            if i in plus:
                total_x += vectors[i][0]
                total_y += vectors[i][1]
            else:
                total_x -= vectors[i][0]
                total_y -= vectors[i][1]
        # print(total_x, total_y)

        # 길이 계산
        temp_length = (total_x ** 2 + total_y ** 2) ** 0.5
        if temp_length < length:
            length = temp_length

    print(length)
