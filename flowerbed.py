n = int(input())
toplant = int(input())
arr = list(map(int,input().split()))
coplant = 0
for i in range(len(arr)):
    if arr[i] == 0:
        left = (i==0) or (arr[i-1] == 0)
        right = (i == n-1) or (arr[i+1] == 0)
        if left and right:
            arr[i] = 1
            coplant = coplant + 1
            if coplant >= toplant:
                break
if coplant>=toplant:
    print("True")
else:
    print("False")