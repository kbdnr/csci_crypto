#Kevin Bednar - CSCI4905 - Breaking the RSA Cryptosystem
import math
import time

#Given Constants:
n = 2177994659
b = 65537

def rangeapprox(n): #Find approximate factor (minimizes prime range)
  return math.floor(math.sqrt(n))

#Recursive Euclidean Algorithm
def rEEA(a,b):
  if a == 0:
    return (b,0,1)
  else:
    g,y,x = rEEA(b % a,a)
    return (g, x - (b//a) * y, y)

#Modular Inverse calculator
def inverse(a, m):
  gcd, x, y = rEEA(a, m)
  if gcd != 1:
    return None
  else:
    return x % m

#Begin finding prime factors with the square root of n
approxFactor = rangeapprox(2177994659)
approxFactor-=1 #To make odd
p = q = 0

while(True):
  if n % approxFactor == 0:
    p = approxFactor
    break
  approxFactor-=2

#from primegen import primes
#if p in primes:      #Check whether the given value is a prime number

#Solve for q after finding p
q = n // p
print('p =',p,'q =',q)

#Determine phi(n)
#Easily done here since both p/q are primes
phiN = (p-1)*(q-1)
print('phi(n) =',phiN)

#Compute Decryption exponent, a as the inverse of b modulo phi(n)
inv = inverse(b,phiN)
print('a =',inv)

#Decrypt ciphertext
file = open('rsa-cipher.txt')
ciphertext = ''
for line in file:
  ciphertext = line

#For each 'chunk' of ciphertext, calculate compute inverse mod n
chunks = ciphertext.split()
decChunks = []
for chunk in chunks:
  decChunks.append(pow(int(chunk),inv,n))
  #where 3 argument pow uses square/multiply
#print(decChunks)

#Useful approach which essentially solves the linear system as if it were in base 26
ptext = ''
for chunk in decChunks:
  a = chunk // 26**5
  chunk-=a*26**5
  b = chunk // 26**4
  chunk-=b*26**4
  c = chunk // 26**3
  chunk-=c*26**3
  d = chunk // 26**2
  chunk-=d*26**2
  e = chunk // 26
  chunk-=e*26
  f = chunk
  #print(a,b,c,d,e,f)
  #print(chr(a+65),chr(b+65),chr(c+65),chr(d+65),chr(e+65),chr(f+65))
  ptext += chr(a+65) + chr(b+65) + chr(c+65) + chr(d+65) + chr(e+65) + chr(f+65)
print(ptext)
