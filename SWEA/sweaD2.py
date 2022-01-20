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

# 2005
# 파스칼의 삼각형
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     arr = [[0 for _ in range(N)] for __ in range(N)]
#     arr[0][0] = 1
#     i = 1
#     while i != N:
#         arr[i][0] = 1
#         for k in range(1, i + 1):
#             arr[i][k] = arr[i-1][k-1] + arr[i-1][k]
#         i += 1
#
#     print(f'#{tc + 1}')
#     for j in range(len(arr)):
#         print(" ".join(map(str, arr[j][:j+1])))

# 2001
# 파리 퇴치
# test_case = int(input())
#
# for tc in range(test_case):
#     N, M = map(int, input().split(" "))
#     mosquito_map = [[0 for _ in range(N)] for __ in range(N)]
#
#     for i in range(N):
#         mosquito_map[i] = list(map(int, input().split(" ")))
#     max_num = 0
#
#     for row in range(N-M+1):
#         for col in range(N-M+1):
#             region_num = 0
#
#             for k in range(M):
#                 region_num += sum(mosquito_map[row + k][col: col+M])
#             if region_num > max_num:
#                 max_num = region_num
#
#     print(f'#{tc+1} {max_num}')

# 1989 초심자의 회문검사
# test_case = int(input())
# for tc in range(test_case):
#     given_string = input()

#     print(f'#{tc + 1} {int(given_string == given_string[::-1])}')

# 1986 지그재그 숫자
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#
#     if N % 2:  # 홀수
#         print(f'#{tc + 1} {-1 * (N // 2) + N}')
#     else:
#         print(f'#{tc + 1} {-1 * (N // 2)}')

# 1984 중간 평균값 구하기 # 7번 테케에 공백있음
# test_case = int(input())
# for tc in range(test_case):
#     num_list = list(map(int, input().rstrip(" ").split(" ")))
#     num_list.sort()
#     num_list = num_list[1:-1]
#
#     print(f'#{tc+1} {round(sum(num_list)/len(num_list))}')

# 1983 조교의 성적 매기기
# test_case = int(input())
# alphabet_socre_list = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-',
#                        'C+', 'C0', 'C-', 'D0']
# for tc in range(test_case):
#     n, k = map(int, input().split(" "))  # n = 총 학생수 k = 몇 번째 학생
#     students_score_list = []
#     for i in range(n):
#         middle, last, report = map(int, input().split(" "))
#         student_score = 0.35 * middle + 0.45 * last + 0.2 * report
#         if i == k - 1:
#             kstudent_score = student_score
#         students_score_list.append(student_score)
#
#     students_score_list.sort(reverse=True)  # 점수 정렬
#     for j in range(len(students_score_list)):
#         if kstudent_score == students_score_list[j]:
#             break
#
#     print(f'#{tc+1} {alphabet_socre_list[int((j * 10) // n)]}')

# 1979 어디에 단어가 들어갈 수 있을까?
# def puzzle_checker(arr, cnt=0):
#     # 가로 방향 단어 자리 찾기
#     for row in range(N):
#         for col in range(N - M + 1):
#             if arr[row][col:col + M] == [1 for _ in range(M)]:
#                 if col == (N - M):
#                     if arr[row][col - 1] == 0:
#                         cnt += 1
#                 elif arr[row][col + M] == 0:
#                     if col == 0:
#                         cnt += 1
#                     elif arr[row][col - 1] == 0:
#                         cnt += 1
#
#     return cnt
#
# test_case = int(input())
# for tc in range(test_case):
#     N, M = map(int, input().split(' '))
#     # 맵 입력 받기
#     puzzle_map = [[0 for _ in range(N)] for __ in range(N)]
#     for i in range(N):
#         puzzle_map[i] = list(map(int, input().split()))
#
#     # 가로 방향 단어 자리 찾기
#     cnt = puzzle_checker(puzzle_map, 0)
#     # 맵 회전
#     arr_2 = [[0 for _ in range(N)] for __ in range(N)]
#     for row in range(N):
#         for col in range(N):
#             arr_2[col][N - 1 - row] = puzzle_map[row][col]
#     cnt = puzzle_checker(arr_2, cnt)
#
#     print(f'#{tc + 1} {cnt}')


# 1976 시각 덧셈
# test_case = int(input())
# for tc in range(test_case):
#     hour_1, min_1, hour_2, min_2 = map(int, input().split(' '))
#     if min_1 + min_2 >= 60:
#         result_min = min_1 + min_2 - 60
#         if hour_1 + hour_2 + 1 > 12:
#             result_hour = hour_1 + hour_2 - 11
#         else:
#             result_hour = hour_1 + hour_2 + 1
#     else:
#         result_min = min_1 + min_2
#         if hour_1 + hour_2 > 12:
#             result_hour = hour_1 + hour_2 - 12
#         else:
#             result_hour = hour_1 + hour_2
#
#     print(f'#{tc+1} {result_hour} {result_min}')

# 1974 스도쿠 검증
# def checker(map):
#     ref_list = [num for num in range(1, 10)]
#     # 가로 체크
#     for row in range(9):
#         if ref_list != sorted(map[row][:]):
#             return 0
#
#     # 세로 체크
#     sudoku_map_90 = [[0 for _ in range(9)] for __ in range(9)]
#     for j in range(9):
#         sudoku_map_90[j] = [row[j] for row in map]
#     for row in range(9):
#         if ref_list != sorted(sudoku_map_90[row][:]):
#             return 0
#
#     # 3 * 3 체크
#     for k in range(3):
#         for j in range(3):
#             a = map[3*k][3*j: 3*j + 3] + map[3*k+1][3*j: 3*j + 3] + map[3*k+2][3*j: 3*j + 3]
#             if ref_list != sorted(a):
#                 return 0
#
#     return 1
#
#
# test_case = int(input())
# for tc in range(test_case):
#     sudoku_map = [[0 for _ in range(9)] for __ in range(9)]
#     for i in range(9):
#         sudoku_map[i] = list(map(int, input().split()))
#     print(f'#{tc+1} {checker(sudoku_map)}')

# 1970 쉬운 거스름돈돈

