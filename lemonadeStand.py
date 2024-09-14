# Use print() to print to the console
a = list(map(int, input().split()))
five, ten = 0, 0

for i in range(len(a)):
    if a[i] == 5:
        five += 1
    elif a[i] == 10:
        if five >= 1:
            five -= 1
            ten += 1
        else:
            print("false")
            exit()
    elif a[i] == 20:
        if ten >= 1 and five >= 1:
            ten -= 1
            five -= 1
        elif five >= 3:
            five -= 3
        else:
            print("false")
            exit()

print("true")