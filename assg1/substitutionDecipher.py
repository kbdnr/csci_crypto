#Substitution Cipher Decryption Program - CSCI4905 - Kevin Bednar

# -- Import Constants --
from constants import cSubText,lSub,numSub,digrams,trigrams,primaryLetter,diSub,diNum,triSub,triNum
from math import log10
from random import choice

# -- Global Variables --
#Single Letters
sortCipher = sorted(zip(numSub,lSub),reverse=True) #Sort Relative Frequencies - lSorted as letters sorted, numSorted as numbers sorted
lSorted = [x for y, x in sortCipher]
numSorted = sorted(numSub,reverse=True)
#Digrams
diSort = sorted(zip(diNum,diSub),reverse=True)
diSorted = [x for y, x in diSort]
diNumSort = sorted(diNum,reverse=True)
#Trigrams
triSort = sorted(zip(triNum,triSub),reverse=True)
triSorted = [x for y, x in triSort]
triNumSort = sorted(triNum,reverse=True)
#Guess Array
trialText = ['_'] * len(cSubText) #trial text for testing purposes
#Declare lists for tracking replacements
replacement = []
freplacement = []
remainingL = []
pos = 0

#  -- Functions --
#Handles replacement of letters
def replace(oLetter, nLetter, rep = 1):
  #Function handles replacement of characters - old letter / new letter
  #Find indices of old letter
  indices = [i for i, x in enumerate(cSubText) if x == oLetter]
  #Replace old indices with new letter
  for i in indices:
      trialText[i] = nLetter
  if rep == 1:
    replacement.append([oLetter,nLetter])

#Allows for manual backtrack of guesses, useful if user solves manually
def rollback(position = -1):
  #Replace last nLetter edit with '_' in trialText
  indices = [i for i, x in enumerate(trialText) if x == replacement[position][1]]
  #Add failed replacement to list
  freplacement.append(replacement[position])
  for i in indices:
      trialText[i] = '_'

#Print remaining plaintext letters and ciphertext letters to be solved and their relative frequencies respectively
def lRemain():
  attempts = [x[1] for x in replacement]
  cipher = [x[0] for x in replacement]
  remainingL = [x for x in primaryLetter if x not in attempts]
  remainingC = [x for x in lSorted if x not in cipher]
  print('\nRemaining plaintext letters:',remainingL)
  print('Remaining ciphertext chars: ',remainingC)

#Map remaining unsolved ciphertext/plaintext letters for use with hill climbing
def lremMap():
  #use lRemain functionality to guess cipher/plaintext key by frequency of remaining chars
  attemps = [x[1] for x in replacement]
  cipher = [x[0] for x in replacement]
  remainingL = [x for x in primaryLetter if x not in attemps]
  remainingC = [x for x in lSorted if x not in cipher]
  for l in range(len(remainingC)):
    replace(remainingC[l],remainingL[l],rep=0)

