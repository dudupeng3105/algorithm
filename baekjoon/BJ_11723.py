import sys
N = int(sys.stdin.readline())
bit = 0
for _ in range(N):
    given_op = sys.stdin.readline().split()
    if given_op[0] == 'empty':
        bit = 0
    elif given_op[0] == 'all':
        bit = (1 << 20) -1
    else:
        op, x = given_op[0], int(given_op[1]) - 1
        if op == 'add':
            bit |= (1 << x)

        elif op == 'remove':
            bit &= ~(1 << x)

        elif op == 'check':
            if bit & (1 << x) == 0:
                print(0)
            else:
                print(1)

        elif op == 'toggle':
            bit = bit ^ (1 << x)

