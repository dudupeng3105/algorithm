from collections import defaultdict
string = input()
arr = [0 for _ in range(200)]
for char in string:
    arr[ord(char)] += 1

print(chr(arr.index(max(arr))))