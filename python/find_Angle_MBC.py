#https://www.hackerrank.com/challenges/find-angle/problem?h_r=next-challenge&h_v=zen

import math

ab = int(input())
bc = int(input())

ac = (ab**2 + bc**2)**0.5
mc = ac/2

cosC = bc / ac 

bm = (mc**2 + bc**2 - 2*mc*bc*cosC)**0.5

cosMBC = (bm**2 + bc**2 - mc**2)/(2*bm*bc)

# c^2 = a^2 + b^2 - 2(a)(b)(cos beta)

theta = round(math.degrees(math.acos(cosMBC)))

degree_sign= u'\N{DEGREE SIGN}'

print("{}{}".format(theta,degree_sign))
