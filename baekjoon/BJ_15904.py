given_string = input()
state = 0
flag = 0
for char in given_string:
    if state == 0:
        if char == 'U':
            state = 1

    elif state == 1:
        if char == 'C':
            state = 2

    elif state == 2:
        if char == 'P':
            state = 3

    else:  # 3
        if char == 'C':
            flag = 1
            break

if flag:
    print('I love UCPC')
else:
    print('I hate UCPC')