## -- Digram Function --
#def diApply(pos):
#  print('\nDigram Statistics\n')
#  #use solved letters to find related digrams
#  possible0 = []
#  possible1 = []
#  cpossible0 = []
#  cpossible1 = []
#
#  #for one relevant letter at a time
#  count = pos
#  for count in range(pos+1):
#    #Plaintext Digram Possibilities
#    for di in digrams:
#      if di.find(replacement[count][1]) == 0:
#        #Replacement possibility is in position 2
#        possible1.append([di,digrams.index(di)])
#      elif di.find(replacement[count][1]) == 1:
#        #Replacement possiblity is in position 1
#        possible0.append([di,digrams.index(di)])
#      else:
#        #not found
#        pass
#
#    #Ciphertext Digram Possibilities
#    for di in diSort:
#      if di[1].find(replacement[count][0]) == 0:
#        #Replacement possibility is in position 2
#        cpossible1.append(di)
#      elif di[1].find(replacement[count][0]) == 1:
#        #Replacement possiblity is in position 1
#        cpossible0.append(di)
#      else:
#        #not found
#        pass
#
#  #possible contains digrams which contain a solved letter on either side
#  #remove digrams in possible that contain two already solved letters
#  print('Here is information regarding digram frequency in the form\nCipher Digram Freq -- Most Likely Digram (out of 50) -- (first letter replacements)')
#  cp0 = [[b,a] for a,b in cpossible0]
#  for x in range(len(possible0)):
#    print(cp0[x],' -- ',possible0[x],'consider replacing',cp0[x][0][0],'with',possible0[x][0][0])
#
#  cp1 = [[b,a] for a,b in cpossible1]
#  print('(second letter replacements)')
#  for x in range(len(possible1)):
#    print(cp1[x],' -- ',possible1[x],'consider replacing',cp1[x][0][1],'with',possible1[x][0][1])
#
## --Trigram function--
#def triApply(pos):
#  print('\nTrigram Statistics\n')
#  #Using primary guesses and trigram frequency try replacements
#  #List of cipher solved charactear
#  replaceC = [x[0] for x in replacement]
#  #List of plaintext solved characters
#  replaceS = [x[1] for x in replacement]
#  l1 = replaceS[pos]
#  l2 = replaceS[pos+1]
#  r1 = replaceC[pos]
#  r2 = replaceC[pos+1]
#  #List to hold one and two letter trigrams found
#  tlTri = []
#  olTri = []
#
#  print('Searching for trigram relevance using letters: ',l1,l2)
#  count = pos
#  for count in range(pos+1):
#    for tri in trigrams:
#      #find two letters
#      if tri.find(l1) != -1:
#        if tri.find(l2) != -1:
#          #Contains two letters
#          tlTri.append(tri)
#      #find one letter
#      elif tri.find(l1)!= -1 or tri.find(l2) != -1:
#        olTri.append(tri)
#      else:
#        pass
#
#  #Give likeliness output similar to diApply()
#  print('The following digrams were found containig two previously solved letters:')
#  for x in tlTri:
#    print(x,' -- ',trigrams.index(x) + 1)

#Allows for user to take a guess given digram/trigram statistics or intuition
def userGuess():
  seeRemaining = input('Would you like to see the remaining choices? (y/n) ')
  if seeRemaining == 'y':
    lRemain()
  #Ask for for cipher letter and plaintext guess
  ogCipher()
  oLetter = input('Which cipher text letter would you like to replace? (uppercase input) ')
  nLetter = input('What would you like ' + oLetter + ' mapped to? (uppercase input) ')
  replace(oLetter,nLetter)

#Prints original cipher text in list character format (for ease of comparison with trialText)
def ogCipher():
  #Function for ease of trialText / cipher text comparison
  ogCipher = []
  for x in cSubText:
    ogCipher.append(x)
  print(ogCipher)

# -- For Hill Climbing score comparison --
pdict = {}
file = open('english_quintgrams.txt','r')
for line in file:
  key,count = line.split()
  pdict[key] = int(count)
dictL = len(key)
dictN = sum(pdict.values())
for key in pdict:
  pdict[key] = log10(float(pdict.get(key) / dictN))
floor = log10(0.01/dictN)

