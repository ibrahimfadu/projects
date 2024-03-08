x=int(input("Enter the value :"))
if x!=0:
    for i in range(2,x):
        if x%i==0:
            print("not prime")
            break
        else:
            print("Prime ")
else:
    print("Zero")