# 참고용 코드
from sys import stdin

n = int(stdin.readline())
board = []

for i in range(n):
    row = stdin.readline().replace('T', '1').replace('H', '0')
    #print(row)
    row = int(row, 2)
    #print(row)
    board.append(row)

minT = 1 << n

for i in range(1 << n):
    numT = 0
    for row in board:
        #print(row)
        rowT = bin(i ^ row).count('1')  # xor연산에서 비트1인 0 이면 결과가 비트2와 같음
        # 그리고 비트1이 1이면 not 비트2와 결과가 같음 이걸 이용한 듯
        print(rowT)
        if 2 * rowT < n:
            numT += rowT
        else:
            numT += n - rowT
    # 열은 따로 체크 안한 듯..
    if minT > numT:
        minT = numT

print(minT)
