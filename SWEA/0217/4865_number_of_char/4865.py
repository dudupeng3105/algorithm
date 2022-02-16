import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    string_1 = list(input())
    string_2 = list(input())
    string_1 = set(string_1)

    alpha_dict = dict(zip(string_1, [0]*len(string_1)))

    for char in string_2:
        if char in string_1:
            alpha_dict[char] += 1

    # 최대값 찾기기
    max_value = -1
    for value in alpha_dict.values():
        if value > max_value:
            max_value = value

    print(f'#{tc} {max_value}')