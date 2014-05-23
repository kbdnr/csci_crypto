cAffineText = ''
oAffineCipher = []
cHillText = ''
oHillCipher = []
lAffine = []
numAffine = [0] * 26

#Digram text analysis only for hill cipher
diHill = []
diNum = [0]*310

#Frequency Analysis of Affine Cipher
file = open('affine-cipher.txt','r')
for line in file:
  line = line.strip()
  cAffineText = line
  for letter in line:
    oAffineCipher.append(ord(letter))

for letter in cAffineText:
  if letter in lAffine:
    tNum = lAffine.index(letter)
    numAffine[tNum] += 1
  else:
    lAffine.append(letter)
    numAffine[len(lAffine)-1] += 1

file.close()

#Frequency Analysis of Hill Cipher
file = open('hill-cipher.txt','r')
for line in file:
  line = line.strip()
  cHillText = line
  for letter in line:
    oHillCipher.append(ord(letter))

for count in range(len(cHillText)):
  #Grab two letter segments
  digram = cHillText[count:count+2]
  if len(digram) == 2:
    if digram in diHill:
      tNum = diHill.index(digram)
      diNum[tNum]+=1
    else:
      diHill.append(digram)
      diNum[len(diHill)-1]+=1

file.close()
