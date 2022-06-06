import sys
input = sys.stdin.readline

n = int(input())
solution_list = list(map(int, input().split()))

# All acid
if solution_list[0] > 0 and solution_list[len(solution_list)-1] > 0:
    print(solution_list[0], solution_list[1])
# All base
elif solution_list[0] < 0 and solution_list[len(solution_list)-1] < 0:
    print(solution_list[len(solution_list)-2], solution_list[len(solution_list)-1])
else:
    # 1. 산과 염기의 경계선 찾기
    change_index = -1
    for i in range(len(solution_list)):
        if solution_list[i] > 0: # 염기다가 산으로 바뀜
            change_index = i
            break

    # 초기값 세팅(염기에 젤 작은 거 2개, 산의 젤 작은거 2개)
    acid_min = 5000000000
    base_min = 5000000000
    # acid_min
    if change_index + 1 < len(solution_list) -1:  #최소 2개 있어야
        acid_min = solution_list[change_index] + solution_list[change_index + 1]
    # base_min
    if change_index - 2 > 0:  # 최소 2개 있어야
        base_min = solution_list[change_index - 2] + solution_list[change_index - 1]
    # 최소 저장
    if abs(acid_min) <= abs(base_min):
        result_sols = [solution_list[change_index], solution_list[change_index + 1]]
        result_sum = acid_min
    else:
        result_sols = [solution_list[change_index - 2], solution_list[change_index - 1]]
        result_sum = base_min

    # 투 포인터
    base_index = change_index - 1
    acid_index = change_index
    base_acid_sum = solution_list[base_index] + solution_list[acid_index]
    while True:
        if abs(base_acid_sum) < abs(result_sum):
            result_sols = [solution_list[base_index], solution_list[acid_index]]
            result_sum = base_acid_sum

        if base_acid_sum == 0:
            break

        elif base_acid_sum > 0:
            base_index -= 1
            if base_index < 0:
                break
            else:
                base_acid_sum = solution_list[base_index] + solution_list[acid_index]

        else: # base_acid_sum < 0
            acid_index += 1
            if acid_index == len(solution_list):
                break
            else:
                base_acid_sum = solution_list[base_index] + solution_list[acid_index]

    print(*result_sols)
    # print(result_sum)
    # print("끝")



