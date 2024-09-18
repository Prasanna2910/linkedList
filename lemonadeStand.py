a = int(input())
arr = list(map(int,input().split()))
five = 0
ten = 0
for i in arr:
    if i == 5:
        five = five+1
    elif i == 10:
        if five>=1:
            five-=1
            ten+=1
        else:
            print("False")
            exit()
    elif i == 20:
        if five>=3:
            five-=3
        elif ten>=1 and five>=1:
            ten-=1
            five-=1
        else:
            print("False")
            exit()
print("True")    