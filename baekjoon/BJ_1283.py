import sys

input = sys.stdin.readline

n = int(input())
arr = []
shortcut = []

for i in range(n):
    temp = list(map(list, input().rstrip().split(" ")))
    arr.append(temp)

for i in range(n):
    word = arr[i]
    # 조각의 맨앞 글자 비교
    flag = 0
    for piece in word:  # piece = ['N', 'e', 'w']
        if piece[0].lower() not in shortcut:
            shortcut.append(piece[0].lower())
            piece[0] = '[' + piece[0] + ']'
            flag = 1  # 단축키 찾았다 이말임
            break

    if not flag:
        for piece in word:  # piece = ['N', 'e', 'w']
            for i in range(len(piece)):
                if piece[i].lower() not in shortcut:
                    shortcut.append(piece[i].lower())
                    piece[i] = '[' + piece[i] + ']'
                    flag = 1  # 단축키 찾았다 이말임
                    break

            if flag:
                break

for i in range(n):
    temp = ''
    for word in arr[i]:
        temp += "".join(word)
        temp += " "
    print(temp.rstrip())
