import numpy as np

a1 = np.matrix("1 7 8; 0 3 21; 0 11 4")
og = np.matrix("3 3 3")
result = (og * a1) % 26
print result

result+=[12,17,2]
result = result % 26
print result

result2 = result
#result2-=[12,17,2]
trial = [-12%26,-17%26,-2%26]
result2+=trial
print trial


result = result2 % 26
print result

#print a1.I
#print np.linalg.solve(a1,[3,11,21])

invm1 = np.matrix("1 4 3; 0 2 9; 0 1 21")

print 'here we go...'

og = np.matrix("15 2 23")
result = og * invm1
result = result % 26
print result
