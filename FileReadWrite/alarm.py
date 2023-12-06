import sys
import math

fi = open('alarm.inp', 'r')
fo = open('alarm.out', 'w')

n = int(fi.read())
seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
hh, mm = [], []

for i in range(0, 24):
    hh.append(seg[i//10] + seg[i%10])
for i in range(0, 60): 
    mm.append(seg[i//10] + seg[i%10])
for i in range(0, 24):
    for j in range(0, 60): 
        if hh[i] + mm[j] == n: 
            fo.write(str(i//10) + str(i%10) + ':' + str(j//10) + str(j%10))
            exit()
fo.write('Impossible')