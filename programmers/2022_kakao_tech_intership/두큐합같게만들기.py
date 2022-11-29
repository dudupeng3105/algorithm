# 팝 인서트
# 1, 2, 3, 4 -> 2, 3, 4 -> 2, 3, 4, 5
# 3 2 7 2 4 6 5 1
from collections import deque

queue1 = [1, 1] # 14
queue2 = [1, 5] # 16
answer = -2
# [3, 2, 7, 2, // 4, 6, 5, 1 //]
# [3, \\2, 7, 2, 4\\, 6, 5, 1]
# [1,2,1,2,<<1,10,1,2>>]
# 6 14
# 17 3
#
# end 7 -> 4 -> (+5) / s -> 4 -> 6 (+2)
# end 4 + 8 = 12 - 7
# = 7
# [1,2,1,2,1>>,10<<,1,2]
total_q = queue1 + queue2
q_len = len(total_q)
q1_sum = sum(queue1)
q2_sum = sum(queue2)
initial_s = len(queue1)
initial_e = len(total_q) - 1
cnt = 999999
s, e = initial_s, initial_e

while s <= e <= 2*q_len:
    #print(s, e)
    if q1_sum == q2_sum:
        # print(s, e)
        diff_s = (s + q_len // 2) % q_len  # 3 + 4
        diff_e = (e+1) % q_len
        cnt = min(cnt, diff_s + diff_e)
        e += 1
        cal_e = e % q_len
        num = total_q[cal_e]
        q1_sum -= num
        q2_sum += num
    elif q1_sum > q2_sum:
        e += 1
        cal_e = e % q_len
        num = total_q[cal_e]
        q1_sum -= num
        q2_sum += num
    else:  # q1_sum < q2_sum
        cal_s = s % q_len
        num = total_q[cal_s]
        q1_sum += num
        q2_sum -= num
        s += 1

print(cnt)

