import sys

input = sys.stdin.readline

n = int(input())
ref = list(input().rstrip())

pre = []
end = []
len_ref = len(ref)
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
    if len(test) < len_ref - 1:
        flag = 0
    else:
        for i in range(len(pre)):
            if test[i] != pre[i]:
                flag = 0
                break

        if flag:
            for j in range(len(end)):
                if test[-j-1] != end[-j-1]:
                    flag = 0
                    break

    if flag:
        print('DA')
    else:
        print('NE')