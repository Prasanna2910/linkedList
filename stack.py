a, b = map(int,input().split())
store = []
track = []
def top(store):
    # print(store[-1])
    track.append(store[-1])
def push(store,j):
    if len(store)>b:
        # print("Stack Overflow")
        track.append("Stack Overflow")
    else:
        store.append(j)
def pop(store):
    if len(store)<=0:
        # print("Stack Underflow")
        # store.append("Stack Underflow")
        track.append("Stack Underflow")
    else:
        s = store.pop()
        # print(s)
        track.append(s)
for i in range(a):
    j= input().split()
    if j[0] == "push":
        # store.append(j[1])
        push(store,j[1])
    elif j[0] == "pop":
        pop(store)
    elif j[0] == "top":
        top(store)
# print(top(store))
for i in track:
    print(i)
        
        
# print(store)
    