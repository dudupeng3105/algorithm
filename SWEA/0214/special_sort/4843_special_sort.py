import sys

# 가장 큰 수와 가장 작은 수
def bubble_sort(lst):
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


sys.stdin = open("input.txt")

testcase = int(input())
for tc in range(1, testcase + 1):
    length = int(input())
    given_list = list(map(int, input().split()))
    sorted_list = bubble_sort(given_list)
    # [1 2 3 4 5 6 7 8 9 10]
    arr = []
    for i in range(5):
        arr.append(sorted_list[length-1-i])
        arr.append(sorted_list[i])

    print(f'#{tc}', end=' ')
    print(*arr)