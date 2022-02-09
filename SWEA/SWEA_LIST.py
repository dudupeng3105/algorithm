import sys

# 버블소트
# O(n^2), 코딩이 쉬움, 쓰레기
def bubble_sort(lst):
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


# 카운팅 소트
# 카운팅 정렬은 공간복잡도를 버리고, 시간복잡도를 취함
# O(n+k)
# 알파벳이나 0~10의 수 등 숫자 범위 작을 때 매우 유용
def counting_sort(lst):
    count_lst = [0 for _ in range(10)]
    # 개수 찾기
    for i in lst:
        count_lst[i] += 1
    # 누적합
    for j in range(len(count_lst) - 1):
        count_lst[j + 1] += count_lst[j]
    # 프린트
    result = [0 for __ in range(len(lst))]
    for num in lst[::-1]:
        count_lst[num] -= 1
        result[count_lst[num]] = num

    return print(*result, end='')


# test_list = [1, 3, 4, 4, 2, 1, 6, 7, 8, 0, 9, 9, 2, 3, 6, 5, 2]
# counting_sort(test_list)

# 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라
# testcase = int(input())
# for tc in range(testcase):
#     length = int(input())
#     arr = list(map(int, input().split()))
#     result = bubble_sort(arr)
#     print(f'#{tc+1} {result[length-1]-result[0]}')


#
# testcase = int(input())
# for tc in range(testcase):
#     length = int(input())
#     arr = list(input())
#     count_lst = [0 for x in range(10)]
#     for i in arr:
#         count_lst[int(i)] += 1
#
#     cnt = 0
#     num = 0
#     for j in range(10):
#         if count_lst[j] >= cnt:
#             cnt = count_lst[j]
#             num = j
#     print(f'#{tc+1} {num} {cnt}')
#


# 4835. 구간합

# testcase = int(input())
# for tc in range(testcase):
#     length, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     min_num = 10000000
#     max_num = 0
#     for i in range(0, length - M + 1):
#         temp = sum(arr[i:i + M])
#         if temp > max_num:
#             max_num = temp
#         if temp < min_num:
#             min_num = temp
#
#     print(f'#{tc + 1} {max_num - min_num}')

# # 4831. 전기버스
# testcase = int(input())
# for tc in range(testcase):
#     # K: 한 번 충전으로 이동할 수 있는 정류장 수, N: 정류장 수
#     # M: 충전기가 설치된 정류장의 수
#     K, N, M = map(int, input().split())
#     chargers = [False for _ in range(N)]
#     charger_lst = list(map(int, input().split()))
#     # 충전기 설치된 정류장 True 처리
#     for charger in charger_lst:
#         chargers[charger] = True
#     cnt = 0
#     now_station = 0
#
#     while now_station + K < N:
#         checker = 0
#         for i in range(now_station + K, now_station, -1):
#             if chargers[i]:
#                 checker = 1
#                 now_station = i
#                 cnt += 1
#                 break
#
#         if checker == 0:
#             break
#
#     if checker:
#         print(f'#{tc+1} {cnt}')
#     else:
#         print(f'#{tc+1} {0}')

# Gravity
