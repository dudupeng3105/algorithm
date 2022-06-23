import sys
input = sys.stdin.readline

tc = 1
while True:
    left_stack = 0
    right_stack = 0
    given_str = input().rstrip()
    # print(given_str)
    # 종료 조건
    if given_str[0] == '-':
        break

    # 하나씩 확인
    for char in given_str:
        # print(left_stack, right_stack)
        # { 들어오면 left_stack에 담음
        if char == '{':
            left_stack += 1

        else: # char == '}'
            if left_stack:  # 왼쪽괄호있으면 짝이 있는거니까 left_stack에서 하나꺼내서 없애버림
                left_stack -= 1
            else:  # 짝이 없으면 right_stack에 담음
                right_stack += 1

    # 최종 계산
    result = 0
    # 왼쪽애들이 남아 있으면 경우가 2개임 개수가 짝수이면({{{{) -> {}{}이런식으로 left_stack//2
    # 홀수개이면 {{{{{ -> {}{} 하고 {가남는데 이 말은 right_stack에 또 }가 있다는 말임
    # 이 둘은 왜 짝이 못되어을까... -> }{ 이렇게 됐기 때문임 그래서 --> {}로 바꾸려면 2번이 필요함
    # 여기서 나온게 left_stack % 2 입니다.
    result += left_stack // 2 + left_stack % 2
    # right_stack애들도 상황은 똑같음
    result += right_stack // 2 + right_stack % 2
    print(f'{tc}. {result}')
    tc += 1
