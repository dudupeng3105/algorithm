# 6603 로또
# n combination 6

def dfs(elements, start, k):
    if k == 6:
        print(*elements)            
        return
    
    for i in range(start, n):
        elements.append(s[i])
        dfs(elements, i + 1, k + 1)
        elements.pop()


while True:
    given_string = list(map(int, input().split()))
    if given_string[0] == 0:
        break
    else:
        n = given_string[0]        
        s = sorted(given_string[1:])        
        dfs([], 0, 0) # [], start = 0, k = 0 
        print()    










