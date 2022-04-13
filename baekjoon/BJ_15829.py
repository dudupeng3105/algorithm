l = int(input())
# ord('a') = 97
given_str = input()
h = 0
for i in range(l):
    h += ((ord(given_str[i]) - 96) * (31**i))
print(h % 1234567891)