#Handles intelligent fill of remaining letters with use of frequency relations
def hillClimb():
  cipherText = ''
  best = []
  parent = -99e99 #extremely low value (to be replaced)
  test = parent

  attempts = [x[1] for x in replacement]
  cipher = [x[0] for x in replacement]
  remainingL = [x for x in primaryLetter if x not in attempts]
  remainingC = [x for x in lSorted if x not in cipher]

  #Sort letters into lists based upon frequency E / TAOINSHR / DL / CUMWFGYPB / VKJXQZ
  # 5 Lists - E is already handled --> 4 Lists
  l2 = [] # is ~ TAOINSHR
  l3 = [] # is ~ DL
  l4 = [] # is ~ CUMFGYPB
  l5 = [] # is ~ VKJXQZ

  #Each letter is sorted by approximated mappings, with useful overlaps
  for x in range(8):
    l2.append(lSorted[x+1])
  for x in range(5):
    #Riskier Guesses
    l3.append(lSorted[x+8])
  for x in range(10):
    l4.append(lSorted[x+11])
  for x in range(7):
    l5.append(lSorted[x+19])

  #Remove previous guesses from digram/trigram completion
  l2 = [x for x in l2 if x in remainingC]
  l3 = [x for x in l3 if x in remainingC]
  l4 = [x for x in l4 if x in remainingC]
  l5 = [x for x in l5 if x in remainingC]

  l2o = ['T','A','O','I','N','S','H','R']
  l3o = ['D','L']
  l4o = ['C','U','M','F','G','Y','P','B']
  l5o = ['V','K','J','X','Q','Z']

  #Remove previously used letters
  l2o = [x for x in l2o if x in remainingL]
  l3o = [x for x in l3o if x in remainingL]
  l4o = [x for x in l4o if x in remainingL]
  l5o = [x for x in l5o if x in remainingL]

  #hill climbing algorithm to fill in remaining characters after diApply / triApply attempts
  lremMap() #create mapping based off of remaining single letter statistics

  #Every letter is now mapped -- Begin hill climbing
  for guesses in range(100000):
    cipherText = ''
    for l in trialText:
      cipherText += l
    test = score(cipherText)

    if test > parent:
      parent = test
      best = trialText

    #make intelligent guesses from relative frequencies while avoiding same mappings
    for l in l2:
      replace(l,choice(l2o),rep=0)
    for l in l3:
      replace(l,choice(l3o),rep=0)
    for l in l4:
      replace(l,choice(l4o),rep=0)
    for l in l5:
      replace(l,choice(l5o),rep=0)
  return best

#Score - compares trialText against quadgram dictionary for overall rating of likeliness
def score(test):
  ptext = ''
  ptext = test
  for x in trialText:
    ptext+=x
  score = 0
  for i in range(len(ptext)-dictL+1):
    if ptext[i:i+dictL] in pdict: score += pdict.get(ptext[i:i+dictL])
    else: score += floor
  return score

# -- Begin Main Code Segment --
# -- Primary Guess Loop --
pos = 0
go = True
while(go):
  #Basic option menu
  print('_________________________________________________________________________________________________')
  print('_________________________________________M__E__N__U______________________________________________')
  dec = input('| b - basic step (DO THIS FIRST!)\n| d - display digram stats\n| t - display trigram statistics\n| r - rollback\n| u - user guess\n| h - hill climb to completion\n| m - remaining options\n| c - display best guess / trialText (hill climbing result)\n| e - end (writes plaintext to file and key): ').lower()
  if dec == 'e':
    go = False #Get out of loop
  elif dec == 'r':
    rbPos = int(input('Enter a position number or -1 for last position: '))
    rollback(rbPos)
    pos-=1 #Negates incriment of letter
  elif dec == 'u':
    #User decision
    userGuess()
  elif dec == 'h':
    print('Please wait a moment for the algorithm...')
    bestguess = hillClimb()
    print(bestguess)
  elif dec == 'm':
    lRemain()
  elif dec == 'c':
    print(trialText)
  elif dec == 'd':
    print('\n',diSort,'\n\n',digrams,'\n')
  elif dec == 't':
    print('\n',triSort,'\n\n',trigrams,'\n')
  elif dec == 'b':
    pos = 0
    #Finds letters sorted by frequency which have > 20% difference in comparison to the next letter
    #Use this stat to fill in primary guesses before moving onto digrams/trigrams
    while(float(numSorted[pos]/numSorted[pos+1]*100-100) > 20):
      print('\n',pos+1,'most frequent letter is:',lSorted[pos],'appearing',numSorted[pos],'times')
      print('It is highly plausible that',lSorted[pos],'may be equal to',primaryLetter[pos])
      print(lSorted[pos],'occurs',float(numSorted[pos]/numSorted[pos+1]*100-100),'% more than',lSorted[pos+1],'- the next most frequently occuring letter in the cipher text')
      pos+=1
    primaryGuesses = pos
    print('\nI feel confident filling in the first',primaryGuesses,'primary letter(s) correctly.\n')

    for i in range(primaryGuesses):
      replace(lSorted[i],primaryLetter[i])

  pos+=1

#Once loop is exitted, save final trialText elements to file
plaintext = ''
for x in trialText:
  plaintext += x
file = open("substitution_plaintext.txt",'w')
file.write(plaintext)
file.write('\n'+str([x for x in replacement]))
