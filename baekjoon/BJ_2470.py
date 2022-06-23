import sys
input = sys.stdin.readline

n = int(input())
solution_list = list(map(int, input().split()))
solution_list.sort()

# All acid
# 죄다 산이면 작은거 두개만 고르면 됨 1, 2, 8, 10
if solution_list[0] > 0 and solution_list[-1] > 0:
    print(solution_list[0], solution_list[1])
# All base
# 죄다 염기면 끝에꺼 두개만 고르면 됨 -10, -8, -2, -1
elif solution_list[0] < 0 and solution_list[-1] < 0:
    print(solution_list[-2], solution_list[-1])

else:
    result_sum = 5000000000

    # 투 포인터
    left = 0
    right = n - 1
    base_acid_sum = solution_list[left] + solution_list[right]
    while left < right:
        base_acid_sum = solution_list[left] + solution_list[right]
        if abs(base_acid_sum) <= abs(result_sum):
            result_sols = [solution_list[left], solution_list[right]]
            result_sum = base_acid_sum

        if base_acid_sum == 0:
            break

        elif base_acid_sum > 0:
            right -= 1

        else:  # base_acid_sum < 0
            left += 1

    print(*result_sols)