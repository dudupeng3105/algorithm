test_case = int(input())

for tc in range(test_case):
    given_bin = input()
    for i in range(len(given_bin)//7):
        temp_bin = given_bin[7*i: 7*(i+1)]
        square_num = 0
        a = 0
        for num_bin in temp_bin[::-1]:
            a += int(num_bin) * (2**square_num)
            square_num += 1
        print(a, end=' ')
    print()
