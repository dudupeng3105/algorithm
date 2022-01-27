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
# 50000, 10000, 5000, 1000, 500, 100, 50, 10
# test_case = int(input())
# money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for tc in range(test_case):
#     N = int(input())
#     result_list = [0 for x in range(8)]
#     print(f'#{tc+1}')
#     result = ''
#     for i in range(8):
#         num = N // money_list[i]
#         result_list[i] = num
#         N = N - num * money_list[i]
#         result = result + str(num) + ' '
    
#     print(result.rstrip())

# 1966 숫자를 정렬하자
# # 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     seq = list(map(int, input().split()))
#     seq.sort()
#     print(f'#{tc+1}', end=' ')
#     for i in range(N-1):
#         print(seq[i], end=' ')

#     print(seq[N-1])
    
# 1961 숫자 배열 회전
# def rotate_90(arr):
#     arr_2 = [[0 for _ in range(N)] for __ in range(N)]
#     for row in range(N):
#         for col in range(N):
#             arr_2[col][N - 1 - row] = arr[row][col]

#     return arr_2


# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     arr = [[0 for _ in range(N)] for __ in range(N)]
#     result_list = [[0 for _ in range(N)] for __ in range(N)]
#     for i in range(N):
#         arr[i] = list(map(int, input().split()))

#     for r in range(3): # 90, 180, 270
#         arr = rotate_90(arr)
#         for i in range(N):
#             if r == 0:
#                 result_list[i] = arr[i]        
#             else:
#                 result_list[i] += arr[i]

#     print(f'#{tc+1}')
#     for i in range(N):
#         for j in range(len(result_list[i])-1):
#             if (j+1) % N == 0:
#                 print(result_list[i][j], end='')
#                 print(' ',end='')            
#             else:
#                 print(result_list[i][j], end='')
#         print(result_list[i][len(result_list[i])-1]) # 마지막 요소

# 1959 두 개의 숫자열
# def max_multiplication(short_list, long_list):
#     result_total = 0
#     for i in range(len(long_list) - len(short_list) + 1):
#         total = 0

#         for j in range(len(short_list)):
#             total += short_list[j] * long_list[j + i]

#         result_total = max(total, result_total)
    
#     return result_total

# test_case = int(input())
# for tc in range(test_case):
#     N, M = map(int,input().split())
#     A_list = list(map(int, input().split()))
#     B_list = list(map(int, input().split()))
#     if N > M:
#         print(f'#{tc + 1} {max_multiplication(B_list, A_list)}')
#     else:
#         print(f'#{tc + 1} {max_multiplication(A_list, B_list)}')

# 1954 달팽이 숫자
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     arr = [[0 for _ in range(N)] for __ in range(N)]
#     num = 1 # 1~n*n 채워넣기
#     i = 0
#     j = 0
#     path_checker = 1 # x 축 양의 방향 전진
#     while num < N**2 + 1:    
#         arr[i][j] = num        
#         if path_checker == 1: # x 축 양의 방향 전진
#             if j == N-1 or arr[i][j+1]:
#                 path_checker = 4 # y 축 음의 방향으로 전환            
#                 i += 1
#             else:
#                 j += 1
        
#         elif path_checker == 4: # y 축 음의 방향으로 전환
#             if i == N-1 or arr[i+1][j]:
#                 path_checker = 3 # x 축 음의 방향 전진            
#                 j -= 1
#             else:
#                 i += 1
        
#         elif path_checker == 3: # x 축 음의 방향 전진
#             if j == 0 or arr[i][j-1]:
#                 path_checker = 2 # y 축 양의 방향 전진            
#                 i -= 1
#             else:
#                 j -= 1
        
#         elif path_checker == 2: # y 축 양의 방향 전진
#             if i == 0 or arr[i-1][j]:
#                 path_checker = 1 # x 축 양의 방향 전진            
#                 j += 1
#             else:
#                 i -= 1
        
#         num += 1

#     print(f'#{tc + 1}')
#     for row in arr:
#         print(*row)

