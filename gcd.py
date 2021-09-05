def gcd(a,b):
    if (b==0):
        return a;
    else:
        return gcd(b,a%b)

print("Input two nos.:")
m=int(input())
n=int(input())
print("GCD of "+str(m)+ " and "+str(n)+" is: "+str(gcd(m,n)))