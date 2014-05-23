# Kevin Bednar - CSCI4905 - Hill Cipher Breaker
from constants import cHillText,oHillCipher,diHill,diNum
from time import sleep

diSort = sorted(zip(diNum,diHill),reverse=True)
diSorted = [x for y, x in diSort]
numSorted = sorted(diNum, reverse=True)
digrams = []

#invertible elements in Z26
possibleA = [1,3,5,7,9,11,15,17,19,21,23,25]
aInv = [1,9,21,15,3,19,7,23,11,5,17,25]
keyattempt = []

#read in digrams:
file = open('digrams.txt','r')
for line in file:
  digrams.append(line.strip())
file.close()

#Matrix Inverter
def mInverter(a,b,c,d):
  matrix = []
  matrix = [d,(-1 * b)%26,(-1*c)%26,a]
  return matrix

#GCD Calc
def gcd(num1,num2):
  #finds and returns gcd of two numbers
  larger = 0
  smaller = 0
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

def detCalc(a,b,c,d):
  det = (a*d - b*c)%26
  if det == 0:
    return False
  detInv = gcd(det,26)
  if detInv == 1:
    return True
  else:
    return False

def aInverter(num):
  i = possibleA.index(num)
  return aInv[i]

def decrypt(a,b,c,d):
  #multiply 2 letter pairs by possible decryption matrix
  plaintext = ''
  x = 0
  while(x < len(oHillCipher)):
    if x >= len(oHillCipher)-1:
      break
    else:
      l1 = oHillCipher[x]-65
      l2 = oHillCipher[x+1]-65
      p1 = (a*l1 + b*l2)%26 + 65
      p2 = (c*l1 + d*l2)%26 + 65
      plaintext+=chr(p1)
      plaintext+=chr(p2)
      x+=2
  return plaintext

def eqSolver(a,b,c,d,e1,e2):
  print('Attempting to solve:\n(',a,'a+',c,'b)=',e1,sep='')
  print('(',b,'a+',d,'b)=',e2,sep='')
  #Solves out series of equations in form Xa + Yb = Z
  for x in range(26):
    for y in range(26):
      if (a*x+c*y)%26==e1 and (b*x+d*y)%26==e2:
        #detCalc(
        print(x,y)
        #return 2 values from calculations
        return (x,y)

count = 0
valList = []
#while(True):
for x in range(25):
#Using 1 - A,...,26 - Z & mod 27 where 27 = 1 and 26 = 26, etc
  a1 = c1 = ord(diSorted[count][0]) - 64
  b1 = d1 = ord(diSorted[count][1]) - 64
  a2 = c2 = ord(diSorted[count+1][0]) - 64
  b2 = d2 = ord(diSorted[count+1][1]) - 64
  e11 = ord(digrams[count][0]) - 64
  e12 = ord(digrams[count][1]) - 64
  e21 = ord(digrams[count+1][0]) - 64
  e22 = ord(digrams[count+1][1]) - 64
  print(diSorted[count],diSorted[count+1])
  print(digrams[count],digrams[count+1])

  valList.append(eqSolver(a1,a2,b1,b2,e11,e21))
  valList.append(eqSolver(c1,c2,d1,d2,e12,e22))
  print(valList)

  attempt = [a1,b1,a2,b2]
  print(mInverter(attempt[0],attempt[1],attempt[2],attempt[3]))
  inv = mInverter(e11,e12,e21,e22)
  #keyM = [(attempt[0]*inv[0]+attempt[1]*inv[2])%26,(attempt[2]*inv[0]+attempt[3]*inv[2])%26,(attempt[0]*inv[1]+attempt[1]*inv[3])%26,(attempt[2]*inv[1]+attempt[3]*inv[3])%26]
  #print(decrypt(keyM[0],keyM[1],keyM[2],keyM[3]))
  #decrypt(inv[0],inv[1],inv[2],inv[3])
  count+=1

#Brute Force Concept used to find key - reduces attempts from 26^4 to a smaller number using determinant gcd functionality
#for a in range(26):
#  for b in range(26):
#    for c in range(26):
#      for d in range(26):
#        if detCalc:
#          #use of scoring / manual review
#          score(decrypt(a,b,c,d))
#          if score(decrypt(a,b,c,d)) > best:
#            key = [a,b,c,d]

#Correct Key attained from brute force
print('Key = 11,4,7,3')
print(decrypt(11,4,7,3)) #decryption function use
