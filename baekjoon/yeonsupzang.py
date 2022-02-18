num_list = list(map(int, input().split()))

serial_num = 0
for num in num_list:
    serial_num += num**2

print(serial_num%10)