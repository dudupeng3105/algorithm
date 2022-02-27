N = int(input())
arr = list(map(int, input().split()))
n = int(input())
for _ in range(n):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(1, N + 1):
            if 0 <= num * i - 1 < N:
                if arr[num*i-1] == 1:
                    arr[num*i-1] = 0
                else:
                    arr[num*i-1] = 1

    elif gender == 2:
        # 여성이라면 일단 자기 자신 먼저 바꾼다
        if 0 <= num-1 < N:
            if arr[num - 1] == 1:
                arr[num - 1] = 0
            else:
                arr[num - 1] = 1

        for i in range(1, N):
            if 0 <= num-1-i < N and 0 <= num-1+i < N:
                if arr[num-1-i] == 0 and arr[num-1+i] == 0:
                    arr[num-1-i] = 1
                    arr[num-1+i] = 1
                elif arr[num-1-i] == 1 and arr[num-1+i] == 1:
                    arr[num-1-i] = 0
                    arr[num-1+i] = 0
                else:
                    break
if N <= 20:
    print(*arr)
else:
    for i in range(N//20 + 1):
        print(*arr[20*i:20*(i+1)])