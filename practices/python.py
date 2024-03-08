def search(arr,key):
    n=len(arr)
    for i in range(0,n):
        if key==arr[i]:
            return i
    return -1
arr=[20,30,50,10,40]
key=40
result=search(arr,key)
if result == -1:
    print ("Key is there not there in the Array")
else :
    print("Key is present in the array")