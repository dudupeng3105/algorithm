n = int(input())

result_lst = []
result_length = 0
for i in range(n//2, n+1):
    temp = [n, i]
    flag = 1
    i = 2
    while True:
        addition_num = temp[i-2] - temp[i-1]
        if addition_num < 0:
            break
        else:
            temp.append(addition_num)

        i += 1

    if i > result_length:
        result_length = i
        result_lst = temp[:]

print(result_length)
print(*result_lst)