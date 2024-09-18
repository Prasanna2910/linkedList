arr = input().strip()
flag = False
for i in range(len(arr)):
    rotated = arr[i:] + arr[:i]
    if rotated == rotated[::-1]:
        print("Yes, it is a palindrome.")
        flag = True
        break
if not flag:
    print("Not a palindrome")