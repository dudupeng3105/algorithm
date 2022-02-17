import sys
sys.stdin = open("test.txt")

test_case = int(input())
for tc in range(1, test_case + 1):
    string_1 = input()  # 짧은 문자열
    string_2 = input()  # 긴 문자열
    string_1 = set(string_1)  # 알파벳 중복 제거

    # string_1 set과 같은길이의 0 list로 dict 만듬
    alpha_dict = dict(zip(string_1, [0]*len(string_1)))

    # string 2를 한 글자씩 확인하면서 딕셔너리에 카운트 올라감
    for char in string_2:
        try:
            alpha_dict[char] += 1
        except:  # 키값 없을 때
            continue

    # 최대값 찾기기
    max_value = -1
    # 사전의 값 중에 가장 큰 값 찾기
    for value in alpha_dict.values():
        if value > max_value:
            max_value = value

    print(f'#{tc} {max_value}')