N = int(input())
if N % 2:  # 홀수
    arr = [1, 2] * (N // 2)
    arr.append(3)
    print(*arr)
else:
    arr = [1, 2] * (N // 2)
    print(*arr)


