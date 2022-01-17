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
