l = int(input())
arr = list(map(int, input().split()))
if l == 0:
    print("0")
else:
    ma = float('-inf') 
    for i in range(0, l):
        store = 0
        for j in range(i, l):
            store = store + arr[j]
            ma = max(store, ma)
    print(ma)