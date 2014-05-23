#Constants.py - Handles file input and basic frequency analysis of both files
oShiftCipher = [] #original cipher list
oSubCipher = [] #original cipher list
cShiftText = ''
cSubText = ''
lShift = []
lSub = []
numShift = [0] * 26
numSub = [0] * 26
digrams = []
trigrams = []
primaryLetter = ['E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']

file = open('shift-cipher.txt','r')

for line in file:
  line = line.strip()
  cShiftText = line
  for letter in line:
    #fill oShiftCipher list with integer mapping of letters
    oShiftCipher.append(ord(letter))

for letter in cShiftText:
  if letter in lShift:
    tNum = lShift.index(letter)
    numShift[tNum]+=1
  else:
    lShift.append(letter)
    numShift[len(lShift)-1]+=1

#DEBUG
#for count in range(len(lShift)):
  #print(lShift[count],numShift[count])

#CLEANUP
file.close()
#DEBUG

#Freq. Analysis of Substitution cipher
file = open('substitution-cipher.txt','r')

for line in file:
  line = line.strip()
  cSubText = line
  for letter in line:
    #fill oSubCipher list with integer mapping of letters
    oSubCipher.append(ord(letter))

for letter in cSubText:
  if letter in lSub:
    tNum = lSub.index(letter)
    numSub[tNum]+=1
  else:
    lSub.append(letter)
    numSub[len(lSub)-1]+=1

file.close()

#Read in digrams and trigrams
file = open('digrams.txt','r')
for line in file:
  digrams.append(line.strip())
file.close()

#Compute digram frequency for substitution cipher only
#using cSubText
diSub = []
diNum = [0]*250
for count in range(len(cSubText)):
  #Grab 2 letter segment
  digram = cSubText[count:count+2]
  if len(digram) == 2:
    if digram in diSub:
      tNum = diSub.index(digram)
      diNum[tNum]+=1
    else:
      diSub.append(digram)
      diNum[len(diSub)-1]+=1

file = open('trigrams.txt','r')
for line in file:
  trigrams.append(line.strip())
file.close()

#Compute trigram frequency for substitution cipher only
triSub = []
triNum = [0]*250
for count in range(len(cSubText)):
  #Grab 3 letter segment
  trigram = cSubText[count:count+3]
  if len(trigram) == 3:
    if trigram in triSub:
      tNum = triSub.index(trigram)
      triNum[tNum]+=1
    else:
      triSub.append(trigram)
      triNum[len(triSub)-1]+=1
