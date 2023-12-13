fi = open('calendar.inp','r')
fo = open('calendar.out','w')

w = int(fi.readline())
d,m = map(int, fi.readline().split())

dem = d+(m-1)*30 + (m-1)//2 + (m-1)%2 - 1
num = (w + dem%7) % 7
if num == 0: num=7

fo.write(str(num))