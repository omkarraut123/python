def GCD(x,y):
    if x==0:
        return y
    if y==0:
        return x
    return GCD(y,x%y)  

x=6
y=4
gcd=GCD(x,y)    
print("GCD of {0} and {1} is {2}".format(x,y,gcd))
lcm=(x*y)//gcd
print("LCM is ",lcm)

