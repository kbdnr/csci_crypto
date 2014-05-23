#Shift Cipher Decrypt Program - CSCI 4905 - Kevin Bednar

#Begin by importing important details from constants
from constants import cShiftText,lShift,numShift,primaryLetter

#Letters to attempt shift by, in order of highest chance to lowest chance
attemptShift = primaryLetter
key = 0 #Initialize key (attempt)
plaintext = ''

#Find most frequent letter given information from constants
large = 0
pos = 0
#Find most frequent Letter
maxNum = max(numShift)
i = numShift.index(maxNum)
l = lShift[i]

print('Most frequent letter is:',l,'appearing',maxNum,'times')
print('It is highly plausible that',l,'may be equal to E')

#Try shifts by most common letters (descending)
for letter in attemptShift:
  #Find shift amount between l[pos] (O) and l (E,T,A,O...,R)
  #If Ciphertext is shifted
  if(ord(l) != ord(letter)):
    #Find key
    key = ord(l) - ord(letter)
    if key < 1:
      key = 26 + key
    print('Shift key between',l,'and',letter,'is',key,'.  Attempting Shift...')

    #For each letter in cipher text - shift by key
    for eL in cShiftText:
      if ord(eL)-key < 65:
        plaintext = plaintext + chr(90+(ord(eL)-key)-64)
      else:
        plaintext = plaintext + chr(ord(eL)-key)
    print(plaintext)
    i = input('Does this seem correct? (y/n) ')
    #If user confirms text as correct - write to file
    if i == 'y':
      f = open('shift_plaintext.txt','w')
      f.write(plaintext + '\n' + str(key))
      f.close()
      print('File written to shift_plaintext.txt including plaintext and key')
      break

  #Reset Plaintext per attempt
  plaintext = ''
