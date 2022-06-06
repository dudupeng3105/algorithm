import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_length = 100000001
left_point = 0
right_point = 0
temp_sum = arr[0]

while True:
    if temp_sum < s:
        right_point += 1
        if right_point >= n:
            break
        temp_sum += arr[right_point]

    else: # temp_sum >= s
        min_length = min(min_length, right_point-left_point + 1)
        temp_sum -= arr[left_point]
        left_point += 1
        if left_point > right_point:
            break

if min_length == 100000001:
    print(0)
else:
    print(min_length)
