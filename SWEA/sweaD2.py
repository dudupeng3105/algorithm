# 1859 백만 장자 프로젝트
#
# test_case = int(input())
#
# for i in range(test_case):
#     day_num = int(input())
#     num_list = list(map(int, input().split(' ')))
#     total = 0
#     pointer_day = len(num_list)-1
#     while pointer_day > 0:
#         sell_day = num_list[pointer_day]
#         pointer_day = pointer_day - 1
#         buy_day_list = []
#         while sell_day > num_list[pointer_day]:  # 파는 날 보다 비싼 값 나올 때까지 거꾸로 읽음
#             buy_day_list.append(sell_day - num_list[pointer_day])
#             pointer_day = pointer_day - 1
#             if pointer_day == -1:
#                 break
#         total = total + sum(buy_day_list)
#     print(f'#{i+1} {total}')

# 1956 간단한 369 게임
#
# N = int(input())   # 33
# for x in range(1, N+1):
#     cnt = 0
#     for str_x in str(x):
#         if str_x in ['3', '6', '9']:
#             cnt += 1
#     if cnt > 0:
#         print('-'* cnt,end='')
#     else:
#         print(x, end='')
#     if x < N:
#         print(' ', end='')
#     else:
#         pass

# 2007
# input KOREAKOREAKOREAKOREAKOREAKOREA
# output #1 5
# N = int(input())
#
# for test_case in range(N):
#     given_list = input()
#     given_list = list(given_list)
#     max_len_unit = 0
#     for i in range(1,11):
#         one_unit = given_list[:i]
#         check_unit = given_list[i: 2*i]
#         if one_unit == check_unit:
#             max_len_unit = i
#             break  # 문제조건이 좀 이상해서 조건되면 바로 탈출시킴
#     print(f'#{test_case+1} {max_len_unit}')