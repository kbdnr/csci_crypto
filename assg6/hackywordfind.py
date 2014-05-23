#Basic word finder

file = open('7lwords.txt')

for line in file:
  if len(line) < 7:
    pass
  else:
    if line[1] == 'a' and line[6] == 'a':
      print line
