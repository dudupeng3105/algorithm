s = "ababcdcdababcdcd"
answer = 9999
# len(s)//2
for window in range(3, 4):
    remain = len(s) % window
    quotient = len(s) // window
    for i in range(quotient):
        print(window * quotient, window * (quotient + 1))
        strg = s[window * quotient: window * (quotient + 1)]
        print(strg)

