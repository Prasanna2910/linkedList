g = list(map(int,input().split()))
s = list(map(int,input().split()))
store = 0
g.sort()
s.sort()
j = 0
for i in range(len(g)):
    while j<len(s):
        if s[j] >= g[i]:
            store = store + 1
            j = j+1
            break
        j = j+1
print(store)