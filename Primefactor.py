import math
n=int(input("Enter an integer:"))
def is_prime(n):
    i=1
    prime_factors = [1]
    while(i<= (n**0.5)):
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                prime_factors.append(i)
        i=i+1
    if len(prime_factors)==1:
        is_prime_num = True
    else:
        is_prime_num = False
    return {"Is prime": is_prime_num, "Prime factors": prime_factors}
print (is_prime(n))

print (is_prime(n)["Is prime"])
print (is_prime(n)["Prime factors"])