print('hoàng đình thịnh msv 235752021610114')
import math;
x1=int(input('enter x1--->'))
y1=int(input('enter y1--->'))

x2=int(input('enter x2--->'))
y2=int(input('enter y2--->'))

d1 = (x2-x1) * (x2-x1);
d2 = (y2-y1) * (y2-y1);
res = math.sqrt(d1+d2)
print('distance between two points:', res);
