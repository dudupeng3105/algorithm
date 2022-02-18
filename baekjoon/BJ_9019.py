import sys
from collections import deque


def bfs(start_num):
    q = deque()
    q.append((start_num, ''))  # num, operation_string
    arr[start_num] = True
    while q:
        num, op_str = q.popleft()
        for i in range(4):  # D,S,L,R
            if i == 0:  # D (2배)
                new_num = (num * 2) % 10000
                if arr[new_num]:
                    continue
                if new_num == end_num:
                    return op_str + 'D'
                arr[new_num] = True
                q.append((new_num, op_str + 'D'))

            if i == 1:  # S (-1)
                if num:
                    new_num = num - 1
                    if arr[new_num]:
                        continue
                    if new_num == end_num:
                        return op_str + 'S'
                    arr[new_num] = True
                    q.append((new_num, op_str + 'S'))
                else:  # n == 0
                    new_num = 9999
                    if arr[new_num]:
                        continue
                    if new_num == end_num:
                        return op_str + 'S'
                    arr[new_num] = True
                    q.append((new_num, op_str + 'S'))

            if i == 2:  # L (왼쪽회전)
                if num < 1000:
                    new_num = num * 10
                    if arr[new_num]:
                        continue
                    if new_num == end_num:
                        return op_str + 'L'
                    arr[new_num] = True
                    q.append((new_num, op_str + 'L'))
                else:
                    new_num = (num % 1000) * 10 + (num // 1000)
                    if arr[new_num]:
                        continue
                    if new_num == end_num:
                        return op_str + 'L'
                    arr[new_num] = True
                    q.append((new_num, op_str + 'L'))

            if i == 3:  # R (왼쪽회전)
                new_num = (num % 10) * 1000 + (num // 10)
                if arr[new_num]:
                    continue
                if new_num == end_num:
                    return op_str + 'R'
                arr[new_num] = True
                q.append((new_num, op_str + 'R'))


test_case = int(sys.stdin.readline())
for tc in range(test_case):
    arr = [False for _ in range(10000)]
    start_num, end_num = map(int, sys.stdin.readline().split())

    result = bfs(start_num)
    print(result)


# BFS 방문체크는 꼭 큐에 넣기전에 하자!
# 큐 pop 시 하면 그 뒤에 오는 것에서 중복으로 들어가서 시간복잡도 Up
# 안들어가는 조건도 넣기 전에 해야함 => 그래야 최대한 줄여짐