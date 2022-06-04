import sys

input = sys.stdin.readline

a = input().rstrip()
op = input().rstrip()
b = input().rstrip()

if op == '*':
    digit = len(a) + len(b) - 2
    print('1' + '0' * digit)

elif op == '+':
    if len(a) > len(b):  # 1000 10
        print('1' + '0' * (len(a) - len(b) - 1) + '1' + '0' * (len(b) - 1))
    elif len(a) < len(b):
        print('1' + '0' * (len(b) - len(a) - 1) + '1' + '0' * (len(a) - 1))
    else:  # len(a) == len(b)
        print('2' + '0' * (len(a) - 1))