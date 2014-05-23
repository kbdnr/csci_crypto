#Basic GCD calculator

#Takes two numbers as input and finds greatest common divisor
num1 = input('Enter num1: ')
num1 = int(num1)
num2 = input('Enter num2: ')
num2 = int(num2)

#def gcdCalc(num1,num2):

#Euclidean Algorithm
#Find larger of two input numbers
if num1 > num2:
  larger = num1
  smaller = num2
else:
  larger = num2
  smaller = num1

largerList = [larger]
smallerList = [smaller]
remainderList = []
dividendList = []

#calculate GCD(larger,smaller)
#add value to be removed to enter loop
remainderList.append(1)

arrayPos = 0

while(remainderList[-1] != 0):
  if arrayPos == 0:
    #remove arbitrary value to begin computation
    remainderList.pop(arrayPos)

  #integer division
  dividendList.append(largerList[arrayPos] // smallerList[arrayPos])
  remainderList.append(largerList[arrayPos] % smallerList[arrayPos])
  largerList.append(smallerList[arrayPos])
  smallerList.append(remainderList[arrayPos])

  #increment array position
  arrayPos+=1

#Debug2
print('larger', largerList,'smaller', smallerList, 'remainder', remainderList,'dividend', dividendList)
gcd = smallerList[len(remainderList)-1]
print('GCD is ',gcd,'\n')

#Euchlidean Extended Algorithm
print('Euclidean Extended Algorithm structure')
x = 0
for x in range(len(remainderList)):
  print(largerList[x], '=',dividendList[x],'*',smallerList[x],'r',remainderList[x],'\n')

for x in range(len(remainderList)):
  print(remainderList[x],'=',largerList[x],'-',dividendList[x],'*',smallerList[x])
