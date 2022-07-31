import sys
# 탑 보기
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
left_forward = []
right_forward = []

stack = [(arr[0], 1)]
right_forward.append((0, 0))

# right_forward(오른쪽으로가면서.. 왼쪽에 보이는거만 신경씀)
for i in range(1, len(arr)):
    # 나보다 작은건 못보니까 빼줌
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()

    # 나보다 높은것들의 개수과, 가장가까이(stack[-1])의 빌딩 넘버를 저장함
    if stack:
        right_forward.append((len(stack), stack[-1][1]))
    else:
        right_forward.append((0, 0))

    # 스택에 나 자신의 높이와 빌딩넘버를 append
    stack.append((arr[i], i + 1))  # height, num


stack = [(arr[-1], len(arr))]
left_forward.append((0, 0))
# left_forward(왼쪽으로가면서.. 오른쪽에 보이는거만 신경씀)
for i in range(len(arr) - 2, -1, -1):
    # 이하동문
    while stack and stack[-1][0] <= arr[i]:
        stack.pop()
    if stack:
        left_forward.append((len(stack), stack[-1][1]))
    else:
        left_forward.append((0, 0))

    stack.append((arr[i], i + 1))  # height, num

left_forward = left_forward[::-1]
# print(right_forward)
# print(left_forward)
for i in range(n):
    num = i + 1
    # 나 기준 왼쪽에 보이는 것과 오른쪽에 보이는 것을 더해야 좌우에 조건을 만족하는 빌딩의 개수
    left_see, left_close_num = right_forward[i][0], right_forward[i][1]
    right_see, right_close_num = left_forward[i][0], left_forward[i][1]
    sum_see = left_see + right_see
    if not sum_see:
        print(0)
    else:
        if left_see and right_see:
            if (num - left_close_num) <= (right_close_num-num):
                print(sum_see, left_close_num)
            else:
                print(sum_see, right_close_num)
        else:
            if right_see:
                print(sum_see, right_close_num)
            else:  # left_see
                print(sum_see, left_close_num)
