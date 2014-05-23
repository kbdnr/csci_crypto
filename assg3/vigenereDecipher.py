# Kevin Bednar - CSCI4905 - Vigenere Cipher Breaker
#Begin by reading and analyzing the ciphertext

## File Input / Analysis
#Read in ciphertext from file
vigCipher = ''
file = open('vigenere-cipher.txt','r')
for line in file:
  vigCipher = line.strip()
file.close()

lenCipher = len(vigCipher)
x = 0
triK = []
triNum = [0]*655
for x in range(lenCipher-3):
  temp = vigCipher[x:x+3]
  if len(temp) == 3:
    if temp in triK:
      tNum = triK.index(temp)
      triNum[tNum]+=1
    else:
      triK.append(temp)
      triNum[len(triK)-1]+=1

triSort = sorted(zip(triNum,triK),reverse=True)
print(triSort)

#Takes most common trigrams found in ciphertext and attempts to do
#the kasiski test
indexes = []
def indexFinder(num,string):
  index = 0
  while index < len(vigCipher):
    index = vigCipher.find(string,index)
    if index == -1:
      break
    print(string,'found at',index)
    indexes.append(index)
    index += 3
    
differences = []
def indexTest(num):
  #perform remainder of test
  for x in range(4):
    #subtract
    differences.append(indexes[5*num+x+1]-indexes[5*num+x])
    print(differences)

for x in range(6):
  indexFinder(x,triSort[x][1])
for x in range(6):
  indexTest(x)
  #find gcd of differences
  #this is the key length
  
keysize=5
print('key length =',keysize)

#create L lists for shift decifers (relative to key size)
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []

cList = list(vigCipher)
for x in range(len(vigCipher)):
  #x mod keysize
  if x%keysize == 0:
    l1.append(cList[x])
  elif x%keysize == 1:
    l2.append(cList[x])
  elif x%keysize == 2:
    l3.append(cList[x])
  elif x%keysize == 3:
    l4.append(cList[x])
  elif x%keysize == 4:
    l5.append(cList[x])

#Shifts characters in list
def shifter(l,num):
  for x in range(len(l)):
    if(ord(l[x])-65)-num < 0:
      l[x] = chr(91 + ((ord(l[x])-65)-num))
    else:
      l[x] = chr(ord(l[x])-num)
  return l

def rebuild(l1,l2,l3,l4,l5):
  #Build plaintext string
  plaintext = ''
  for x in range(len(vigCipher)//5):
    plaintext+=l1[x]+l2[x]+l3[x]+l4[x]+l5[x]
  plaintext+=l1[165]+l2[165]+l3[165]+l4[165]
  return plaintext

def guesser(lst):
  possible = ['E','T','A','O']
  print('Possible values for list:')
  for x in range(4):
    mostFreq = ord(lst[0][1])
    pos = ord(possible[x])
    if (mostFreq - pos) < 0:
      tKey = ((mostFreq - pos) % 26) + 65
      print(chr(tKey),tKey-65)
    else:
      tKey = (mostFreq - pos) + 65
      print(chr(tKey),tKey-65)
          

#Computer freq analysis of each list
def freqAnalyshift():
  tList = []
  nList = [0]*26
  for l in l1:
    if l in tList:
      nList[tList.index(l)]+=1
    else:
      tList.append(l)
      nList[tList.index(l)]+=1
  l1Sort = sorted(zip(nList,tList),reverse=True)
  print(l1Sort)
  
  tList = []
  nList = [0]*26
  for l in l2:
    if l in tList:
      nList[tList.index(l)]+=1
    else:
      tList.append(l)
      nList[tList.index(l)]+=1
  l2Sort = sorted(zip(nList,tList),reverse=True)
  print(l2Sort)
  
  tList = []
  nList = [0]*26
  for l in l3:
    if l in tList:
      nList[tList.index(l)]+=1
    else:
      tList.append(l)
      nList[tList.index(l)]+=1
  l3Sort = sorted(zip(nList,tList),reverse=True)
  print(l3Sort)
  
  tList = []
  nList = [0]*26
  for l in l4:
    if l in tList:
      nList[tList.index(l)]+=1
    else:
      tList.append(l)
      nList[tList.index(l)]+=1
  l4Sort = sorted(zip(nList,tList),reverse=True)
  print(l4Sort)
  
  tList = []
  nList = [0]*26
  for l in l5:
    if l in tList:
      nList[tList.index(l)]+=1
    else:
      tList.append(l)
      nList[tList.index(l)]+=1
  l5Sort = sorted(zip(nList,tList),reverse=True)
  print(l5Sort)
  
  #Dumb guesses
  #key1 = ord(l1Sort[0][1]) - ord('E')
  #key2 = ord(l2Sort[0][1]) - ord('E')
  #key3 = ord(l3Sort[0][1]) - ord('E')
  #key4 = ord(l4Sort[0][1]) - ord('E')
  #key5 = ord(l5Sort[0][1]) - ord('E')
  #print(chr(key1+65),chr(key2+65),chr(key3+65),chr(key4+65),chr(key5+65))

  #use guesser function to give possibilities of the shift
  guesser(l1Sort)
  guesser(l2Sort)
  guesser(l3Sort)
  guesser(l4Sort)
  guesser(l5Sort)

  #10 guesses
  for x in range(10):
    key1 = int(input('Enter key 1: '))
    nl1 = shifter(l1, key1)
    key2 = int(input('Enter key 2: '))
    nl2 = shifter(l2, key2)
    key3 = int(input('Enter key 3: '))
    nl3 = shifter(l3, key3)
    key4 = int(input('Enter key 4: '))
    nl4 = shifter(l4, key4)
    key5 = int(input('Enter key 5: '))
    nl5 = shifter(l5, key5)

    print(rebuild(nl1,nl2,nl3,nl4,nl5))

#executes the primary program functionality
freqAnalyshift()
