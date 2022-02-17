import sys
import time


def find_palindrome(max_length):
    for r in range(100): # 행
        for palindrome_length in range(100, max_length, -1):
            if palindrome_length < max_length:  # for 문 중도에 max_length 바꼈을 때 경우
                break
            else:
                for start in range(100-palindrome_length+1):
                    if arr[r][start:start+palindrome_length] == arr[r][start:start+palindrome_length][::-1]:
                        if palindrome_length > max_length:
                            max_length = palindrome_length
                            break

    return max_length


def longest_palindrome(arr):
    # 가로
    max_length = find_palindrome(0)

    # 전치행렬
    for i in range(100):
        for j in range(100):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 세로
    result_max_length = find_palindrome(max_length)

    return result_max_length


sys.stdin = open("test.txt")

for _ in range(10):
    tc = int(input())
    arr = [[] for _ in range(100)]
    for i in range(100):
        arr[i] = list(input())
    start = time.time()  # 시작 시간 저장
    print(f'#{tc} {longest_palindrome(arr)}')
    print("time :", time.time() - start)