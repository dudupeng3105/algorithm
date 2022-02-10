import sys


def custom_sum(lst): # sum 쓰려고 만듬
    result = 0
    for element in lst:
        result += element

    return result

sys.stdin = open("input.txt")

testcase = int(input())
for tc in range(testcase):
    length, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_num = 100000000
    max_num = 0
    for i in range(0, length - M + 1):  # ex 5, 3의 경우 index 2까지만 조사하면됨, 3부터는 범위 넘어감
        temp = custom_sum(arr[i:i + M])  # 이웃한 M개의 합
        if temp > max_num:
            max_num = temp
        if temp < min_num:
            min_num = temp

    print(f'#{tc + 1} {max_num - min_num}')
