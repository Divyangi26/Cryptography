
from math import sqrt
def Primenochecker(number):
    if (number<= 1):
        return False
    if (number<= 3):
        return True
    if (number % 2 == 0 or number % 3 == 0):
        return False
    start = 5
    while (start * start <= number):
        if (number % start == 0 or number % (start+ 2) == 0):
            return False
        start+=6
    return True
#act as pow function of primitive root calculation
def primitiverootpower(base, y,modno):
    ans= 1
    base = base % modno
    while (y > 0):
        if (y & 1):
            ans = (ans * base) % modno
        y = y >> 1
        base = (base * base) % modno
    return ans
#calculating prime roots by checking in the list of all prime factors
def Primroots(n):
    temp=n
    l = set()
    if (Primenochecker(n) == False):
        return -1
    n=n-1
    while (n % 2 == 0):
        l.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0):
            l.add(i)
            n = n // i
    if (n > 2):
        l.add(n)
    for element in range(2,temp):
        flag = False
        for item in l:
            if (primitiverootpower(element,(temp-1) // item, temp) == 1):
                flag = True
                break
        if (flag == False):
            return element
    return -1
print("Enter a prime number :")
p=int(input())
print("calculating the primitive root of the given prime nummber")
g=Primroots(p)
print("The value of primitive root of the input prime number: ",g)
print("Select the value of x for Alice: ")
x=int(input())
r1=pow(g,x,p)
print("Select the value of y for Bob: ")
y=int(input())
r2=pow(g,y,p)
print("r1=",r1,"and r2=",r2)
print("----------------if normal diffle hellman key exchange would have taken place------------------------------")
print("Symmetric key for Alice: pow(r1,y,p)= ",pow(r1,y,p))
print("Symmetric key for Bob: pow(r2,y,p)=",pow(r2,x,p))
print("---------------------------------simulating man in the middle attack-------------------------")
print("Enter value for z used by the attacker: ")
z=int(input())
wr1=pow(g,z,p)
print("-----key shared between attacker and bob after man in the middle attack-------- ")
print("key present with the Attacker:",pow(r2,z,p))
print("key received by Bob:",pow(wr1,y,p))
print("-----key shared between attacker and alice after man in the middle attack------- ")
print("key present with the Attacker:",pow(r1,z,p))
print("Key received by Alice:",pow(wr1,x,p))

