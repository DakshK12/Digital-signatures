#Part 1
import math
import hashlib
def isPrime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True    
    

def phi(n):
    pro=n
    for i in range(2,n+1):
        if(isPrime(i) and n%i==0):
            pro=pro*(i-1)/i;
    pro=math.floor(pro)        
    return (pro)

p,q,e=43,47,155
phin=phi(p*q)

d=0
for i in range(1,phin):
    if((i*e)%phin==1):
        d=i
        break
publickey=(p*q,e)
privatekey=(p*q,d)

#Part 2
n=p*q
def hashing(s,n):
    sumi=0
    po=1
    m=256
    for i in s:
        sumi=sumi+ord(i)*po
        po=po*m    
    return sumi%n    
#Alice part
m="2101-CON101 INTRODUCTION TO COMP.SC. amp; ENG"

hashcode=0
hashcode=hashing(m,n)

x=(hashcode**d)%(n)

s=""
s=s+str(x%256)
x=x//256

while(x>0):
    s=s+"."+str(x%256)
    x=x//256
signature=s
#Bob part
a1=s.split(".")

sum2=0
po=1
for i in a1:
    sum2=sum2+int(i)*po
    po=po*256
hashcode2=hashing(m,n)
y=(sum2**e)%n
#Output
print("Euler's phi function is",phin)
print("public key is",publickey)
print("private key is",privatekey)
print("signature is",signature)
print("digest of hash is",hashcode)
print("h generated by Bob is",y)

    