# # 1948 날짜 계산기
# month_days = [0, 31, 28, 31, 30, 31\
#             ,30, 31, 31, 30, 31, 30, 31]
# test_case = int(input())
# for tc in range(test_case):
#     m1, d1, m2, d2 = map(int, input().split())

#     if m1 == m2: # 달이 같은 경우
#         print(f'#{tc + 1} {d2 - d1 + 1}')
#     else:
#         total_days = month_days[m1] - d1 + 1  # 첫 달 날짜     
        
#         for i in range(m1 + 1, m2): # m1+1 ~ m2 -1 달 날짜 합침
#             total_days += month_days[i]

#         total_days += d2 # 마지막 달 날짜 합산

#         print(f'#{tc + 1} {total_days}')

# 1946 간단한 압출 풀기
# test_case = int(input())
# for tc in range(test_case):
#     result_str = ''
#     N = int(input())
#     for _ in range(N):
#         c, k = input().split()
#         k = int(k)
#         result_str += c*k

#     print(f'#{tc + 1}')
#     if len(result_str) < 10:
#         print(result_str[:])
#     else:
#         for i in range(len(result_str)//10):
#             print(result_str[10*i: 10*(i+1)])
#         print(result_str[10*(i+1):])    

# 1945 간단한 소인수분해
# test_case = int(input())
# num_list = [2, 3, 5, 7, 11]
# result_list = [0, 0, 0, 0, 0] # a,b,c,d,e
# for tc in range(test_case):
#     N = int(input())
#     result_list = [0, 0, 0, 0, 0]
#     for i in range(len(num_list)):
#         divider = num_list[i]
#         while N % divider == 0:
#             N = N // divider
#             result_list[i] += 1
    
#     print(f'#{tc + 1}', end = ' ')
#     print(*result_list)

# 1928 Base64 Decoder
# LIF => 01001100 01101001 01100110 => TGIM
# test_case = int(input())
# # base_64 역변환표 문자 -> 숫자
# num_list = [x for x in range(64)]
# word_list = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]\
#             + [str(x) for x in range(10)]  + ['+','/']
# base_64_dict = dict(zip(word_list, num_list))

# for tc in range(test_case):
#     given_str = input()
#     bit_string = ''
#     for char in given_str:
#         value = base_64_dict[char]
#         a = format(value, 'b')
#         bit_string += a.zfill(6) # 한 글자당 6비트로 만들어 졌으니까

#     print(f'#{tc + 1}', end = ' ')
#     for i in range(len(bit_string)//8): # 8비트씩 읽음
#         a = int(bit_string[8*i: 8*(i+1)], 2) # 2진수 -> 10진수
#         print(chr(a),end='') # 아스키코드에 맞는 문자 출력
#     print() # 줄 바꿈


# 1288 새로운 불면증 치료법
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     add = N
#     res = set()    
#     while len(res) < 10:
#         res.update(list(str(N)))        
#         N = N + add        
    
#     print(f'#{tc + 1} {N-add}')

# 1284. 수도 요금 경쟁
# test_case = int(input())
# for tc in range(test_case):    
#     p, q, r, s, w = map(int,input().split())
#     company_a_price = w * p
#     if w < r:
#         company_b_price = q
#     else:
#         company_b_price = q + (w-r)*s

#     if company_a_price > company_b_price:
#         print(f'#{tc + 1} {company_b_price}')
#     else:
#         print(f'#{tc + 1} {company_a_price}')
# 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# from collections import Counter
# test_case = int(input())
# for tc in range(test_case):
#     N = int(input())
#     num_lst = list(map(int,input().split()))
#     c1 = Counter(num_lst)
#     print(f'#{tc + 1} {c1.most_common(1)[0][0]}')

# 1940. 가랏! RC카!
test_case = int(input())
for tc in range(test_case):
    N = int(input())
    res_distance = 0
    vel = 0
    for _ in range(N):
        given_command = input()
        if given_command == '0':
            command = 0
            res_distance += vel
        else: 
            command, acc = map(int, given_command.split())
            if command == 1: # 가속
                vel = vel + acc
            else: # 감속
                vel = vel - acc
                if vel < 0:
                    vel = 0
            
            res_distance += vel
        
    print(f'#{tc + 1} {res_distance}')
            
    


