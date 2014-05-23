#Kevin Bednar - CSCI 4905 - Assignment 4

def binEnc(character): 
  #Encode plaintext into binary
  if character == ' ': tInt = 26
  elif character == '?': tInt = 27
  elif character == '!': tInt = 28
  elif character == '.': tInt = 29
  elif character == "'": tInt = 30
  elif character == '$': tInt = 31
  else: tInt = ord(character)-65

  #5-bit representation
  nBin = '{:05b}'.format(tInt)
  return nBin

def binDec(binary):
  #Convert binary value to plaintext
  intVal = int(binary,2)
  if intVal == 26: return ' '
  elif intVal == 27: return '?'
  elif intVal == 28: return '!'
  elif intVal == 29: return '.'
  elif intVal == 30: return "'"
  elif intVal == 31: return '$'
  else: intVal = intVal + 65
  return chr(intVal)

print('H',binEnc('H'),'\nI',binEnc('I'))

#Cipher text as given in the problem
cipherText = '011011010101101001000010110110010001000001011001011010110101010100010110110111001110100111110110111110110101010000101111'

#Generates the Keystream based on shift coefficients
def streamGen(initVector,length):
  memory = ''
  memory += initVector
  for x in range(length-5):
    memory += str((int(memory[x]) + int(memory[x+3])) % 2)

  return memory

#Does a diff check against the elements of both the cipherText and the keystream
def streamDiff(memory, cipherText):
  #calculate plain binary based on diff check
  pBin = ''
  for x in range(len(cipherText)):
    if memory[x] == cipherText[x]: pBin+='0'
    else: pBin+='1'
  return pBin

#Debug continued
print(streamGen('01010',len(cipherText)))
print(streamDiff(streamGen('01010',len(cipherText)),cipherText))

binary = streamDiff(streamGen('01010',len(cipherText)),cipherText)

#assignment 4 - 1e)
#Plaintext Solver
ans = ''
for x in range(len(binary)):
  if(x%5 == 0):
    ans += binDec(binary[x:x+5])
print(ans)

#assignment 4 - 1f)
#Plaintext Encoder
exampletext = 'stream ciphers are used in cell phones.'
binSentence = ''
for letter in exampletext:
  binSentence+=binEnc(letter)
keystream = streamGen('01101',len(binSentence))
encodedString = streamDiff(binSentence,keystream)
print(binSentence)
print(keystream)
print(encodedString)
