subarray = []
for i in range(len(arr)):
    for j in range(i,len(arr)):
        store = arr[i:j+1]
        subarray.append(store)

for i in subarray:
    print(i)