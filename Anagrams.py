arr = input().split()
t = arr[0]
s = arr[1]
# print(t)
# print(s)

dic1 = {}
dic2 = {}
for i in range(len(t)):
    if t[i] in dic1:
        dic1[t[i]] = dic1[t[i]] + 1
    else:
        dic1[t[i]] = 1
for i in range(len(s)):
    if s[i] in dic2:
        dic2[s[i]] = dic2[i[i]] + 1
    else:
        dic2[s[i]] = 1
if len(s) == len(t):
    if dic1 == dic2:
        print("Anagrams")
    else:
        print("Not Anagrams")
else:
    print("Not Anagrams")