given_str = input()
joi_num = 0
ioi_num = 0
for i in range(len(given_str)-2):
    check_str = given_str[i:i+3]
    if check_str == 'JOI':
        joi_num += 1
    elif check_str == 'IOI':
        ioi_num += 1
    else:
        continue

print(joi_num)
print(ioi_num)