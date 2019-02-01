#gopi
x=int(input())
if (x>0):
    for i in range(2,x):
        if (x%i==0):
            print("No")
            break
        else:
            print("Yes")
            break
else:
    print("No")
