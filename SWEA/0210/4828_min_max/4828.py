import sys

# 가장 큰 수와 가장 작은 수
def bubble_sort(lst):
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


sys.stdin = open('input.txt')
# 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라
testcase = int(input())
for tc in range(testcase):
    length = int(input())
    arr = list(map(int, input().split()))
    # 정렬
    result = bubble_sort(arr)
    # 제일 큰 값 - 제일 작은 값
    print(f'#{tc+1} {result[-1]-result[0]}')