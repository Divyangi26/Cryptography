**RSA CRYPTOSYSTEM
import random
print(“---------key generation-----------")
print(“Enter the prime number p: “)
p=int(input())
print(“Enter the prime number q: “)
q=int(input())
n=p*q
print(“The value of n= p*q is: “,n)
print(“Enter the plaintext to be encrypted: “)
pt=input()
totient=(p-1)*(q-1)
print(“The value of phi(n): “,totient)
def greatcommondivisor(x1,x2):
    if x2==0:
        return x1
    else:
        return greatcommondivisor(x2,x1%x2)
def modularInversecal(a,m):
    a = a%m
    for x in range(1,m):
       if (a*x)%m ==1:
          return x
while 1:
        e = random.randrange(1,totient)
        g = greatcommondivisor(e,totient)
        d = modularInversecal(e,totient)
        if g == 1 and e != d:
            break
print(“The public key is: (“,e,”,”,n,”)”)
print(“\n”)
print(“The private key is: “,d)
print(“--------------Encryption----------------------")
print(“\n”)
cipher= [pow(ord©, e, n) for c in pt]
print(“The cipher text in numerical form: “)
print(‘’.join(map(lambda x: str(x), cipher)))
print(“\n”)
print(“The cipher text in text form: “)
ctext=[chr© for c in cipher]
print(*ctext)
print(“\n”)
print(“-----------Decryption------------------")
print(“\n”)
pn=[pow(c,d,n) for c in cipher]
print(“The plaintext in numerical form: “)
print(‘’.join(map(lambda x: str(x), pn)))
print(“\n”)
print(“The original message or the decrypted message: “)
plaintext = [chr(pow(c, d, n)) for c in cipher]
print(*plaintext)

