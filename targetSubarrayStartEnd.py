a = int(input())
arr = list(map(int,input().split()))
tar = int(input())
flag = False
for i in range(len(arr)):
    store = 0
    for j in range(i,len(arr)):
        store = store + arr[j]
        if store == tar:
            print(i,j)
            flag = True
            break
else:
    print("NO subarray")
