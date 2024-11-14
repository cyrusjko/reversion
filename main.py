def rev(n):
    if(n>0):
        last=n%10
        if(n//10>0):
            current=rev((int)(n//10))
            return last*pow(10,len((str(current))))+current
        return n
n=int(input("Enter a number: "))
print("Reverse is ", rev(n))