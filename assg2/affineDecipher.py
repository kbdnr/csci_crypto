# Kevin Bednar - CSCI4905 - Affine Cipher Breaker
from constants import cAffineText,oAffineCipher,lAffine,numAffine

sortCipher = sorted(zip(numAffine,lAffine), reverse=True)
lSorted = [x for y, x in sortCipher]
numSorted = sorted(numAffine, reverse=True)

#all invertible values in ax+b for a
possibleA = [1,3,5,7,9,11,15,17,19,21,23,25]
aInv = [1,9,21,15,3,19,7,23,11,5,17,25] #given in ch 1, pg 10

def gcd(num1,num2):
  #finds and returns gcd of two numbers
  larger, smaller = 0
  remainderList = []
  dividendList = []
  arrayPos = 0

  if num1 > num2:
    larger = num1
    smaller = num2
  else: #covers ==
    larger = num2
    smaller = num1

  largerList = [larger]
  smallerList = [smaller]
  remainderList.append(1) #arbitrary

  while(remainderList[-1] != 0):
    if arrayPos == 0:
      #Removes arbitrary value
      remainderList.pop(arrayPos)
    dividendList.append(largerList[arrayPos] // smallerList[arrayPos])
    remainderList.append(largerList[arrayPos] % smallerList[arrayPos])
    largerList.append(smallerList[arrayPos])
    smallerList.append(remainderList[arrayPos])
    
    arrayPos += 1
  return smallerList[len(remainderList)-1]

def invertible(num):
  isInv = gcd(num,26)
  if isInv == 1:
    return True
  else:
    return False

def aInverter(a):
  i = possibleA.index(a)
  return aInv[i]

def decrypt(a,b):
  guess = []
  for letter in oAffineCipher:
    guess.append(chr((((letter-65-b)*aInverter(a))%26)+65))
  return guess

def eqSolve(x1,x2,e1,e2):
  solvA = 0
  solvB = 0
  ans = []
  ptext = ''

  for a in possibleA:
    for b in range(26):
      #When the system of equations is solved
      if (((x1*a+b)%26)==e1) and (((x2*a+b)%26)==e2):
        ans = decrypt(a,b) #decrypt using given a and b
        solvA = a
        solvB = b
  print('System solved! Results written to file: affine-plaintext.txt')
  #Output key and solved text to file
  file = open('affine-plaintext.txt','w')
  file.write('key = ' + str(solvA) + 'x + ' + str(solvB) + '\n')
  for l in ans:
    ptext += l
  file.write(ptext)

#Initial guess from cryptanalysis
print('...Solving the following system of equations...')
print(ord('E')-65,'a + b = ',ord(lSorted[0])-65,sep='')
print(ord('T')-65,'a + b = ',ord(lSorted[1])-65,sep='')
eqSolve(ord('E')-65,ord('T')-65,ord(lSorted[0])-65,ord(lSorted[1])-65)

##brute force concept - keyspace 312
#for i in possibleA:
#  for x in range(26):
#    print('attempting ',i,'x +',x)
#    decrypt(i,x)
