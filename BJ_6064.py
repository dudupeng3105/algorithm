from math import lcm

Test_case = int(input())

for _ in range(Test_case):
    M, N, X, Y = map(int, input().split(" "))
    lcm_M_N = lcm(M, N)
    flag = 0
    if M < N:
        if X == Y:
            flag = 1
            x = X
            y = Y
        else:
            x, y = 0, 0
            X_d = X - x
            x, y = X_d, X_d
            while (x < lcm_M_N) & (y < lcm_M_N):
                x, y = x + M, y + M
                if (y % N) == (Y % N):
                    flag = 1
                    break
    elif M > N:
        if X == Y:
            flag = 1
            x = X
            y = Y
        else:
            x, y = 0, 0
            Y_d = Y - y
            x, y = Y_d, Y_d
            while (x < lcm_M_N) & (y < lcm_M_N):
                x, y = x + N, y + N
                if (x % M) == (X % M):
                    flag = 1
                    break

    else:  # M == N
        if X != Y:
            flag = 0
        else:
            x, y = 0, 0
            Y_d = Y - y
            x, y = Y_d, Y_d
            flag = 1

    if flag == 1:
        print(x)
    else:
        print(-1)
