# Use print() to print to the console
n = int(input())
# a = list(map(int,input().split()))
store = []
for i in range(n):
    row = list(map(int,input().split()))
    store.append(row)

for i in range(n):
    for j in range(i+1,n):
        store[i][j],store[j][i] = store[j][i],store[i][j]

for i in range(n):
    for j in range(n//2):
        store[i][n-1-j],store[n-1-j][i] = store[n-1-j][i], store[i][n-1-j]

for i in store:
    print(*i)
print("__")
