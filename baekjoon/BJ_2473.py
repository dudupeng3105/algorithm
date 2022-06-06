import sys

input = sys.stdin.readline

n = int(input())
solution_list = list(map(int, input().split()))
solution_list.sort()
# print(solution_list)

ans_sum = 5000000000
ans_list = []

flag = 0
for i in range(n - 2):
    fixed_point = i
    left_point = i + 1
    right_point = n - 1
    while left_point < right_point:
        temp_sum = solution_list[fixed_point] + solution_list[left_point] + solution_list[right_point]
        if abs(temp_sum) <= abs(ans_sum):
            ans_list = [solution_list[fixed_point], solution_list[left_point], solution_list[right_point]]
            ans_sum = temp_sum
        if temp_sum < 0:
            left_point += 1
        elif temp_sum > 0:
            right_point -= 1
        else:  # temp_sum == 0
            print(*ans_list)
            flag = 1
            break
    if flag:
        break

if not flag:
    print(*ans_list)
