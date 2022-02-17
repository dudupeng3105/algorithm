import sys
sys.stdin = open('test.txt')
import time
start = time.time()  # 시작 시간 저장

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    result = 0
    for M in range(100, 0, -1):
        for a in range(100-M+1):
            for i in range(100):
                word = ''
                word_reverse = ''
                for j in range(a, M+a):
                    word = word + arr[i][j]
                    word_reverse = arr[i][j] + word_reverse
                if word == word_reverse and len(word) > result:
                    result = len(word)
    for M in range(100, 0, -1):
        for b in range(100-M+1):
            for j in range(100):
                word = ''
                word_reverse = ''
                for i in range(b, M+b):
                    word = word + arr[i][j]
                    word_reverse = arr[i][j] + word_reverse
                if word == word_reverse and len(word) > result:
                    result = len(word)
    print(f'#{tc}', end=' ')
    print(result)
    print("time :", time.time() - start)