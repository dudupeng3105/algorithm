import sys

sys.stdin = open('input.txt')
test_case = int(input())

for tc in range(test_case):
    N = int(input())
    boxes_height = list(map(int, input().split()))

    result = 0

    for i in range(N):
        max_height = len(boxes_height) - (i+1)
        for j in range(i + 1, N):
            if boxes_height[j] >= boxes_height[i]:
                max_height = max_height -1

        if max_height > result:
            result = max_height

    print(f'#{tc+1} {result}')