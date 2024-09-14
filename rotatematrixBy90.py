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
    for j in range(n // 2):
        store[i][j], store[i][n - 1 - j] = store[i][n - 1 - j], store[i][j]

for i in store:
    print(*i)
print("__")
