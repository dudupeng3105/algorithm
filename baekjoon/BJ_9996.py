# 한국이 그리울 땐

import sys

input = sys.stdin.readline

n = int(input())
ref = list(input().rstrip())

pre = []
end = []
len_ref = len(ref)
# 별 기준 앞쪽(pre) 뒤쪽(end) 나눔
for i in range(len_ref):
    if ref[i] == '*':
        a = i
        break
    else:
        pre.append(ref[i])

for i in range(a+1, len_ref):
    end.append(ref[i])

for i in range(n):
    test = list(input().rstrip())
    flag = 1
    if len(test) < len_ref - 1:  # ?*? 보다 짧으면 확인할 필요도 없음
        flag = 0
    else:
        for i in range(len(pre)):  # pre 체크
            if test[i] != pre[i]:
                flag = 0
                break

        if flag:
            for j in range(len(end)):  # end 체크
                if test[-j-1] != end[-j-1]:
                    flag = 0
                    break

    if flag:
        print('DA')  # yes
    else:
        print('NE')  # no