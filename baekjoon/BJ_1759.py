def dfs(elements, start):
    if len(elements) == l:
        cnt = 0
        for e in elements:            
            if e in ['a','e','i','o','u']:
                cnt += 1            
        if cnt == 0 or (l-cnt) < 2:
            return
        else:
            print(''.join(elements))
            return
    
    for i in range(start, c):        
        elements.append(alpha_list[i])
        dfs(elements, i + 1)
        elements.pop()  


l, c = map(int, input().split())
alpha_list = list(input().split())
alpha_list.sort()
elements = []
for i in range(0, c - l + 1):
    elements.append(alpha_list[i])
    dfs(elements, i + 1)
    elements.pop()