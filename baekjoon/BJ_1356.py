n = input()

if n == '1':
    print('NO')
else:
    for i in range(len(n)):
        start_num = 1
        end_num = 1
        flag = 0
        for x in range(i+1):
            start_num *= int(n[x])
        for y in range(i+1, len(n), 1):
            end_num *= int(n[y])

        if start_num == end_num:
            flag = 1
            break

    if flag:
        print('YES')
    else:
        print('NO')


